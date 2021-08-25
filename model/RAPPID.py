"""
Model file created on 2021-06-10 11:45:36.858241 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; KdN
A + T = TA; 1/2*KdA
B + T = TB; 1/2*KdB
TB + T = TTB; 2*KdB
TB + A = ABTi; 1/2*KdA
TA + T = TTA; 2*KdA
TA + B = ABTi; 1/2*KdB
ABTi = ABTa; KdN / EM 

Labeled component: AB
data_mode: custom
"""

import numpy as np

# All variables for this model
variables = ['ABTi', 'ATT', 'BT', 'AB', 'T', 'ABTa', 'BTT', 'B', 'A', 'AT', 'KdA', 'KdB', 'EM', 'KdN', 'T_tot', 'B_tot', 'A_tot', 'Scaling']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['T', 'B', 'A']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AT', 'BT', 'BTT', 'ABTi', 'ATT', 'ABTa']
# The constant terms in the model
constants = ['KdA', 'KdB', 'EM', 'KdN', 'Scaling']
# Which components are labeled / detected in the experiment
labeled_components = ['ABTi', 'AB', 'ABTa'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    T = concentrations[0]
    B = concentrations[1]
    A = concentrations[2]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    EM = state.EM
    KdA = state.KdA
    KdB = state.KdB
    KdN = state.KdN
    T_tot = state.T_tot

    result = np.zeros(3)
    result[0] = (4*A*B*EM*T/(KdA*KdB*KdN) + 4*A*B*T/(KdA*KdB) + 2*A*T/KdA + 2*A*T**2/KdA**2 + 2*B*T/KdB + 2*B*T**2/KdB**2 + T - T_tot) / T_tot
    result[1] = (4*A*B*EM*T/(KdA*KdB*KdN) + A*B/KdN + 4*A*B*T/(KdA*KdB) + B + 2*B*T/KdB + B*T**2/KdB**2 - B_tot) / B_tot
    result[2] = (4*A*B*EM*T/(KdA*KdB*KdN) + A*B/KdN + 4*A*B*T/(KdA*KdB) + A + 2*A*T/KdA + A*T**2/KdA**2 - A_tot) / A_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.T = solution[0]
    state.B = solution[1]
    state.A = solution[2]

    # Readability 
    A = state.A
    B = state.B
    EM = state.EM
    KdA = state.KdA
    KdB = state.KdB
    KdN = state.KdN
    T = state.T

    # Dependent variables
    state.AB = A*B/KdN
    state.AT = 2*A*T/KdA
    state.BT = 2*B*T/KdB
    state.BTT = B*T**2/KdB**2
    state.ABTi = 4*A*B*T/(KdA*KdB)
    state.ATT = A*T**2/KdA**2
    state.ABTa = 4*A*B*EM*T/(KdA*KdB*KdN)


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    ABTa = state.ABTa
    Scaling = state.Scaling
    
    return ABTa * Scaling
