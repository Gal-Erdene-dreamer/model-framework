# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:31:22 2021

@author: N.H.J. Geertjens

Note: In order to prevent user error when entering setup type, e.g. "Combined"
instead of "combined", the name will be made lowercase before searching it
in this file. Because of this, please make sure any setup function in this
file consists of only lowercase words seperated by '_' for readability if 
required. 
In line with the PEP8 naming convention for functions.

The driver script will pass all named arguments to these functions in order
to facilitate future expansions/ changes (e.g. new condition type objects), as
such, a "**kwargs" argument is required.
"""
import numpy as np
import pandas as pd

from src.core.basic_system import System, Condition
from src.core.analysis_system import AnalysisSystem
from src.data_handle import process_csv, process_excel

INPUT_PROCESSOR = process_excel

def combined(model, titrate, known_parameters, input_folder,
             min_concentration = 0, max_concentration = np.inf, **kwargs):
    """
    Process the input data as multiple conditions for a single chemical
    system for which (a) common parameter(s) should be determined.
    e.g. data from a 2d titration.

    Parameters
    ----------
    model : Python module reference
        The model to associate with the system. See System documentation for
        additional details.
    titrate : String
        The parameter which was titrated in the data. See system documentation
        for additional details.
    known_parameters : dictionary of string: float
        Contains parameter: value pairs which will be added to all new
        conditions added to the system.
    input_folder : pathlike
        The folder containing the input csv files and config.ini
    max_concentration : float, optional
        Exclude all titrate values above the given value during fitting.
        The default is infinity (no exclusion).
    min_concentration : float, optional
        Exclude all titrate values below the given value during fitting.
        The default is 0 (no exclusion).

    Returns
    -------
    systems
        List of system objects created. With this setup type, always a single
        system.

    """
    data = INPUT_PROCESSOR(input_folder)
    config = input_folder + 'config.ini'
    system = System(name = 'Combined system', model = model, 
                    titrate = titrate, known_parameters = known_parameters)
    for name, experiment in data.items():
        system.add_condition(condition = Condition, name = name,
             data = experiment, config_location=config)
        
    system.solve_setup(max_concentration = max_concentration, 
                       min_concentration = min_concentration)
    try:
        system.conditions = sorted(system.conditions, 
                       key = lambda cond: int(cond.name.split('_')[-1]))
    except ValueError:
        print('Combined system "conditions" could not be sorted (for plotting'
              '). If this is desired, make sure the names of input data '
              'end in "_x", where x is an integer. Continuing..')
    return [system]


def separate(model, titrate, known_parameters, input_folder,
             min_concentration = 0, max_concentration = np.inf, **kwargs):
    """
    Process the input data as separate systems, each with the same model, 
    but with unique parameter values. Perform the same analysis on all
    systems.

    Parameters
    ----------
    model : Python module reference
        The model to associate with the system. See System documentation for
        additional details.
    titrate : String
        The parameter which was titrated in the data. See system documentation
        for additional details.
    known_parameters : dictionary of string: float
        Contains parameter: value pairs which will be added to all new
        conditions added to the system.
    input_folder : pathlike
        The folder containing the input csv files and config.ini
    max_concentration : float, optional
        Exclude all titrate values above the given value during fitting.
        The default is infinity (no exclusion).
    min_concentration : float, optional
        Exclude all titrate values below the given value during fitting.
        The default is 0 (no exclusion).
        
    Returns
    -------
    systems
        List of system objects created. With this setup type, the number of
        systems is equal to the number of input files.

    """
    data = INPUT_PROCESSOR(input_folder)
    config = input_folder + 'config.ini'
    systems = []
    for name, experiment in data.items():
        system = System(name = name, model = model, titrate = titrate,
                        known_parameters = known_parameters)
        system.add_condition(condition = Condition, name = name,
             data = experiment, config_location=config)
        system.solve_setup(max_concentration = max_concentration, 
                           min_concentration = min_concentration)
        systems.append(system)
    return systems
    
def analysis(model, titrate, known_parameters, input_folder, fit_parameters,
             min_concentration = None, max_concentration = None, **kwargs):
    """
    Setup a system object without attached data. Intended to analyse the
    custom model.

    Parameters
    ----------
    model : Python module reference
        The model to associate with the system. See System documentation for
        additional details.
    titrate : String
        The parameter which was titrated in the data. See system documentation
        for additional details.
    known_parameters : dictionary of string: float
        Contains parameter: value pairs which will be added to all new
        conditions added to the system. Should contain a value for each
        parameter in the model for the analysis type system.
    input_folder : pathlike
        The folder containing the config.ini
    max_concentration : float, optional
        The max concentration in the 'data' of the system. Many analyses
        determine the default plotting range using the concentration values 
        in the data.
    min_concentration : float, optional
        The min concentration in the 'data' of the system. Many analyses
        determine the default plotting range using the concentration values 
        in the data.

    Raises
    ------
    ValueError
        If fit_parameters != {}. Fitting is not available for analysis type
        systems.
        If either min_concentration or max_concentration is None.

    Returns
    -------
    systems
        List of system objects created. With this setup type, this will
        always be a single system.
    """
    
    if fit_parameters != {}:
        raise ValueError('Fitting is not available for analysis type setup. '
                         'fit parameters should be: "{}"')
    if min_concentration is None or max_concentration is None:
        raise ValueError('As there is no data for the analysis system, '
                         'please set the default plotting limits for this '
                         'system using the additional arguments: '
                         '"min_concentration": value and "max_concentration": value')
    config = input_folder + 'config.ini'
    system = AnalysisSystem(name = 'Analysis system', model = model,
                    titrate = titrate, known_parameters = known_parameters)
    df = pd.DataFrame({'measurement':[np.nan, np.nan]})
    df.index = [min_concentration, max_concentration]
    system.add_condition(condition = Condition, name = 'Analysis system',
                                 data = df, config_location=config)
    return [system]
    