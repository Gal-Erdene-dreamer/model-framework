"""
Created on Fri Feb  5 12:00:11 2021

@author: Nick Geertjens, initial structure by Pim de Vink
"""
import os
from collections import defaultdict
import re
import string
import sys

from sympy import Symbol, Pow, sympify, degree

from src.localization.creator_strings import strings


def build_model_file(name, equations, labeled, data_mode, custom_input):
    """
    Creates a custom model file for use with the model framework.
    
    Parameters
    ----------
    Name: String
        The name to use for the created model file, if the file exists, an 
        exception will be raised.
    Equations: String
        Multiline string describing the system. See 'text_to_massbalance' or
        the example input.
    labeled: String
        Which specie is labeled for detection in the experiment. Depending
        on the data_mode, this value is used in order to set up the function.
    Data_mode: {'anisotropy', 'custom'}
        The manner in which state is related to the system data.
        Possible modes:
            'anisotropy': Default anisotropy measurement, unbound labelled 
            specie gives min anisotropy, all other combinations containing
            labelled result in max signal. Can also be used for other
            techniques where unbound results in the low signal and bound
            results in the high signal while the individual contributions
            can be summed.
            'inverse_anisotropy': Equal to the anisotropy mode but inversed.
            Unbound results in high signal, while all other complexes
            containing the specie results in low signal.
            'itc': ITC measurement of a single complex forming. IMPORTANT:
            this mode expects total heat as measurement value. NOT the delta
            heat. Each measurement point should be the total heat produced
            up to that point.
            'custom': Will try to parse the value in custom_input into
            a data equation. If no input is given, will show the determined
            model equations but raise an exception afterwards.
    Custom_input: String
        When the 'custom' data_mode is chosen, this string will be evaluated
        in order to define the custom data function.
        
    Post
    ----
    Writes a 'name'.py model file to the output directory suitable for use
    with the model framework, adhering to the given mode. 
    """
    print('Attempting to create new model file...')
    data_mode = data_mode.lower()
    # First add the input to the header, for reference then start processing
    header_text = _header_text(equations, labeled, data_mode, custom_input)
    
    equations, species, recipes, constants, mass_balance = text_to_massbalance(equations)
    if data_mode.lower() == 'custom':
        custom_input = _proces_custom_input(custom_input, species,
                                                constants, mass_balance)
    _anti_blackbox(equations, species, recipes, constants, mass_balance,
                   data_mode, custom_input)
    
    variable_text = _variable_text(
        equations, species, recipes, constants, labeled)    
    system_equations_text = _system_equations_text(equations)
    update_state_text = _update_state_text(
        equations, species, recipes, constants)
    data_function_text = _data_function_text(
        data_mode, species, labeled, custom_input, recipes)
    
    os.makedirs('output/', exist_ok=True)
    with open(f'output/{name}.py', 'x', encoding="utf-8") as f:
        f.write(header_text)
        f.write(strings['imports'])
        f.write(variable_text)
        f.write(system_equations_text)
        f.write(update_state_text)
        f.write(data_function_text)
        
    print("Finished building file.")
    

def text_to_massbalance(text):
    """
    Processes a multiline string and determines the massbalance equations 
    defined in it.
    
    Pre
    ---
        Each reaction is entered on a single line in the text.
        A reaction is defined as followed:
            A + B = AB; Kd1
            
        The equality sign separates the before and after, the semicolon
        is followed by the reaction rate. The rate is defined as the reverse
        reaction rate (dissociation constant), such that the above example 
        results in the following equilibrium:
            [A]*[B] / Kd1 = [AB]
        
        Each specie name can only contain alpha-numerical characters.
        The names of the species start with a capital letter and should
        only contain other capital letters to indicate formation of a complex.
        e.g.:   'A', 'B', 'Enzyme', 'Q8' are all valid specie names.
                'AB', 'EnzymeB', 'CaDaBa' are all valid names for the combined
                species of A + B, Enzyme + B and Ca + Da + Ba respectively.
        Thus, AR + A results in a different input than Ar + A.
                
        If multi character specie names are used, make sure that each
        *specie* name is unique, and not a subsection of a different name.
        e.g.: If both Partner and P are present, searching for 'P' will lead
        to unintended behavior. 
        In this case, instead use Partner and Ps for example. 
        
        Adhering to these naming concenventions allowes the function to check
        for common errors, such as AB + C and AC + B should both result in the
        same combination of compounds ABC, instead of two seperate 
        combinations, ABC and ACB.
        If this behavior unwanted, instead use unique names for each specie
        rather than combinations of componenet names.
        e.g.: AB + C = Abc and AC + B = Acb.
        
        Rate constants can be defined as single rates or the ratio / product 
        of other rates. Rates are not orded by capital letters as species
        are and constant names are case sensitive. Brackets are not supported 
        in rate definition and no implicit multipication is detected. 
               
        e.g.: The input 'AB' is not seen as the rate 'A * B', but as a single 
        rate 'AB'.
        'Kd2', 'kd', 'Kd4/ alpha', 'beta * C' are all valid inputs, where the 
        last two are detected as rates composed of multiple constants.
    
    Parameters
    ----------
    Text: String
        Multiline string with the input equations.
    
    Returns 
    -------
    equations: dictionary
        Contains all the equilibrium equations. If a specific input vector
        result in zero for each equation, that input corresponds to the 
        concentrations of the species at equilibrium.
        Equations are stored as pairs:
            independent_variable: equilibrium equation equal to zero
    species: set
        All species present in the system
    recipes: dictionary
        Contains the formulas for calculating the concentrations of the
        dependent species from the independent species as:
                dependent_specie: formula.
    constants: set
        All rate constants defined in the system.
    mass_balance: dictionary
        Contains the sum of all specie concentrations that should add up to 
        the total concentration for each independent specie. Also contains 
        appropiate weights when a specie is contained in a complex multiple
        times.
    """
    equations = dict()
    species = set()
    
    recipes = dict()
    all_recipes = defaultdict(list)
    
    constants = set()
    mass_balance = dict()
    
    # Whitespace removal translation table
    trans_table = str.maketrans('','', string.whitespace)

    for line in text.splitlines():
        if len(line) == 0:
            continue
        _structure_check(line)
        
        # Remove whitespaces and split into parts
        equality = line.split('=')
        left = equality[0].translate(trans_table)
        right, rate = [string.translate(trans_table)
                       for string in equality[1].split(';')]
        
        # Split left side in species and process
        left = left.split('+')
        left = [_process_specie(specie) for specie in left]
        
        # Check that there is only one specie in right hand 
        if any(c in right for c in ['*', '+']):
            raise NotImplementedError(
                "Handling of multiple species on right-hand side is "
                "not supported. Please use an intermediate step if required.")
        construct = _process_specie(right)
                
        # Process the constant(s)
        rate = _process_rate(rate)
        
        # Update all the sets
        # Processing input 2*A returns A**2, not A, so we need to account for
        # this.
        left_atoms = set().union(*[x.atoms(Symbol) for x in left])
        species = species.union(left_atoms, [construct])
        constants = constants.union(rate.atoms(Symbol))
        
        # Create the recipe
        recipe = _product(left) / rate
           
        # Add the new recipe
        all_recipes[construct].append(recipe)
        recipes[construct] = recipe
    
    # Determine the independent vars
    independent_vars = species.difference(recipes.keys())
    
    # Check that there are no illegal overlapping names
    _name_check(independent_vars)
    
    # Simplify recipes and check for definition sanity
    errors = 0
    for construct, methods in all_recipes.items():
        recipes[construct] = recipes[construct].subs(recipes)
        if len(methods) > 1:
            errors += _specie_definition_check(recipes, methods, construct, 
                                     independent_vars)
    if errors > 0:
        sys.exit('Model definition error')
         
    # Prepare the final result
    for specie in independent_vars:
        # Create the base, which is the free concentration minus total
        # concentration. 
        specie_tot = Symbol(str(specie)+'_tot')
        base = [specie - specie_tot]
        
        # Setup mass_balance equation
        mass_equation = [specie]
        
        # Now find all other species that contain the independent specie 
        others = []
        for product, recipe in recipes.items():
            # Check if our specie is in the recipe
            count = degree(recipe, specie)
            if count > 0:
                others += count * [recipe] 
                mass_equation += count*[product]
                
        equation = sum(base + others)
        equations[specie] = equation
        mass_balance[specie_tot] = sum(mass_equation)
    return equations, species, recipes, constants, mass_balance       

def _specie_definition_check(recipes, methods, construct, independent_vars):
    """
    Performs sanity check on the proposed definition. If there are multiple
    ways to construct a given specie, all methods should contain the same
    component numbers and rate constants (path independence).
    """
    # Get the component numbers
    construct_degrees = [(var, degree(recipes[construct], var)) 
                   for var in independent_vars]
    
    # Each method should have same component degrees and rate constants
    for recipe in methods:
        subed_recipe = recipe.subs(recipes)
        recipe_degrees = [(var, degree(subed_recipe, var))
                           for var in independent_vars]
        if recipe_degrees != construct_degrees:
            print(f'ERROR: Multiple pathways exist for {construct}​, but they do not ' 
                  'have the same building blocks:')
            print('    ', *recipe_degrees)
            print('    ', *construct_degrees)
            return True
        elif subed_recipe != recipes[construct]:
            bars = min(max(len(str(recipes[construct])), len(str(subed_recipe))), 30) 
            print(f'ERROR: Multiple pathways exist for {construct}​, but they do not ' 
                  'have the same product of equilibrium constants:')
            print('    1st:', recipes[construct])
            print('    2nd:', subed_recipe)
            print(9*' '+bars * '―', '/ divide')
            print(8*' ','=', recipes[construct]/subed_recipe,'-should be equal to 1.')    
            return True
        else:
            return False
            
def _anti_blackbox(equations, species, recipes, constants, mass_balance,
                   data_mode, custom_input):  
    print('The following constants were found in the specified input:')
    print(*constants, sep=', ')
    print()
    
    print('The following species were found in the specified input:')
    print(*species, sep=', ')
    print()
    print('From these species, the following cannot be "created" '
          'in the current model definition (the components of the system). ' 
          'They determine the solution of the system and the concentrations ' 
          'of the other species. They will be labeled as "independent" in the '
          'model file.')
    print(*equations.keys(), sep=', ')
    print()
    print('The concentrations of the other species in equilibrium can be ' 
          'determined based on the concentrations of the independent ' 
          'species and the equilibrium constant, using the following '
          '"recipes". They will be labeled as "dependent":')
    for dependent, recipe in recipes.items():
        print(f'{dependent}: {recipe}')
    print()
    print('The total concentration of each independent specie is constant. ' 
          'The sum of the concentrations of all species that contain that '
          'independent species, correcting for complexes that contain the ' 
          'independent specie multiple times, should therefore also be constant '
          '(notice the distinction between "A", the free concentration '
          'and "A_tot", the total concentration, independent of binding):')
    for total, recipe in mass_balance.items():
        print(f'{total}: {recipe}')
    print('\nSubstituting the recipes above:')
    for independent, recipe in equations.items():
        independent_total = str(independent) + '_tot'
        recipe = str(recipe).replace('- '+ independent_total, '')
        print(f'{independent_total} = {recipe}')
    print()
    print('Finally, we rewrite these equations to equal zero, and divide '
          'by the total concentrations on both sides in order to reach a '
          'solution faster during solving. This form can also be found in the '
          'model file:')
    for independent, recipe in equations.items():
        print(f'{independent}: ({recipe}) / {independent}_tot = 0')
    
    if data_mode.lower() == 'custom':
        if custom_input is not None:
            print('\nThe given custom data mode was processed to:\n'
                  f'{custom_input}')
        else:
            raise sys.exit('Custom data mode was selected but no custom input '
                         'was given. Please define the custom function.')
            
    print('\nNOTE: please carefully inspect the above information to prevent '
          'any errors in model definition.\n')    

def _proces_custom_input(custom_input, species, constants, mass_balance):
    """
    Processes the custom input, add any new variables as constants and checks
    for illegal names. If the input was empty, return None,
    otherwise the symbolic expression.
    
    Raises
    ------
    ValueError
        If none of the variables in the equation relate to a concentration
        in the system.
    """
    if len(custom_input) > 0:
        equation = sympify(custom_input)
        variables = equation.atoms(Symbol)
        
        # A physical sensisble data function contains at least one system
        # concentration.
        if not any(var in species for var in variables):
            raise ValueError('None of the specie concentrations in the system '
                     'detected in the custom equation. The data function '
                     'needs to be concentration dependent. All values entered '
                     'are case sensitive.\n'
                     f'Detected species: {species}\n'
                     f'Custom function variables: {variables}')
            
        # Add any new variables defined to our constants set. Mass_balance keys
        # contains the total concentration of each independent specie.
        for var in variables:
            if (not var in species and not var in constants 
                                        and not var in mass_balance.keys()):
                if not str(var).isalnum():
                    raise ValueError(f'Newly defined variable "{var}" in custom ' 
                                     'input contains non alphanumerical '
                                     'characters.')
                constants.update({var}) 
        return equation         
    else:
        return None
          

def _product(list_like):
    """
    Helper function, returns the product of all items in the iterable,
    not robust.
    """
    if len(list_like) == 0:
        return None
    
    result = 1
    for item in list_like:
        result = result * item
    return result
        
def _structure_check(line):
    """
    Check that the general structure of a line for text_to_massbalance 
    is correct.
    
    Parameters
    ----------
    Line: String
        Input to be checked.
    
    Raises
    ------
    ValueError: if not exactly 1 ('=' or ';') is found && 
        if ';' appears before '='.
    """
    if (line.count('=') != 1 or line.count(';') != 1):
        raise ValueError(
            "Incorrect number of '=' and/ or ';' detected in a single line.\n" 
            + f"please check: {line}")
    if (line.find('=') > line.find(';')):
        raise ValueError(
            f"Rate declaration detected before equality.\nPlease check {line}")

def _process_specie(specie):
    """   
    Process a specie obtained during text_to_massbalance for mass-balance
    equations.
    
    First determines if the specie name consists of just alpha-numerical
    characters. Then, the 'buildingblocks' are sorted to prevent
    that ACD and ADC become 2 seperate molecules. A buildingblock is any
    part of the string starting with a capital letter.
    
    correct inputs:
        A, B, Ce, Component, ACD, ADC, CeAD
    outputs for sample inputs:
        A, B, Ce, Component, ACD, ACD, ACeD 
        
    Returns
    -------
    sympy Symbol of processed specie
        
    Raises
    ------
    ValuesError: if specie name is not alphanumerical or does not start with
    a capital letter.
    """
    # While sympify could be used here, using eval can lead to security risks
    # if the code is ever ran on a server like structure. As there is almost no
    # performance loss, the already written method which prevents the use of 
    # eval was kept.
    power = 1
    if specie.count('*') == 1:
        items = specie.split('*')
        if items[0].isnumeric() and not items[1].isnumeric():
            power = int(items[0])
            specie = items[1]
        elif items[1].isnumeric() and not items[0].isnumeric():
            power = int(items[1])
            specie = items[0]
        else:
            raise ValueError('Detected a multiplication symbol in specie '
                              f'but could not correctly process: {specie}')
    
    # Make sure no special characters are left
    if not specie.isalnum():
        raise ValueError("Specie consists of none alphanumerical "
                         f" characters: {specie}")
    
    # Check that first letter is capital:
    if not specie[0].isupper():
        raise ValueError(
            f'Please start specie names with a capital letter: {specie}')
    substituents = sorted(re.split('(?=[A-Z])', specie))
    specie = ''.join(substituents)
    return Pow(Symbol(specie), power)

def _process_rate(rate):
    """
    Process a rate string obtained during text_to_massbalance.
    
    Pre
    ---
    Constant names contain only alpha-numerical characters, starting with
    an alphabetic character.
    
    Returns
    -------
    Sympy function of the rate string
    """
    if '-' in rate or '+' in rate:
        raise ValueError('Addition and subtraction in rate constants is not ' 
                         'supported. Please make a seperate variable if ' 
                         'required')
    result = sympify(rate)
    violations = [str(C) for C in result.atoms(Symbol) if not str(C).isalnum()]
    if len(violations) != 0:
        raise ValueError('The following rate constant(s) violate naming ' 
                         'rules: {}'.format(', '.join(violations)))
    return result       

def _name_check(species):
    """
    Helper function to check that there is no overlap in independent specie
    names. This could lead to unintended behavior.
    """
    species = [str(specie) for specie in species]
    for specie in species:
        occurence = sum([specie in other for other in species])
        if occurence > 1:
            raise ValueError(f"Specie name: '{specie}' overlaps with "
                             f'other specie names. {*species,}')

def _header_text(equations, labeled, data_mode, custom_input):
    """
    Helper function to create the header docstring for the model creator
    
    Parameters
    ----------
    equations: String
        The original input equations
    labeled: String
        The specie entered as labeled
    data_mode: String
        The chosen mode
    custom_input: String
        The custom input string
        
    Returns
    -------
    Multiline string representing model file header
    
    """
    function_string = strings['header']
    function_string += equations + '\n'
    function_string += f'Labeled specie: {labeled}\n'
    function_string += f'data_mode: {data_mode}\n'
    if data_mode.lower() == 'custom':
        function_string += f'custom input: {custom_input}\n'
    function_string += '"""\n\n'
    return function_string

def _variable_text(equations, species, recipes, constants, labeled):
    """
    Helper function to create the variable text for the model creator.

    Parameters
    ----------
    equations: dictionary
        Equations solution generated by text_to_massbalance
    species: Set
        species result from the text_to_massbalance function.
    recipes: dictionary
        Recipes result from the text_to_massbalance function.
    constants : Set
        Constants result from the text_to_massbalance function.
    labeled: String
        The model_builder input value for 'labeled', the species that has
        been labeled / tracked in the experiment.

    Raises
    ------
    ValueError:
        If not at least one species is found containing the given label.
        
    Returns
    -------
    Multiline string which defines the variables used in the model file.

    """
    variables = species.union(constants)
    variables = ([str(var) for var in variables] + 
                 [str(var)+'_tot' for var in equations.keys()])
    variable_text = strings['variables_base']
    variable_text += 'variables = ' + str(variables) + '\n'
    
    variable_text += strings['independent_base']
    independent_vars = [str(var) for var in equations.keys()]
    variable_text += f'independent_species = {independent_vars}\n'
    
    variable_text += strings['dependent_base']
    dependent_vars = [str(var) for var in recipes.keys()]
    variable_text += f'dependent_species = {dependent_vars}\n'
    
    variable_text += strings['constants_base']
    constants_txt = [str(constant) for constant in constants]
    variable_text += f'constants = {constants_txt}\n'
    
    label_vars = [str(var) for var in species if labeled in str(var)]
    if len(label_vars) < 1:
        raise ValueError(
            "build_model_file found no variables corresponding to the given "
            "label. (Case sensitive)")
    variable_text += strings['labeled_base']
    variable_text += f'labeled_components = {str(label_vars)} \n\n'
    return variable_text

def _system_equations_text(equations):
    """
    Helper function to create the system equation function for the 
    model creator.
    
    Parameters
    ----------
    equations: dictionary
        Equations solution generated by text_to_massbalance
        
    Returns
    -------
    Multiline string defining the system_equations function.
    """
    function_string = strings['equations_base']
    for i, var in enumerate(equations.keys()):
        function_string += f'    {var} = concentrations[{i}]\n'
        
    function_string += '\n'
    function_string += '    # Readability\n'
    
    species = set().union(*[eq.atoms(Symbol) for eq in equations.values()])
    species = species.difference(set(equations.keys()))
  
    for specie in sorted(species, key=str):
        comp = str(specie)
        function_string += f'    {comp} = state.{comp}\n'
    function_string += '\n'
    function_string += f'    result = np.zeros({len(equations.keys())})\n'
    
    for i, (var, eq) in enumerate(equations.items()):
        function_string += f'    result[{i}] = ({str(eq)}) / {var}_tot\n'
    function_string += '    return result \n\n\n'
    return function_string


def _update_state_text(equations, species, recipes, constants):
    """
    Helper function to create the update_state function for the model creator.
    
    Parameters
    ----------
    equations: dictionary
        Equations solution generated by text_to_massbalance
    species: Set
        species result from the text_to_massbalance function.
    recipes: dictionary
        Recipes result from the text_to_massbalance function.
    constants : Set
        Constants result from the text_to_massbalance function.
        
    Returns
    -------
    Multiline string defining the update_state function.
    """
    function_string = strings['update_base']
    
    function_string += '    # Independent variables\n'
    for i, var in enumerate(equations.keys()):
        function_string += f'    state.{var} = solution[{i}]\n'
    function_string += '\n'    
    
    function_string += '    # Readability \n'
    dependent = set(equations.keys())
    for specie in sorted(dependent.union(constants), key=str):
        function_string += f'    {specie} = state.{specie}\n'
    function_string += '\n'


    function_string += '    # Dependent variables\n'
    for specie, recipe in recipes.items():
        function_string += f'    state.{specie} = {str(recipe)}\n'
    function_string += '\n\n'
    return function_string    


def _data_function_text(mode, species, labeled, custom_input, recipes):
    """
    Helper function to create the data function for the model creator, 
    based on a given mode.
    
    Parameters
    ----------
    Mode: String
        Specific form the data function takes. Modes are defined in
        build_model_file doc string.
    species: Set
        species result from the text_to_massbalance function.
    Labeled: String
        The species that has been labeled / tracked in the experiment.
    Custom_input: String
        Used with mode = custom, the processed version of the custom_input by
        _proces_custom_input.
    Recipes: Dictionary
        Recipes result from text_to_mass_balance function
    """
    components = [specie for specie in species if specie not in recipes.keys()]
    contains_labeled = [specie for specie, recipe in recipes.items()
                        if labeled in str(recipe)]
    function_string = strings['data_base']
    mode = mode.lower()
    
    if mode == 'anisotropy' or mode == 'inverse_anisotropy':
        total_labeled = Symbol(f'{labeled}_tot')
        labeled = Symbol(labeled)
        if labeled not in components:
            raise ValueError('Default (inverse) anisotropy data-mode expects '
                    'one of the system components as labeled specie. Please ' 
                    'use custom data mode if this is not the the case.')
        
        fraction_upper = []
        for specie in contains_labeled:
            recipe = recipes[specie]
            count = degree(recipe, labeled)
            if count != 1:
                raise ValueError('Labeled component contained multiple times '
                    f'in complex: {specie}. Anisotropy contribution for each '
                    'of the different complex sizes is poorly defined. '
                    'Please use a custom data function.')
            fraction_upper.append(specie)
        
        if mode == 'anisotropy':
            bound_part = Symbol('data_max') * sum(fraction_upper) / total_labeled    
            unbound_part = Symbol('data_min') * labeled / total_labeled 
        else:
            bound_part = Symbol('data_min') * sum(fraction_upper) / total_labeled    
            unbound_part = Symbol('data_max') * labeled / total_labeled 
            
        complete = unbound_part + bound_part
        function_string +='    # Readability\n'
        for specie in sorted(complete.atoms(Symbol), key=str):
            specie = str(specie)
            function_string += f'    {specie} = state.{specie}\n'
        function_string += '\n'
        function_string +=f'    return {complete}\n\n\n'  
        
    elif mode == 'itc':
        total_labeled = Symbol(f'{labeled}_tot')
        labeled = Symbol(labeled)
        if labeled not in components:
            raise ValueError('Default ITC data-mode expects one of '
                    'the system components as labeled specie. Please use '
                    'custom data mode if this is not the the case.')
        
        if len(contains_labeled) != 1:
            raise ValueError('Did not find one (and only one) complex with '
                        'labeled component. Default ITC is only defined for '
                        'a single binding event. Please use a custom '
                        'function if this is not the case.')            
            
        # Only a single labeled construct
        fraction_bound = contains_labeled[0] / total_labeled

        function_string +='    # Readability\n'
        for component in sorted(fraction_bound.atoms(Symbol), key=str):
            component = str(component)
            function_string += f'    {component} = state.{component}\n' 
        for limit in ['data_min', 'data_max']:
            function_string += f'    {limit} = state.{limit}\n'

        function_string += ("\n    q_constant = data_min if abs(data_min) > " 
                            "abs(data_max) else data_max\n")
        function_string += (f'    return {fraction_bound} * q_constant')
        
    elif mode == 'custom':
        if custom_input == '':
            function_string += ('    raise NotImplementedError("Model creator '
                'custom data function was chosen but has not been entered yet. '
                'Please edit the model file.")\n\n')
        else:
            function_string += '    # Readability\n'
            for atom in custom_input.atoms(Symbol):
                function_string += f'    {atom} = state.{atom}\n\n'
            function_string += '    return ' + str(custom_input)
    else:
        raise ValueError(
            "Unsupported mode given for the data function creator.")
    return function_string       
                     