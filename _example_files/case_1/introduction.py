"""
Model file created on 2022-03-09 12:29:21.026082 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
R + P = PR; Kd

Labeled specie: P
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['R', 'P', 'PR', 'Kd', 'R_tot', 'P_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['R', 'P']
# Species who's concentration can be determined from others
dependent_species = ['PR']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['P', 'PR'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    R = concentrations[0]
    P = concentrations[1]

    # Readability
    Kd = state.Kd
    P_tot = state.P_tot
    R_tot = state.R_tot

    result = np.zeros(2)
    result[0] = (R - R_tot + P*R/Kd) / R_tot
    result[1] = (P - P_tot + P*R/Kd) / P_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.R = solution[0]
    state.P = solution[1]

    # Readability 
    Kd = state.Kd
    P = state.P
    R = state.R

    # Dependent variables
    state.PR = P*R/Kd


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    P = state.P
    PR = state.PR
    P_tot = state.P_tot
    data_max = state.data_max
    data_min = state.data_min

    return P*data_min/P_tot + PR*data_max/P_tot


