"""
Model file created on 2021-08-20 13:47:44.065600 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; Kd
A + C = AC; Kd
A + D = AD; Kd
B + C = BC; Kd
B + D = BD; Kd
C + D = CD; Kd
AB + C = ABC; Kd
AB + D = ABD; Kd
AC + D = ACD; Kd
BC + D = BCD; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['ABC', 'A', 'AD', 'ACD', 'BCD', 'B', 'CD', 'ABD', 'AB', 'AC', 'D', 'BC', 'Kd', 'C', 'BD', 'A_tot', 'B_tot', 'D_tot', 'C_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['A', 'B', 'D', 'C']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABC', 'ABD', 'ACD', 'BCD']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ABC', 'A', 'AD', 'ACD', 'ABD', 'AB', 'AC'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    A = concentrations[0]
    B = concentrations[1]
    D = concentrations[2]
    C = concentrations[3]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    C_tot = state.C_tot
    D_tot = state.D_tot
    Kd = state.Kd

    result = np.zeros(4)
    result[0] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B/Kd + A*C*D/Kd**2 + A*C/Kd + A*D/Kd + A - A_tot) / A_tot
    result[1] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B/Kd + B*C*D/Kd**2 + B*C/Kd + B*D/Kd + B - B_tot) / B_tot
    result[2] = (A*B*D/Kd**2 + A*C*D/Kd**2 + A*D/Kd + B*C*D/Kd**2 + B*D/Kd + C*D/Kd + D - D_tot) / D_tot
    result[3] = (A*B*C/Kd**2 + A*C*D/Kd**2 + A*C/Kd + B*C*D/Kd**2 + B*C/Kd + C*D/Kd + C - C_tot) / C_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.A = solution[0]
    state.B = solution[1]
    state.D = solution[2]
    state.C = solution[3]

    # Readability 
    A = state.A
    B = state.B
    C = state.C
    D = state.D
    Kd = state.Kd

    # Dependent variables
    state.AB = A*B/Kd
    state.AC = A*C/Kd
    state.AD = A*D/Kd
    state.BC = B*C/Kd
    state.BD = B*D/Kd
    state.CD = C*D/Kd
    state.ABC = A*B*C/Kd**2
    state.ABD = A*B*D/Kd**2
    state.ACD = A*C*D/Kd**2
    state.BCD = B*C*D/Kd**2


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    A = state.A
    AB = state.AB
    ABC = state.ABC
    ABD = state.ABD
    AC = state.AC
    ACD = state.ACD
    AD = state.AD
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABD + AC + ACD + AD)/A_tot


