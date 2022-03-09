"""
Model file created on 2022-03-09 12:35:28.115509 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
R + P = PR; Kd1
PR + S = PRS; Kd2 / Alpha
R + S = RS; Kd2
RS + P = PRS; Kd1/ Alpha

Labeled specie: P
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['R', 'S', 'Alpha', 'Kd2', 'P', 'RS', 'Kd1', 'PRS', 'PR', 'R_tot', 'S_tot', 'P_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['R', 'S', 'P']
# Species who's concentration can be determined from others
dependent_species = ['PR', 'PRS', 'RS']
# The constant terms in the model
constants = ['Kd1', 'Alpha', 'Kd2']
# Which components are labeled / detected in the experiment
labeled_components = ['P', 'PRS', 'PR'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    R = concentrations[0]
    S = concentrations[1]
    P = concentrations[2]

    # Readability
    Alpha = state.Alpha
    Kd1 = state.Kd1
    Kd2 = state.Kd2
    P_tot = state.P_tot
    R_tot = state.R_tot
    S_tot = state.S_tot

    result = np.zeros(3)
    result[0] = (Alpha*P*R*S/(Kd1*Kd2) + R - R_tot + R*S/Kd2 + P*R/Kd1) / R_tot
    result[1] = (Alpha*P*R*S/(Kd1*Kd2) + S - S_tot + R*S/Kd2) / S_tot
    result[2] = (Alpha*P*R*S/(Kd1*Kd2) + P - P_tot + P*R/Kd1) / P_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.R = solution[0]
    state.S = solution[1]
    state.P = solution[2]

    # Readability 
    Alpha = state.Alpha
    Kd1 = state.Kd1
    Kd2 = state.Kd2
    P = state.P
    R = state.R
    S = state.S

    # Dependent variables
    state.PR = P*R/Kd1
    state.PRS = Alpha*P*R*S/(Kd1*Kd2)
    state.RS = R*S/Kd2


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    P = state.P
    PR = state.PR
    PRS = state.PRS
    P_tot = state.P_tot
    data_max = state.data_max
    data_min = state.data_min

    return P*data_min/P_tot + data_max*(PR + PRS)/P_tot


