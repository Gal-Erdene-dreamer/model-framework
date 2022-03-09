"""
Model file created on 2022-03-09 15:50:04.987375 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; KdN
A + T = AT; 1/2*KdA
B + T = BT; 1/2*KdB
TB + T = BTT; 2*KdB
TB + A = ABTi; 1/2*KdA
TA + T = ATT; 2*KdA
TA + B = ABTi; 1/2*KdB
ABTi = ABTa; KdN / EM

Labeled specie: 
data_mode: custom
custom input: ABTa * Scaling
"""

import numpy as np

# All variables for this model
variables = ['BTT', 'B', 'ABTa', 'AT', 'ATT', 'KdA', 'Scaling', 'KdN', 'EM', 'KdB', 'T', 'AB', 'ABTi', 'BT', 'A', 'B_tot', 'T_tot', 'A_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['B', 'T', 'A']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AT', 'BT', 'BTT', 'ABTi', 'ATT', 'ABTa']
# The constant terms in the model
constants = ['Scaling', 'KdA', 'KdN', 'EM', 'KdB']
# Which components are labeled / detected in the experiment
labeled_components = ['BTT', 'B', 'ABTa', 'AT', 'ATT', 'T', 'AB', 'ABTi', 'BT', 'A'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    B = concentrations[0]
    T = concentrations[1]
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
    result[0] = (4*A*B*EM*T/(KdA*KdB*KdN) + A*B/KdN + 4*A*B*T/(KdA*KdB) + B + 2*B*T/KdB + B*T**2/KdB**2 - B_tot) / B_tot
    result[1] = (4*A*B*EM*T/(KdA*KdB*KdN) + 4*A*B*T/(KdA*KdB) + 2*A*T/KdA + 2*A*T**2/KdA**2 + 2*B*T/KdB + 2*B*T**2/KdB**2 + T - T_tot) / T_tot
    result[2] = (4*A*B*EM*T/(KdA*KdB*KdN) + A*B/KdN + 4*A*B*T/(KdA*KdB) + A + 2*A*T/KdA + A*T**2/KdA**2 - A_tot) / A_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.B = solution[0]
    state.T = solution[1]
    state.A = solution[2]

    # Readability 
    A = state.A
    B = state.B
    EM = state.EM
    KdA = state.KdA
    KdB = state.KdB
    KdN = state.KdN
    Scaling = state.Scaling
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

    return ABTa*Scaling