# -*- coding: utf-8 -*-
""""""
"""
Created on Wed Dec 16 21:08:24 2020

@author: N.H.J. Geertjens

"""
import os

from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd

from src.analysis.outliers import doornbos_outlier, UndeterminedError
from src.analysis.bootstrap import bootstrap
from src.analysis.helpers import _axis_unit_label, timer


from functools import wraps

"""
The first and only positional argument supplied is system, the system object
that is currectly being investigated. Any required arguments should be given
as named arguments. Finally, each function should contain the **kwargs
argument, which holds the unused arguments, which are intended for other
funcions.

You can iterate over a system. The basic system will return each condition
associated with it. Len(system) returns the number of conditions.
"""

def write_to_file(func):
    """
    A decorator that allowes any function that returns a dataframe to save
    this dataframe as a csv file in the output folder.
    
    Pre
    ---
    func returns a pandas.dataframe or other object with .to_csv method.
    
    Raises
    ------
    NotImplementedError
        If returned result does not have a .to_csv() method.
    
    Post
    ----
    func return written to 'output/*time* *function_name*.csv'
    
    """
    @wraps(func)
    def wrapper_to_file(*args, write_output = True, **kwargs):
        kwargs['write_output'] = write_output
        result = func(*args, **kwargs)
        if write_output == True:
            try:
                time = datetime.now().strftime("%Y-%m-%d %H%M%S")
                os.makedirs('output/', exist_ok=True)
                result.to_csv(f'output/{time} {func.__name__}.csv', sep=';')
                print(f'{func.__name__} created output file.')
            except AttributeError:
                raise NotImplementedError(
                    '@write_to_file decorator can only be used on functions '
                    'that return a dataframe')
        return result
    return wrapper_to_file

def save_plot(fig, name, /, *, write_output = True, **kwargs):
    """
    Common function that most plot-producing functions use in order to save
    the generated fig as a svg file.
    """
    if write_output:
        os.makedirs('output/', exist_ok=True)
        time = datetime.now().strftime("%Y-%m-%d %H%M%S")
        fig.savefig(f'output\{time} {name}.svg', format='svg', dpi=1200)
            

def plot_data(system, *, plot = None, normalise = False, **kwargs):
    """
    Itterates over the conditions associated with the provided system and 
    plots the condition.data for each.
    
    Parameters
    ----------
    system : System object
        System object to plot the associated data for.
    plot : matplotlib (fig, ax) tuple , optional
        Figure to continue plotting in. If none, create new figure.
    normalise: boolean
        Wheter to normalise all datapoint between 0-1.

    Returns
    -------
    fig : matplotlib.figure object
        Figure / ax to add other plots.
    ax : matplotlib.axes object
        Figure / ax to add other plots..

    """
    if plot is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = plot
    
    # Determine colors
    n = len(system)
    ax.set_prop_cycle('color',[plt.cm.turbo(i) for i in np.linspace(0, 1, n)])
    
    # Plot the data
    for condition in system:
        concentrations = condition.data.index.to_numpy()
        measurements = condition.data.mean(axis=1)
        if normalise:
            measurements = ((measurements - measurements.min()) / 
                            (measurements.max() - measurements.min()))
            
        ax.plot(concentrations, measurements, marker='o',
                label=condition.name, ls='')
    
    # Modify graph looks
    ax.set_xscale('log') 
    ax.set_title(f'Data point plot {system.name}')
    ax.set_xlabel(f'Concentration {system.titrate} (M)')
    if normalise:
        ax.set_ylabel('Normalised data value')
    else:
        ax.set_ylabel('Data value')
    if n > 1:
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True)
        
    return fig, ax


@write_to_file
def plot_model(system, normalise = False, model_plot_min = None,
               model_plot_max = None, **kwargs):
    """
    Itterates over the conditions associated with the provided system and 
    plots system.data and model solution (as a line) for each. If no solution 
    is determined, the current parameter values are tried instead.

    Parameters
    ----------
    system : System object
        System objects to plot the data and model prediction for.
    normalise: boolean
        Wheter to normalise all datapoint between 0-1.
    model_plot_min : float
        The minimum titrate concentration to plot
    model_plot_max : float
        The maximum titrate concentration to plot
        
    Warnings
    --------
    Modifies system.state
    
    Returns
    -------
    Matplotlib plot
        The plotted data
    pandas.dataframe
        Dataframe containing the raw numbers plotted.

    """    
    if system.solution is not None:
        system.set_solution_state()

    fig, ax = plot_data(system, normalise = normalise, **kwargs)
    series = []
    
    for sys in system:
        concentrations = sys.data.index.to_numpy()
        if model_plot_min is None:
            bottom = min(concentrations)
        else:
            bottom = model_plot_min
        
        if model_plot_max is None:
            top = max(concentrations)
        else:
            top = model_plot_max
        concentrations = np.geomspace(bottom, top, 100)
        values = sys.range_to_prediction(concentrations)
        if normalise:
            values = ((values - values.min()) / 
                            (values.max() - values.min()))
            
        ax.plot(concentrations, values, marker='', linestyle='-', 
                label=sys.name)
        # Track plotted points in order to allow writing to file
        series.append(pd.Series(
            data = values, index= concentrations, name = sys.name))
        
    ax.set_title(f'Model plot {system.name}')
    plt.show()
    
    #Save the figure
    save_plot(fig, 'plot_model', **kwargs)
    
    df = pd.concat(series, axis=1)
    return df

@write_to_file    
def residuals(system, **kwargs):
    """
    Gets the residuals from system and plots them against the titrate
    concentrations.
    
    Parameters
    ----------
    system: System object
        The system to plot the residuals for.
    
    Returns
    -------
    Matplotlib plot
        Scatterplot displaying the residuals between model prediction and
        measured values.
    pandas.dataframe
        Dataframe containing the numbers plotted.
    """
    if system.solution is None:
        raise TypeError('Cannot plot residuals before determining solution.')
    df = system.solution.residuals
    fig, ax = plt.subplots()
    
    # Set up the color scheme
    n = len(df.columns)
    ax.set_prop_cycle('color',[plt.cm.turbo(i) for i in np.linspace(0, 1, n)])
    
    # Plot the points
    for col in df.columns:
        ax.plot(col, marker='o', linestyle='', data=df)
    
    # Modify graph looks
    ax.set_xscale('log') 
    ax.set_title("Residual after fit")
    ax.set_xlabel(f'Concentration {system.titrate} (M)')
    ax.set_ylabel('Residual')
    ax.axhline(color='grey', linestyle='--')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True)
    
    # Save the figure
    save_plot(fig, 'residuals', **kwargs)
    plt.show()
    
    return df
    

def landscape(system, *, landscape_parameters = None, **kwargs):
    """
    Landscape post process selection tool. Will call the appropriate landscape
    function based on the number of landscape_parameters.
    If no landscape_parameters are given, the landscape function will try
    to use the fit_parameters instead. 
    If more than two parameters are given only the first two will be plotted.

    Parameters
    ----------
    system : System object
        The system to analyse
    landscape_parameters : List of Strings
        The parameters that should be varied in the landscape. If none are
        given, instead the fit_parameters will be used.
    **kwargs : Optional parameters
        See specific landscape functions for details on the optional
        parameters that can be suplied.

    Raises
    ------
    ValueError
        If len(landscape_parameters) < 1 or
        if no landscape_parameters are given and there are no fit_parameters
        
    Warnings
    --------
    Modifies System.condition.state objects concentration
        
    Returns
    -------
    Matplotlib plot
        Appropriate landscape plot for the number of parameters.
    Pandas dataframe
        Contains the raw values used in the plot

    """
    if landscape_parameters is None:
        landscape_parameters = list(kwargs['fit_parameters'].keys())
        if len(landscape_parameters) == 0:
            raise ValueError('No landscape_parameters and no fit_parameters, '
                             'cannot plot landscape.')
    if len(landscape_parameters) == 1:
        landscape_1d(system, landscape_parameters=landscape_parameters, **kwargs)
    elif len(landscape_parameters) >= 2:
        landscape_2d(system, landscape_parameters=landscape_parameters, **kwargs)
    else:
        raise ValueError("post_process.landscape cannot plot the given "
                         'number of landscape_parameters.')        
    

@write_to_file
def landscape_1d(system, *, landscape_parameters, landscape_1_range = None,
                 **kwargs):
    """
    Plot curve of MSE values based on variation in a single fit parameter.

    Parameters
    ----------
    system : System object
        The system to plot parameter fits for.
    landscape_parameters : List of strings
        Note that a list is expected here. This is the parameter that will be
        plotted. If more than one is given, only the first one is used.
    landscape_1_range : 1darray like, optional
        Range of values to fit for the parameter. Use of np.geomspace is 
        recommended. If none are given the landscape parameter current value
        times 0.01 and 100 are used as min and max value respectively.

    Returns
    -------
    Matplotlib plot
        Line plot of the MSE values for the range of parameter values.
    
    pandas.dataframe
        Dataframe containing the numbers plotted.

    """
    initial_value = system.get_parameter(landscape_parameters[0])
    
    if landscape_1_range is None:
        lower = initial_value*0.01
        upper = initial_value*100
        landscape_1_range = np.geomspace(lower,upper,num=100) 
    
    fig, ax = plt.subplots()
    results = []
    for value in landscape_1_range:
        results.append(
            (system.error_function([value], [landscape_parameters[0]])**2).mean())
    ax.plot(landscape_1_range, results)
    
    # Reset initial value
    system.set_parameter(landscape_parameters[0], initial_value)

    # Modify graph looks 
    ax.set_title(f"Parameter landscape for: {landscape_parameters[0]}")
    ax.set_xlabel('Parameter value')
    ax.set_xscale('log')
    ax.set_ylabel('Mean squared error')
    plt.show()
    
    # Save the figure
    save_plot(fig, 'landscape', **kwargs)
    
    # Return numerical values as pandas dataframe
    df = pd.DataFrame(data = results, index = landscape_1_range, 
                       columns = ['MSE'])
    df.index.name = landscape_parameters[0]
    return df
        

@write_to_file
def landscape_2d(system, *, landscape_parameters, landscape_1_range=None, 
                 landscape_2_range=None, **kwargs):
    """
    Creates a landschap of MSE values based on 2 fit parameters.

    Parameters
    ----------
    system : System object
        The system to plot parameter fits for.
    landscape_parameters : List of strings
        The parameters that will be changed. If more than two are given, the
        others are ignored.
    landscape_1_range : 1darray like, optional
        Range of values to fit for the first parameter. Use of np.geomspace is 
        recommended. If none are given the landscape parameter current value
        times 0.01 and 100 are used as min and max value respectively.
    landscape_2_range : 1darray like, optional
        Range of values to fit for the second parameter. Use of np.geomspace is 
        recommended. If none are given the landscape parameter current value
        times 0.01 and 100 are used as min and max value respectively.
    
    Returns
    -------
    Matplotlib plot
        2D plot showing the MSE values for the range of parameter values as
        contour plot.
    pandas.dataframe
        Dataframe containing the raw numbers plotted.
    
    Raises
    ------
    ValueError
        if len(landscape_parameters) < 2

    """
    print('Plotting 2D landscape... ')
    
    # Save initial parameter values
    initial_value_0 = system.get_parameter(landscape_parameters[0])
    initial_value_1 = system.get_parameter(landscape_parameters[1])
    
    if len(landscape_parameters) < 2:
        raise ValueError('postprocess.landscape_2d requires at least 2 ' 
                         'landscape parameters.')
    if landscape_1_range is None:
        lower = initial_value_0*0.01
        upper = initial_value_0*100
        landscape_1_range = np.geomspace(lower,upper,num=50)
    if landscape_2_range is None:
        lower = initial_value_1*0.01
        upper = initial_value_1*100
        landscape_2_range = np.geomspace(lower,upper,num=50)
   
    # Caluclations
    X, Y = np.meshgrid(landscape_1_range, landscape_2_range)
    Z = np.zeros_like(X)
    n = Z.size

    for i, index in enumerate(np.ndindex(X.shape)):
        if (i + 1) % 50 == 0:
            print(f'{i+1} / {n}')
        parameter_guess = (X[index], Y[index])
        error = (system.error_function(
            parameter_guess, landscape_parameters[:2]) ** 2).mean()
        Z[index] = np.log10(error)
    
    # Reset initial value
    system.set_parameter(landscape_parameters[0], initial_value_0)
    system.set_parameter(landscape_parameters[1], initial_value_1)
    
    # Plotting
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, cmap='viridis')
    ax.set_title('Mean squared error landscape', fontsize=14)
    CB = fig.colorbar(CS, shrink=0.8, format=FuncFormatter(
        lambda x, pos: f'{int(10**x):.4g}'))
    ax.set_xlabel(landscape_parameters[0])
    ax.set_ylabel(landscape_parameters[1])
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.show()
    
    # Save the figure
    save_plot(fig, 'landscape', **kwargs)

    # Return plotted data
    return pd.DataFrame(Z, index=[r[0] for r in Y], columns = X[0])
    
    
def outlier(system, *, write_output = True, skip_warnings = False, **kwargs):
    """
    Uses a doornbos procedure to detect outliers in data associated with
    system.
    Will only detect suspects, removal needs to be performed manually after
    conformation.
    See src.analysis.outliers for details on the method.

    Parameters
    ----------
    system : system object 
        The system to analyse for outliers.
    write_output : Boolean, optional
        Optional flag for directing the output to a file instead of system.out.
        The default is False.
    skip_warnings: Boolean, optional
        Optional flag to not print warnings. The default is false.

    Returns
    -------
    None
        Prints any outliers found to the system.out or to file depending
        on parameters.

    """
    # Set up
    undetermined_warning = False
    
    if write_output:
        with open('output\outliers.txt', 'w') as f:
            f.write('The following values are suspected to be outliers:\n')
            
    # Check for potential outliers
    for condition in system:
        found = {}
        for index, row in condition.data.iterrows():
            try:
                outliers = doornbos_outlier(row.values)
            except UndeterminedError:
                undetermined_warning = True
                outliers = np.array([False])
            if outliers.any() == True:
                found[index] = float(row[outliers].values)
        
        if len(found.keys()) > 0:
            if write_output == False:
                _outlier_print(condition, found)
            else:
                _outlier_to_file(condition, found)
    
    # Finalse the procedure            
    if undetermined_warning and not skip_warnings:
        print('Warning: Some replicates contained only two unique values, '
              'doornbos outlier detection is  undetermined for this case.\n')            
    if write_output:
        print('Outliers found have been written to: "output\outliers.txt"')

        
def _outlier_print(system, found):       
    """
    Private helper function for outlier printing to system.out
    """
    print(f'In system: {system.name} the following values are suspected '
          'to be outliers:')
    print('Concentration\tvalue')
    print('-------------\t-----')
    for key, value in found.items():
        print(f'{key:<8}\t\t{value}')
    print()

def _outlier_to_file(system, found):
    """
    Private helper function for outlier writing to output text.
    """
    with open('output\outliers.txt', 'a') as f:
        f.write(f'System: {system.name}\n')
        f.write('Concentration\tvalue\n')
        f.write('-------------\t-----\n')
        for key, value in found.items():
            f.write(f'{key:<8}\t{value}\n')
        f.write('\n')
  
@write_to_file
def plot_concentrations(system, *, plot_species='all', 
                        concentrations_start=None, concentrations_stop=None,
                        **kwargs):
    """
    Plot the concentrations of species in the system for a single condition.
    The free titrate concentration is never plotted but is added to the
    output file.
    
    It is possible to select which species with the plot_species argument:
    -'all': plots all species except for free titrate. 
    -'components': plot all species marked in the model as 'independent', 
    the components of the system.
    -'complexes': plot all species marked in the model as 'dependent',
    the complexes formed from the components.
    -['R', 'S', ...]: a list of species to plot. Species need to be
    defined in the model and lookup is case-sensitive.

    Parameters
    ----------
    system : System object
        The system to analyse
    plot_species : {'all', 'components', 'complexes'} or list of strings, optional
        Which species to plot, see above for options. The default is 'all'.
    concentrations_start : float, optional
        The lowest titrate concentration to plot. The default is equal to the
        lowest concentration in the system.data.
    concentrations_stop : float, optional
        The highest titrate concentration to plot. The default is equal to the
        highest concentration in the system.data.

    Raises
    ------
    ValueError
        If the system has more than one condition associated.
    
    Warnings
    --------
    Modifies system.state

    Returns
    -------
    matplotlib plot
        line plot showing the concentrations of the selected species as a 
        function of the total titrate concentration present.

    pandas.dataframe
        Dataframe containing the numbers plotted.
        
    """
    if len(system) != 1:
        raise ValueError('plot_concentrations only supported for systems '
                         'containing exactly one condition (e.g. not the '
                         'combined setup type.')

    # If a string is entered, make it lowercase
    try:
        plot_species = plot_species.lower()
    # If a list was entered instead, a attribute error will be trown, we can
    # ignore it.
    except AttributeError:
        pass
    
    # Determine the range to plot
    data_concentrations = system.conditions[0].data.index.to_numpy()
    start = (min(data_concentrations) if concentrations_start is None 
             else concentrations_start)
    stop = (max(data_concentrations) if concentrations_stop is None 
            else concentrations_stop)
    titrate_concentrations = np.geomspace(start, stop, num=100)
    
    guess = None
    specie_concentrations = {}
    
    # Loop over all titrate concentrations, build specie_concentration lib
    for titrate in titrate_concentrations:
        result = system.conditions[0].concentrations_at(titrate, guess=guess)
        for specie, value in sorted(result.independent.items()):
            if (specie in plot_species or plot_species == 'all' or 
                plot_species == 'components'):
                specie_concentrations.setdefault(specie, []).append(value) 
        for specie, value in sorted(result.dependent.items()):
            if (specie in plot_species or plot_species == 'all' or 
                plot_species == 'complexes'):
                specie_concentrations.setdefault(specie, []).append(value) 
        guess = result.solution
    
    # New figure
    fig, ax = plt.subplots()
    
    # Set up the color scheme
    n = len(specie_concentrations)
    ax.set_prop_cycle('color',[plt.cm.tab10(i) for i in np.linspace(0, 1, n)])
    
    # Plot the points
    # Free titrate will reach far higher concentrations than other species,
    # so do not plot it.
    free_titrate = system.titrate.replace('_tot', '')
    for specie, value in specie_concentrations.items():
        if specie == free_titrate:
            continue
        ax.plot(titrate_concentrations, value, marker='', linestyle='--',
                label=specie)
    
    # Modify graph looks
    ax.set_xscale('log')
    ax.set_title("Concentration species vs titrate")
    ax.set_xlabel(f'{system.titrate} (M)')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True)
    fig.canvas.draw()
    ax.yaxis.offsetText.set_visible(False)
    multiplier = ax.yaxis.get_offset_text().get_text()
    unit = _axis_unit_label(multiplier)
    ax.set_ylabel(f'Species (x {unit}M)')
    plt.tight_layout()
    
    # Save the figure
    save_plot(fig, 'plot_concentrations', **kwargs)
    
    plt.show()
    
    # Gather the data for return dataframe
    df = pd.DataFrame.from_dict(specie_concentrations)
    df.index = titrate_concentrations
    return df  

@write_to_file
def confidence_interval(system, *, confidence_method='bootstrap', 
                        confidence_repeats=10, bias_acceleration = True,
                        **kwargs):
    """
    Determines a confidence interval for the parameters based on the
    given approach. Currently only the bootstrap method is supported.
    
    The bootstrap method is based on random draw, so a large number of
    repeats is recommended to get accurate results.

    Parameters
    ----------
    system : System object
        The system to perform the analysis on.
    confidence_method : string, optional
        The method to use to determine the interval.
        The default is 'bootstrap'.
    confidence_repeats : integer, optional
        The number of bootstrap sets to generate. A 1000 samples will
        result in reasonable predictions in most cases. The default is 10
        to give an indication of the total duration required.
    
    Warnings
    --------
    Modifies system.state

    Returns
    -------
    result : Pandas dataframe
        Dataframe containing the determined point estimates for all generated
        samples.

    """
    if confidence_method.lower() == 'bootstrap':
        result = bootstrap(system, confidence_repeats, 
                           bias_acceleration=bias_acceleration)    
    else:
        raise ValueError(f'Non implemented method: {confidence_method}')
    if confidence_repeats < 100:
        print()
        print('NOTE: Confidence_interval was executed with repeats = '
              f'{confidence_repeats}. In order to generate accurate ' 
              'predictions, a large sample of generated datasets should be ' 
              'used by setting the option "confidence_repeats": n.')
    return result

def _squared_error_m_function(system):
    """
    Default M function for the parameter_sensitivity analysis.
    Calculates squared model error with current parameters.
    """
    return sum(system.error_function([],[])**2)

@write_to_file
def parameter_sensitivity(system, *, sensitivity_perturbation = 0.5, 
                          sensitivity_state = 'current', 
                          sensitivity_parameters = None,
                          sensitivity_m_function = _squared_error_m_function,
                          **kwargs):
    """
    Performs local parameter sensitivity analysis on the system.
    
    The parameters that are tested should be system constants. This means that
    the parameter has the same value across all associated conditions.
    
    This method is based on the description in van Riel, BRIEFINGS IN 
    BIOINFORMATICS Vol 7 (2006).
    The M(y) value is the model output value to track upon change in parameter
    value y. By default M is defined as the squared error of the model
    compared to the measurement data.
    
    Parameters
    ----------
    system : System object
        The system to analyse
    sensitivity_perturbation : float, optional
        The change in parameter value as a fraction increase. Negative values
        will result in a decrease. The default is 0.5, a 50% increase.
    sensitivity_state : {'solution', 'current'}, optional
        Whether to use the current parameter values or the values determined
        during system.solve. The default is 'solution', the solution values.
    sensitivity_parameters : list of strings
        List of parameters to test for sensitivity. By default the
        fit_parameters are used as sensitivity_parameters
    sensitivity_m_function : python function, optional
        The function to use to determine the M value, see above. By default
        the system.error_function is used. The function should take only a
        single argument 'system'.

    Warnings
    --------
    Modifies system.state
    
    Raises
    ------
    ValueError
        If any of the sensitivity_parameters is not a system constant, see 
        above.

    Returns
    -------
    Matplot plot
        Barplot showing the sensitivities of the different parameters.
    pandas Dataframe
        The absolute values used to plot the data.

    """
    state = sensitivity_state.lower()
    if state == 'solution':
        if system.solution is None:
            raise ValueError('Sensitivity performed with solution state, but '
                             'no solution determined for system.')
        system.set_solution_state()
    elif state == 'current':
        pass
    else:
        raise ValueError('Sensitivity analysis sensitivity_state parameter '
                         'needs to be either "solution" or "current".')
    if sensitivity_parameters is None:
        sensitivity_parameters = kwargs['fit_parameters'].keys()
    if len(sensitivity_parameters) == 0:
        raise ValueError('Sensitivity analysis requires either explicit '
                         '"sensitivity_parameters" or atleast one '
                         'fit parameter.')
        
    initial_m = sensitivity_m_function(system)
    
    results = {}
    data = []
    for par in sensitivity_parameters:
        # Check pre condition
        current_par_values = [condition.state.get_value(par) 
                              for condition in system.conditions]
        if not all(x == current_par_values[0] for x in current_par_values):
            raise ValueError(f'parameter_sensitivity pre violated: {par} '
                             'is not equal for all conditions.')    
        # pre condition ok, continue
    
        par_value = current_par_values[0]
        new_value = par_value*(1 + sensitivity_perturbation)
        system.set_parameter(par, new_value)
        new_m = sensitivity_m_function(system)
        result = ((new_m - initial_m) / initial_m) / (
            (new_value - par_value) / par_value)
        results[par] = result
        
        data.append([par_value, new_value, initial_m, new_m, result])
        
        # Important: return parameter to original value, hard to track bug
        system.set_parameter(par, par_value)
    
    # plot the results
    fig, ax = plt.subplots()
    n = len(sensitivity_parameters)
    ind = np.arange(n)
    bar_heights = results.values()
    bar_labels = results.keys()
    ax.bar(ind, bar_heights)
    
    # Change graph looks
    if all(value < 1 for value in bar_heights):
        ax.set_ylim(top=1.1)
    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_xticks(ind)
    ax.set_xticklabels(bar_labels)
    ax.set_title("Local parameter sensitivity analysis")
    ax.set_ylabel(r'$S^m_\sigma$')
    
    # Save the figure
    save_plot(fig, 'parameter_sensitivity', **kwargs)
    plt.show()
    
    # Prepare return df
    df = pd.DataFrame(data, index=sensitivity_parameters, columns = [
        'Originial parameter value', 'New parameter value', 
        'Originial M value', 'New M value', 'Sensitivity parameter'])
    return df      

@write_to_file
def range_solver(system, *, range_fit_parameters=None, range_n = 10, 
                 log_scale=True, **kwargs):
    """
    Solve the system from a range of initial guess values, using a latin 
    hypercube approach to determine combinations. Displays all
    determined values sorted by the squared error.
    
    All parameters not included in range_fit_parameters are assumed to be
    fixed at their current system values.

    Parameters
    ----------
    system : System object
        The system to analyse
    range_fit_parameters : Dictionary of string:tuple pairs
        Each key represents a fit_parameter, the tuple should contain the
        min and max expected values of that parameter.
    range_n : int
        The number of strata to create within each range. The default is 10.
    log_scale : Boolean
        Whether to use a log based scale instead of a linear scale to create
        the strata. The default is True.

    Warnings
    --------
    Modifies system parameters for the keys in range_fit_parameters
    Modifies system.solution

    Returns
    -------
    result : dataframe
        All the determined parameter values with associated squared error.

    """
    import src.analysis.guess_range_solving as grs
    result = grs.range_solver(system,
                     range_fit_parameters = range_fit_parameters, 
                     range_n = range_n, log_scale=log_scale)
    return result
   