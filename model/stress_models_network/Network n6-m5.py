"""
Model file created on 2021-08-20 13:53:39.527431 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; Kd
A + C = AC; Kd
A + D = AD; Kd
A + E = AE; Kd
A + F = AF; Kd
B + C = BC; Kd
B + D = BD; Kd
B + E = BE; Kd
B + F = BF; Kd
C + D = CD; Kd
C + E = CE; Kd
C + F = CF; Kd
D + E = DE; Kd
D + F = DF; Kd
E + F = EF; Kd
AB + C = ABC; Kd
AB + D = ABD; Kd
AB + E = ABE; Kd
AB + F = ABF; Kd
AC + D = ACD; Kd
AC + E = ACE; Kd
AC + F = ACF; Kd
AD + E = ADE; Kd
AD + F = ADF; Kd
AE + F = AEF; Kd
BC + D = BCD; Kd
BC + E = BCE; Kd
BC + F = BCF; Kd
BD + E = BDE; Kd
BD + F = BDF; Kd
BE + F = BEF; Kd
CD + E = CDE; Kd
CD + F = CDF; Kd
CE + F = CEF; Kd
DE + F = DEF; Kd
ABC + D = ABCD; Kd
ABC + E = ABCE; Kd
ABC + F = ABCF; Kd
ABD + E = ABDE; Kd
ABD + F = ABDF; Kd
ABE + F = ABEF; Kd
ACD + E = ACDE; Kd
ACD + F = ACDF; Kd
ACE + F = ACEF; Kd
ADE + F = ADEF; Kd
BCD + E = BCDE; Kd
BCD + F = BCDF; Kd
BCE + F = BCEF; Kd
BDE + F = BDEF; Kd
CDE + F = CDEF; Kd
ABCD + E = ABCDE; Kd
ABCD + F = ABCDF; Kd
ABCE + F = ABCEF; Kd
ABDE + F = ABDEF; Kd
ACDE + F = ACDEF; Kd
BCDE + F = BCDEF; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['ABC', 'ABCDF', 'AD', 'BF', 'ABCEF', 'B', 'BEF', 'AB', 'AC', 'ADE', 'CDF', 'ABDE', 'ADF', 'BC', 'BCDE', 'ABCF', 'ABF', 'ADEF', 'F', 'CDEF', 'ABDEF', 'ACEF', 'CD', 'ABCE', 'ACDE', 'BCDEF', 'ABD', 'BE', 'ABCD', 'BCF', 'Kd', 'ACDF', 'BDF', 'AE', 'BCE', 'ACE', 'ABE', 'ABCDE', 'BCEF', 'EF', 'BDEF', 'ACF', 'CF', 'BCD', 'AF', 'ABEF', 'BCDF', 'CE', 'BDE', 'A', 'ACD', 'DEF', 'DE', 'ACDEF', 'E', 'ABDF', 'CDE', 'AEF', 'D', 'CEF', 'DF', 'C', 'BD', 'C_tot', 'A_tot', 'B_tot', 'E_tot', 'D_tot', 'F_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['C', 'A', 'B', 'E', 'D', 'F']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'BC', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF', 'DE', 'DF', 'EF', 'ABC', 'ABD', 'ABE', 'ABF', 'ACD', 'ACE', 'ACF', 'ADE', 'ADF', 'AEF', 'BCD', 'BCE', 'BCF', 'BDE', 'BDF', 'BEF', 'CDE', 'CDF', 'CEF', 'DEF', 'ABCD', 'ABCE', 'ABCF', 'ABDE', 'ABDF', 'ABEF', 'ACDE', 'ACDF', 'ACEF', 'ADEF', 'BCDE', 'BCDF', 'BCEF', 'BDEF', 'CDEF', 'ABCDE', 'ABCDF', 'ABCEF', 'ABDEF', 'ACDEF', 'BCDEF']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ABC', 'ABCDF', 'AD', 'ABCEF', 'AB', 'AC', 'ADE', 'ABDE', 'ADF', 'ABCF', 'ABF', 'ADEF', 'ABDEF', 'ACEF', 'ABCE', 'ACDE', 'ABD', 'ABCD', 'ACDF', 'AE', 'ACE', 'ABE', 'ABCDE', 'ACF', 'AF', 'ABEF', 'A', 'ACD', 'ACDEF', 'ABDF', 'AEF'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    C = concentrations[0]
    A = concentrations[1]
    B = concentrations[2]
    E = concentrations[3]
    D = concentrations[4]
    F = concentrations[5]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    C_tot = state.C_tot
    D_tot = state.D_tot
    E_tot = state.E_tot
    F_tot = state.F_tot
    Kd = state.Kd

    result = np.zeros(6)
    result[0] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D/Kd**3 + A*B*C*E*F/Kd**4 + A*B*C*E/Kd**3 + A*B*C*F/Kd**3 + A*B*C/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*E/Kd**3 + A*C*D*F/Kd**3 + A*C*D/Kd**2 + A*C*E*F/Kd**3 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C/Kd + B*C*D*E*F/Kd**4 + B*C*D*E/Kd**3 + B*C*D*F/Kd**3 + B*C*D/Kd**2 + B*C*E*F/Kd**3 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C/Kd + C*D*E*F/Kd**3 + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D/Kd + C*E*F/Kd**2 + C*E/Kd + C*F/Kd + C - C_tot) / C_tot
    result[1] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D/Kd**3 + A*B*C*E*F/Kd**4 + A*B*C*E/Kd**3 + A*B*C*F/Kd**3 + A*B*C/Kd**2 + A*B*D*E*F/Kd**4 + A*B*D*E/Kd**3 + A*B*D*F/Kd**3 + A*B*D/Kd**2 + A*B*E*F/Kd**3 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B/Kd + A*C*D*E*F/Kd**4 + A*C*D*E/Kd**3 + A*C*D*F/Kd**3 + A*C*D/Kd**2 + A*C*E*F/Kd**3 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C/Kd + A*D*E*F/Kd**3 + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D/Kd + A*E*F/Kd**2 + A*E/Kd + A*F/Kd + A - A_tot) / A_tot
    result[2] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D/Kd**3 + A*B*C*E*F/Kd**4 + A*B*C*E/Kd**3 + A*B*C*F/Kd**3 + A*B*C/Kd**2 + A*B*D*E*F/Kd**4 + A*B*D*E/Kd**3 + A*B*D*F/Kd**3 + A*B*D/Kd**2 + A*B*E*F/Kd**3 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B/Kd + B*C*D*E*F/Kd**4 + B*C*D*E/Kd**3 + B*C*D*F/Kd**3 + B*C*D/Kd**2 + B*C*E*F/Kd**3 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C/Kd + B*D*E*F/Kd**3 + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D/Kd + B*E*F/Kd**2 + B*E/Kd + B*F/Kd + B - B_tot) / B_tot
    result[3] = (A*B*C*D*E/Kd**4 + A*B*C*E*F/Kd**4 + A*B*C*E/Kd**3 + A*B*D*E*F/Kd**4 + A*B*D*E/Kd**3 + A*B*E*F/Kd**3 + A*B*E/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*E/Kd**3 + A*C*E*F/Kd**3 + A*C*E/Kd**2 + A*D*E*F/Kd**3 + A*D*E/Kd**2 + A*E*F/Kd**2 + A*E/Kd + B*C*D*E*F/Kd**4 + B*C*D*E/Kd**3 + B*C*E*F/Kd**3 + B*C*E/Kd**2 + B*D*E*F/Kd**3 + B*D*E/Kd**2 + B*E*F/Kd**2 + B*E/Kd + C*D*E*F/Kd**3 + C*D*E/Kd**2 + C*E*F/Kd**2 + C*E/Kd + D*E*F/Kd**2 + D*E/Kd + E*F/Kd + E - E_tot) / E_tot
    result[4] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D/Kd**3 + A*B*D*E*F/Kd**4 + A*B*D*E/Kd**3 + A*B*D*F/Kd**3 + A*B*D/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*E/Kd**3 + A*C*D*F/Kd**3 + A*C*D/Kd**2 + A*D*E*F/Kd**3 + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D/Kd + B*C*D*E*F/Kd**4 + B*C*D*E/Kd**3 + B*C*D*F/Kd**3 + B*C*D/Kd**2 + B*D*E*F/Kd**3 + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D/Kd + C*D*E*F/Kd**3 + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D/Kd + D*E*F/Kd**2 + D*E/Kd + D*F/Kd + D - D_tot) / D_tot
    result[5] = (A*B*C*D*F/Kd**4 + A*B*C*E*F/Kd**4 + A*B*C*F/Kd**3 + A*B*D*E*F/Kd**4 + A*B*D*F/Kd**3 + A*B*E*F/Kd**3 + A*B*F/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*F/Kd**3 + A*C*E*F/Kd**3 + A*C*F/Kd**2 + A*D*E*F/Kd**3 + A*D*F/Kd**2 + A*E*F/Kd**2 + A*F/Kd + B*C*D*E*F/Kd**4 + B*C*D*F/Kd**3 + B*C*E*F/Kd**3 + B*C*F/Kd**2 + B*D*E*F/Kd**3 + B*D*F/Kd**2 + B*E*F/Kd**2 + B*F/Kd + C*D*E*F/Kd**3 + C*D*F/Kd**2 + C*E*F/Kd**2 + C*F/Kd + D*E*F/Kd**2 + D*F/Kd + E*F/Kd + F - F_tot) / F_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.C = solution[0]
    state.A = solution[1]
    state.B = solution[2]
    state.E = solution[3]
    state.D = solution[4]
    state.F = solution[5]

    # Readability 
    A = state.A
    B = state.B
    C = state.C
    D = state.D
    E = state.E
    F = state.F
    Kd = state.Kd

    # Dependent variables
    state.AB = A*B/Kd
    state.AC = A*C/Kd
    state.AD = A*D/Kd
    state.AE = A*E/Kd
    state.AF = A*F/Kd
    state.BC = B*C/Kd
    state.BD = B*D/Kd
    state.BE = B*E/Kd
    state.BF = B*F/Kd
    state.CD = C*D/Kd
    state.CE = C*E/Kd
    state.CF = C*F/Kd
    state.DE = D*E/Kd
    state.DF = D*F/Kd
    state.EF = E*F/Kd
    state.ABC = A*B*C/Kd**2
    state.ABD = A*B*D/Kd**2
    state.ABE = A*B*E/Kd**2
    state.ABF = A*B*F/Kd**2
    state.ACD = A*C*D/Kd**2
    state.ACE = A*C*E/Kd**2
    state.ACF = A*C*F/Kd**2
    state.ADE = A*D*E/Kd**2
    state.ADF = A*D*F/Kd**2
    state.AEF = A*E*F/Kd**2
    state.BCD = B*C*D/Kd**2
    state.BCE = B*C*E/Kd**2
    state.BCF = B*C*F/Kd**2
    state.BDE = B*D*E/Kd**2
    state.BDF = B*D*F/Kd**2
    state.BEF = B*E*F/Kd**2
    state.CDE = C*D*E/Kd**2
    state.CDF = C*D*F/Kd**2
    state.CEF = C*E*F/Kd**2
    state.DEF = D*E*F/Kd**2
    state.ABCD = A*B*C*D/Kd**3
    state.ABCE = A*B*C*E/Kd**3
    state.ABCF = A*B*C*F/Kd**3
    state.ABDE = A*B*D*E/Kd**3
    state.ABDF = A*B*D*F/Kd**3
    state.ABEF = A*B*E*F/Kd**3
    state.ACDE = A*C*D*E/Kd**3
    state.ACDF = A*C*D*F/Kd**3
    state.ACEF = A*C*E*F/Kd**3
    state.ADEF = A*D*E*F/Kd**3
    state.BCDE = B*C*D*E/Kd**3
    state.BCDF = B*C*D*F/Kd**3
    state.BCEF = B*C*E*F/Kd**3
    state.BDEF = B*D*E*F/Kd**3
    state.CDEF = C*D*E*F/Kd**3
    state.ABCDE = A*B*C*D*E/Kd**4
    state.ABCDF = A*B*C*D*F/Kd**4
    state.ABCEF = A*B*C*E*F/Kd**4
    state.ABDEF = A*B*D*E*F/Kd**4
    state.ACDEF = A*C*D*E*F/Kd**4
    state.BCDEF = B*C*D*E*F/Kd**4


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    A = state.A
    AB = state.AB
    ABC = state.ABC
    ABCD = state.ABCD
    ABCDE = state.ABCDE
    ABCDF = state.ABCDF
    ABCE = state.ABCE
    ABCEF = state.ABCEF
    ABCF = state.ABCF
    ABD = state.ABD
    ABDE = state.ABDE
    ABDEF = state.ABDEF
    ABDF = state.ABDF
    ABE = state.ABE
    ABEF = state.ABEF
    ABF = state.ABF
    AC = state.AC
    ACD = state.ACD
    ACDE = state.ACDE
    ACDEF = state.ACDEF
    ACDF = state.ACDF
    ACE = state.ACE
    ACEF = state.ACEF
    ACF = state.ACF
    AD = state.AD
    ADE = state.ADE
    ADEF = state.ADEF
    ADF = state.ADF
    AE = state.AE
    AEF = state.AEF
    AF = state.AF
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABCD + ABCDE + ABCDF + ABCE + ABCEF + ABCF + ABD + ABDE + ABDEF + ABDF + ABE + ABEF + ABF + AC + ACD + ACDE + ACDEF + ACDF + ACE + ACEF + ACF + AD + ADE + ADEF + ADF + AE + AEF + AF)/A_tot


