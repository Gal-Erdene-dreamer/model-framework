# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:27:54 2021

@author: N.H.J. Geertjens
"""
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'model')))
from importlib  import import_module
import matplotlib.pyplot as plt

import src.setup_types
import src.post_process

def run(*, model, input_folder, titrate, setup_type, fit_parameters, 
        known_parameters, analysis, style, **kwargs):
    """
    This script is the main driver behind the facade presented in 'main'.
    
    In order to facilitate the easy addition of new functions, additional
    named parameters can be supplied to **kwargs. All functions are offered 
    these variables. Because of this setup, it is advisible to start with
    the name of the function for new arguments. E.g. landscape_par_range for
    the landscape function.

    Parameters
    ----------
    model : python module reference
        Reference to a model file created using the 'model creator', or 
        manually defined.
    input_folder : String / pathlike
        The folder where the experimental data is located
    titrate : String
        The model species which corresponds to the concentrations in the 
        input data, the species with changing total concentration.
        Note: Please remember that the parameter name corresponding to the
        total species concentration should be entered here, not the free
        concentration. In order to prevent common errors, the model builder
        always adds the suffix '_tot' to total concentration parameters.
        The driver script only accepts parameters ending in '_tot'.
    setup_type : String
        The name of the function to use during setup, as string.
        The corresponding function will be called during setup of the system.
    fit_parameters : dictionary of string: float
        The model parameters to fit as keys with as value their initial guess,
        the starting point for the solver.
    known_parameters : dictionary of string: float
        The model parameters that are known or set beforehand with their
        respective values. Together with fit_parameters all parameters
        should be covered.
    analysis : list of Strings
        List of strings corresponding to the names of the functions in
        'post_process' which should be run after finding a solution to the
        systems.
    style: str, dict, Path or list
        A valid style file for matplotlib, see matplotlib.style.use.
    **kwargs : optional parameters
        Any other named parameters will be given to the functions called
        as optional parameters.

    Raises
    ------
    ValueError
        If any of the following can not be found:
            -The supplied model file
            -The supplied setup function
            -The supplied analysis function
        If each fit or known parameter does not have a non-negative value.
        If no csv files are found in the input folder
        If the titrate entered does not end in '_tot' 

    Returns
    -------
    systems : System object
        List of the system(s) that were setup during this method.

    """
    
    # Check that all references exist.
    try:
        model = import_module('model.'+model)
    except ModuleNotFoundError:
        raise ValueError(
            f"'/model/{model}' could not be found. (case sensitive)") 
    try:
        setup = getattr(src.setup_types, setup_type.lower())
    except AttributeError:
        raise ValueError("src.driver could not find setup_type: "
                         f"'{setup_type.lower()}' in src.setup_types")   
    try:
        analysis_functions = [getattr(src.post_process, func.lower()) 
                              for func in analysis]
    except AttributeError as e:
        faulty_argument = e.args[0].split("'")[-2]
        raise ValueError("src.driver could not find analysis: "
                         f"'{faulty_argument}' in src.post_process")  
    
    # Add parameters to kwargs so all other function can excess them if needed
    kwargs['fit_parameters'] = fit_parameters
        
    # Check other parameters
    for key, value in dict(list(fit_parameters.items()) + 
                           list(known_parameters.items())).items():
        try:
            if not value < 0 and not value > 0:
                raise ValueError(
                    f'Parameter values are not allowed to be zero: {key}.')
        except TypeError:
            raise TypeError(
                f'Non-number value detected for fit_parameter: {key}')
           
    split_titrate = titrate.split('_')
    if split_titrate[-1] != 'tot':
        raise ValueError('Please make sure to enter the parameter '
                'corresponding to the total concentration as titrate ('
                'ends in "_tot").')
    
    if input_folder[-1] != '/':
        input_folder += '/'
    
    # Load matplotlib style
    plt.style.use(style)

    # All setup parameters okey, setup the system(s). 
    systems = setup(input_folder = input_folder, model = model, 
                    titrate = titrate, known_parameters = known_parameters, 
                    **kwargs)
    
    for system in systems:
        if len(fit_parameters) > 0:
            print('Solving system...')
            system.solve(fit_parameters = fit_parameters)
            system.print_solution()
        else:
            print(
                'Notice: No parameters to fit, no solution can be determined.' 
                '\nContinuing with analysis.\n')
            
        for func in analysis_functions:
            func(system, **kwargs)
    
    # Return systems so other code can be run on it.
    return systems
        

