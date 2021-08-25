"""
Model file created on 2021-06-10 10:46:22.482468 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
R + P = RP; KD1
PR + S = RPS; KD2 / Alpha
R + S = RS; KD2
RS + P = RSP; KD1/ Alpha  

Labeled component: P
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['PRS', 'RS', 'S', 'R', 'P', 'PR', 'KD2', 'Alpha', 'KD1', 'S_tot', 'R_tot', 'P_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['S', 'R', 'P']
# Species who's concentration can be determined from others
dependent_species = ['PR', 'PRS', 'RS']
# The constant terms in the model
constants = ['KD2', 'Alpha', 'KD1']
# Which components are labeled / detected in the experiment
labeled_components = ['PRS', 'P', 'PR'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    S = concentrations[0]
    R = concentrations[1]
    P = concentrations[2]

    # Readability
    Alpha = state.Alpha
    KD1 = state.KD1
    KD2 = state.KD2
    P_tot = state.P_tot
    R_tot = state.R_tot
    S_tot = state.S_tot

    result = np.zeros(3)
    result[0] = (Alpha*P*R*S/(KD1*KD2) + S - S_tot + R*S/KD2)
    result[1] = (Alpha*P*R*S/(KD1*KD2) + R - R_tot + R*S/KD2 + P*R/KD1) 
    result[2] = (Alpha*P*R*S/(KD1*KD2) + P - P_tot + P*R/KD1)
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.S = solution[0]
    state.R = solution[1]
    state.P = solution[2]

    # Readability 
    Alpha = state.Alpha
    KD1 = state.KD1
    KD2 = state.KD2
    P = state.P
    R = state.R
    S = state.S

    # Dependent variables
    state.PR = P*R/KD1
    state.PRS = Alpha*P*R*S/(KD1*KD2)
    state.RS = R*S/KD2


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


