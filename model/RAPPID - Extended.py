"""
Model file created on 2021-08-19 11:14:06.042437 
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

TB + A = Tba; KdN
TA + B = Tab; KdN
TAT + B = Tatbi; 1/4*KdB
TBT + A = Tbtai; 1/4*KdA
Tatbi = Tatbs; KdN / EM
Tbtai = Tbtas; KdN / EM
ABTa + T = Tatbs; KdA
ABTa + T = Tbtas; KdB

Labeled specie: 
data_mode: custom
custom input: (ABTa + Tatbs + Tbtas) * Scaling
"""

import numpy as np

# All variables for this model
variables = ['AB', 'A', 'BTT', 'EM', 'KdN', 'Tab', 'ABTa', 'Tbtai', 'T', 'BT', 'Scaling', 'Tatbs', 'AT', 'Tbtas', 'B', 'ABTi', 'Tba', 'Tatbi', 'KdB', 'KdA', 'ATT', 'A_tot', 'T_tot', 'B_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['A', 'T', 'B']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AT', 'BT', 'BTT', 'ABTi', 'ATT', 'ABTa', 'Tba', 'Tab', 'Tatbi', 'Tbtai', 'Tatbs', 'Tbtas']
# The constant terms in the model
constants = ['Scaling', 'EM', 'KdB', 'KdA', 'KdN']
# Which components are labeled / detected in the experiment
labeled_components = ['AB', 'A', 'BTT', 'Tab', 'ABTa', 'Tbtai', 'T', 'BT', 'Tatbs', 'AT', 'Tbtas', 'B', 'ABTi', 'Tba', 'Tatbi', 'ATT'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    A = concentrations[0]
    T = concentrations[1]
    B = concentrations[2]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    EM = state.EM
    KdA = state.KdA
    KdB = state.KdB
    KdN = state.KdN
    T_tot = state.T_tot

    result = np.zeros(3)
    result[0] = (4*A*B*EM*T/(KdA*KdB*KdN) + 4*A*B*EM*T**2/(KdA*KdB**2*KdN) + 4*A*B*EM*T**2/(KdA**2*KdB*KdN) + A*B/KdN + 2*A*B*T/(KdB*KdN) + 2*A*B*T/(KdA*KdN) + 4*A*B*T/(KdA*KdB) + 4*A*B*T**2/(KdA*KdB**2) + 4*A*B*T**2/(KdA**2*KdB) + A + 2*A*T/KdA + A*T**2/KdA**2 - A_tot) / A_tot
    result[1] = (4*A*B*EM*T/(KdA*KdB*KdN) + 8*A*B*EM*T**2/(KdA*KdB**2*KdN) + 8*A*B*EM*T**2/(KdA**2*KdB*KdN) + 2*A*B*T/(KdB*KdN) + 2*A*B*T/(KdA*KdN) + 4*A*B*T/(KdA*KdB) + 8*A*B*T**2/(KdA*KdB**2) + 8*A*B*T**2/(KdA**2*KdB) + 2*A*T/KdA + 2*A*T**2/KdA**2 + 2*B*T/KdB + 2*B*T**2/KdB**2 + T - T_tot) / T_tot
    result[2] = (4*A*B*EM*T/(KdA*KdB*KdN) + 4*A*B*EM*T**2/(KdA*KdB**2*KdN) + 4*A*B*EM*T**2/(KdA**2*KdB*KdN) + A*B/KdN + 2*A*B*T/(KdB*KdN) + 2*A*B*T/(KdA*KdN) + 4*A*B*T/(KdA*KdB) + 4*A*B*T**2/(KdA*KdB**2) + 4*A*B*T**2/(KdA**2*KdB) + B + 2*B*T/KdB + B*T**2/KdB**2 - B_tot) / B_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.A = solution[0]
    state.T = solution[1]
    state.B = solution[2]

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
    state.Tba = 2*A*B*T/(KdB*KdN)
    state.Tab = 2*A*B*T/(KdA*KdN)
    state.Tatbi = 4*A*B*T**2/(KdA**2*KdB)
    state.Tbtai = 4*A*B*T**2/(KdA*KdB**2)
    state.Tatbs = 4*A*B*EM*T**2/(KdA**2*KdB*KdN)
    state.Tbtas = 4*A*B*EM*T**2/(KdA*KdB**2*KdN)


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    Scaling = state.Scaling
    Tatbs = state.Tatbs
    ABTa = state.ABTa
    Tbtas = state.Tbtas

    return Scaling*(ABTa + Tatbs + Tbtas)