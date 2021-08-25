"""
Model file created on 2021-08-20 13:50:41.659502 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; Kd
A + C = AC; Kd
A + D = AD; Kd
A + E = AE; Kd
B + C = BC; Kd
B + D = BD; Kd
B + E = BE; Kd
C + D = CD; Kd
C + E = CE; Kd
D + E = DE; Kd
AB + C = ABC; Kd
AB + D = ABD; Kd
AB + E = ABE; Kd
AC + D = ACD; Kd
AC + E = ACE; Kd
AD + E = ADE; Kd
BC + D = BCD; Kd
BC + E = BCE; Kd
BD + E = BDE; Kd
CD + E = CDE; Kd
ABC + D = ABCD; Kd
ABC + E = ABCE; Kd
ABD + E = ABDE; Kd
ACD + E = ACDE; Kd
BCD + E = BCDE; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['ABC', 'AE', 'AD', 'BCE', 'B', 'ACE', 'AB', 'AC', 'ABE', 'ADE', 'ABDE', 'BCDE', 'BC', 'BCD', 'CE', 'BDE', 'A', 'ACD', 'CD', 'DE', 'ABCE', 'E', 'ABD', 'CDE', 'ACDE', 'D', 'BE', 'ABCD', 'Kd', 'C', 'BD', 'A_tot', 'B_tot', 'E_tot', 'D_tot', 'C_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['A', 'B', 'E', 'D', 'C']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE', 'ABC', 'ABD', 'ABE', 'ACD', 'ACE', 'ADE', 'BCD', 'BCE', 'BDE', 'CDE', 'ABCD', 'ABCE', 'ABDE', 'ACDE', 'BCDE']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ABC', 'AE', 'AD', 'ACE', 'AB', 'AC', 'ABE', 'ADE', 'ABDE', 'A', 'ACD', 'ABCE', 'ABD', 'ACDE', 'ABCD'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    A = concentrations[0]
    B = concentrations[1]
    E = concentrations[2]
    D = concentrations[3]
    C = concentrations[4]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    C_tot = state.C_tot
    D_tot = state.D_tot
    E_tot = state.E_tot
    Kd = state.Kd

    result = np.zeros(5)
    result[0] = (A*B*C*D/Kd**3 + A*B*C*E/Kd**3 + A*B*C/Kd**2 + A*B*D*E/Kd**3 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B/Kd + A*C*D*E/Kd**3 + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C/Kd + A*D*E/Kd**2 + A*D/Kd + A*E/Kd + A - A_tot) / A_tot
    result[1] = (A*B*C*D/Kd**3 + A*B*C*E/Kd**3 + A*B*C/Kd**2 + A*B*D*E/Kd**3 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B/Kd + B*C*D*E/Kd**3 + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C/Kd + B*D*E/Kd**2 + B*D/Kd + B*E/Kd + B - B_tot) / B_tot
    result[2] = (A*B*C*E/Kd**3 + A*B*D*E/Kd**3 + A*B*E/Kd**2 + A*C*D*E/Kd**3 + A*C*E/Kd**2 + A*D*E/Kd**2 + A*E/Kd + B*C*D*E/Kd**3 + B*C*E/Kd**2 + B*D*E/Kd**2 + B*E/Kd + C*D*E/Kd**2 + C*E/Kd + D*E/Kd + E - E_tot) / E_tot
    result[3] = (A*B*C*D/Kd**3 + A*B*D*E/Kd**3 + A*B*D/Kd**2 + A*C*D*E/Kd**3 + A*C*D/Kd**2 + A*D*E/Kd**2 + A*D/Kd + B*C*D*E/Kd**3 + B*C*D/Kd**2 + B*D*E/Kd**2 + B*D/Kd + C*D*E/Kd**2 + C*D/Kd + D*E/Kd + D - D_tot) / D_tot
    result[4] = (A*B*C*D/Kd**3 + A*B*C*E/Kd**3 + A*B*C/Kd**2 + A*C*D*E/Kd**3 + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C/Kd + B*C*D*E/Kd**3 + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C/Kd + C*D*E/Kd**2 + C*D/Kd + C*E/Kd + C - C_tot) / C_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.A = solution[0]
    state.B = solution[1]
    state.E = solution[2]
    state.D = solution[3]
    state.C = solution[4]

    # Readability 
    A = state.A
    B = state.B
    C = state.C
    D = state.D
    E = state.E
    Kd = state.Kd

    # Dependent variables
    state.AB = A*B/Kd
    state.AC = A*C/Kd
    state.AD = A*D/Kd
    state.AE = A*E/Kd
    state.BC = B*C/Kd
    state.BD = B*D/Kd
    state.BE = B*E/Kd
    state.CD = C*D/Kd
    state.CE = C*E/Kd
    state.DE = D*E/Kd
    state.ABC = A*B*C/Kd**2
    state.ABD = A*B*D/Kd**2
    state.ABE = A*B*E/Kd**2
    state.ACD = A*C*D/Kd**2
    state.ACE = A*C*E/Kd**2
    state.ADE = A*D*E/Kd**2
    state.BCD = B*C*D/Kd**2
    state.BCE = B*C*E/Kd**2
    state.BDE = B*D*E/Kd**2
    state.CDE = C*D*E/Kd**2
    state.ABCD = A*B*C*D/Kd**3
    state.ABCE = A*B*C*E/Kd**3
    state.ABDE = A*B*D*E/Kd**3
    state.ACDE = A*C*D*E/Kd**3
    state.BCDE = B*C*D*E/Kd**3


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    A = state.A
    AB = state.AB
    ABC = state.ABC
    ABCD = state.ABCD
    ABCE = state.ABCE
    ABD = state.ABD
    ABDE = state.ABDE
    ABE = state.ABE
    AC = state.AC
    ACD = state.ACD
    ACDE = state.ACDE
    ACE = state.ACE
    AD = state.AD
    ADE = state.ADE
    AE = state.AE
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABCD + ABCE + ABD + ABDE + ABE + AC + ACD + ACDE + ACE + AD + ADE + AE)/A_tot


