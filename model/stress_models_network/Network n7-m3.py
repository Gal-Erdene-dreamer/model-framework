"""
Model file created on 2021-08-20 13:54:43.957661 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; Kd
A + C = AC; Kd
A + D = AD; Kd
A + E = AE; Kd
A + F = AF; Kd
A + G = AG; Kd
B + C = BC; Kd
B + D = BD; Kd
B + E = BE; Kd
B + F = BF; Kd
B + G = BG; Kd
C + D = CD; Kd
C + E = CE; Kd
C + F = CF; Kd
C + G = CG; Kd
D + E = DE; Kd
D + F = DF; Kd
D + G = DG; Kd
E + F = EF; Kd
E + G = EG; Kd
F + G = FG; Kd
AB + C = ABC; Kd
AB + D = ABD; Kd
AB + E = ABE; Kd
AB + F = ABF; Kd
AB + G = ABG; Kd
AC + D = ACD; Kd
AC + E = ACE; Kd
AC + F = ACF; Kd
AC + G = ACG; Kd
AD + E = ADE; Kd
AD + F = ADF; Kd
AD + G = ADG; Kd
AE + F = AEF; Kd
AE + G = AEG; Kd
AF + G = AFG; Kd
BC + D = BCD; Kd
BC + E = BCE; Kd
BC + F = BCF; Kd
BC + G = BCG; Kd
BD + E = BDE; Kd
BD + F = BDF; Kd
BD + G = BDG; Kd
BE + F = BEF; Kd
BE + G = BEG; Kd
BF + G = BFG; Kd
CD + E = CDE; Kd
CD + F = CDF; Kd
CD + G = CDG; Kd
CE + F = CEF; Kd
CE + G = CEG; Kd
CF + G = CFG; Kd
DE + F = DEF; Kd
DE + G = DEG; Kd
DF + G = DFG; Kd
EF + G = EFG; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['ABC', 'BDG', 'FG', 'AD', 'BF', 'B', 'BEF', 'AB', 'AC', 'ADE', 'CDF', 'ADF', 'BC', 'ABF', 'F', 'AFG', 'BCG', 'G', 'CD', 'AG', 'ABD', 'BE', 'BEG', 'BCF', 'Kd', 'DEG', 'DFG', 'C', 'BDF', 'AE', 'BCE', 'CG', 'EG', 'ACE', 'BFG', 'CDG', 'EFG', 'ABE', 'CFG', 'EF', 'ACF', 'CF', 'BCD', 'AEG', 'AF', 'ABG', 'CEG', 'CE', 'BDE', 'A', 'ACD', 'ACG', 'ADG', 'BG', 'DE', 'DEF', 'E', 'CDE', 'AEF', 'D', 'CEF', 'DF', 'DG', 'BD', 'C_tot', 'G_tot', 'A_tot', 'B_tot', 'E_tot', 'D_tot', 'F_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['C', 'G', 'A', 'B', 'E', 'D', 'F']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'BC', 'BD', 'BE', 'BF', 'BG', 'CD', 'CE', 'CF', 'CG', 'DE', 'DF', 'DG', 'EF', 'EG', 'FG', 'ABC', 'ABD', 'ABE', 'ABF', 'ABG', 'ACD', 'ACE', 'ACF', 'ACG', 'ADE', 'ADF', 'ADG', 'AEF', 'AEG', 'AFG', 'BCD', 'BCE', 'BCF', 'BCG', 'BDE', 'BDF', 'BDG', 'BEF', 'BEG', 'BFG', 'CDE', 'CDF', 'CDG', 'CEF', 'CEG', 'CFG', 'DEF', 'DEG', 'DFG', 'EFG']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ABC', 'AD', 'AB', 'AC', 'ADE', 'ADF', 'ABF', 'AFG', 'AG', 'ABD', 'AE', 'ACE', 'ABE', 'ACF', 'AEG', 'AF', 'ABG', 'A', 'ACD', 'ACG', 'ADG', 'AEF'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    C = concentrations[0]
    G = concentrations[1]
    A = concentrations[2]
    B = concentrations[3]
    E = concentrations[4]
    D = concentrations[5]
    F = concentrations[6]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    C_tot = state.C_tot
    D_tot = state.D_tot
    E_tot = state.E_tot
    F_tot = state.F_tot
    G_tot = state.G_tot
    Kd = state.Kd

    result = np.zeros(7)
    result[0] = (A*B*C/Kd**2 + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C/Kd + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C/Kd + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D/Kd + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E/Kd + C*F*G/Kd**2 + C*F/Kd + C*G/Kd + C - C_tot) / C_tot
    result[1] = (A*B*G/Kd**2 + A*C*G/Kd**2 + A*D*G/Kd**2 + A*E*G/Kd**2 + A*F*G/Kd**2 + A*G/Kd + B*C*G/Kd**2 + B*D*G/Kd**2 + B*E*G/Kd**2 + B*F*G/Kd**2 + B*G/Kd + C*D*G/Kd**2 + C*E*G/Kd**2 + C*F*G/Kd**2 + C*G/Kd + D*E*G/Kd**2 + D*F*G/Kd**2 + D*G/Kd + E*F*G/Kd**2 + E*G/Kd + F*G/Kd + G - G_tot) / G_tot
    result[2] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B/Kd + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C/Kd + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D/Kd + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E/Kd + A*F*G/Kd**2 + A*F/Kd + A*G/Kd + A - A_tot) / A_tot
    result[3] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B/Kd + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C/Kd + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D/Kd + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E/Kd + B*F*G/Kd**2 + B*F/Kd + B*G/Kd + B - B_tot) / B_tot
    result[4] = (A*B*E/Kd**2 + A*C*E/Kd**2 + A*D*E/Kd**2 + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E/Kd + B*C*E/Kd**2 + B*D*E/Kd**2 + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E/Kd + C*D*E/Kd**2 + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E/Kd + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E/Kd + E*F*G/Kd**2 + E*F/Kd + E*G/Kd + E - E_tot) / E_tot
    result[5] = (A*B*D/Kd**2 + A*C*D/Kd**2 + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D/Kd + B*C*D/Kd**2 + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D/Kd + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D/Kd + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E/Kd + D*F*G/Kd**2 + D*F/Kd + D*G/Kd + D - D_tot) / D_tot
    result[6] = (A*B*F/Kd**2 + A*C*F/Kd**2 + A*D*F/Kd**2 + A*E*F/Kd**2 + A*F*G/Kd**2 + A*F/Kd + B*C*F/Kd**2 + B*D*F/Kd**2 + B*E*F/Kd**2 + B*F*G/Kd**2 + B*F/Kd + C*D*F/Kd**2 + C*E*F/Kd**2 + C*F*G/Kd**2 + C*F/Kd + D*E*F/Kd**2 + D*F*G/Kd**2 + D*F/Kd + E*F*G/Kd**2 + E*F/Kd + F*G/Kd + F - F_tot) / F_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.C = solution[0]
    state.G = solution[1]
    state.A = solution[2]
    state.B = solution[3]
    state.E = solution[4]
    state.D = solution[5]
    state.F = solution[6]

    # Readability 
    A = state.A
    B = state.B
    C = state.C
    D = state.D
    E = state.E
    F = state.F
    G = state.G
    Kd = state.Kd

    # Dependent variables
    state.AB = A*B/Kd
    state.AC = A*C/Kd
    state.AD = A*D/Kd
    state.AE = A*E/Kd
    state.AF = A*F/Kd
    state.AG = A*G/Kd
    state.BC = B*C/Kd
    state.BD = B*D/Kd
    state.BE = B*E/Kd
    state.BF = B*F/Kd
    state.BG = B*G/Kd
    state.CD = C*D/Kd
    state.CE = C*E/Kd
    state.CF = C*F/Kd
    state.CG = C*G/Kd
    state.DE = D*E/Kd
    state.DF = D*F/Kd
    state.DG = D*G/Kd
    state.EF = E*F/Kd
    state.EG = E*G/Kd
    state.FG = F*G/Kd
    state.ABC = A*B*C/Kd**2
    state.ABD = A*B*D/Kd**2
    state.ABE = A*B*E/Kd**2
    state.ABF = A*B*F/Kd**2
    state.ABG = A*B*G/Kd**2
    state.ACD = A*C*D/Kd**2
    state.ACE = A*C*E/Kd**2
    state.ACF = A*C*F/Kd**2
    state.ACG = A*C*G/Kd**2
    state.ADE = A*D*E/Kd**2
    state.ADF = A*D*F/Kd**2
    state.ADG = A*D*G/Kd**2
    state.AEF = A*E*F/Kd**2
    state.AEG = A*E*G/Kd**2
    state.AFG = A*F*G/Kd**2
    state.BCD = B*C*D/Kd**2
    state.BCE = B*C*E/Kd**2
    state.BCF = B*C*F/Kd**2
    state.BCG = B*C*G/Kd**2
    state.BDE = B*D*E/Kd**2
    state.BDF = B*D*F/Kd**2
    state.BDG = B*D*G/Kd**2
    state.BEF = B*E*F/Kd**2
    state.BEG = B*E*G/Kd**2
    state.BFG = B*F*G/Kd**2
    state.CDE = C*D*E/Kd**2
    state.CDF = C*D*F/Kd**2
    state.CDG = C*D*G/Kd**2
    state.CEF = C*E*F/Kd**2
    state.CEG = C*E*G/Kd**2
    state.CFG = C*F*G/Kd**2
    state.DEF = D*E*F/Kd**2
    state.DEG = D*E*G/Kd**2
    state.DFG = D*F*G/Kd**2
    state.EFG = E*F*G/Kd**2


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    A = state.A
    AB = state.AB
    ABC = state.ABC
    ABD = state.ABD
    ABE = state.ABE
    ABF = state.ABF
    ABG = state.ABG
    AC = state.AC
    ACD = state.ACD
    ACE = state.ACE
    ACF = state.ACF
    ACG = state.ACG
    AD = state.AD
    ADE = state.ADE
    ADF = state.ADF
    ADG = state.ADG
    AE = state.AE
    AEF = state.AEF
    AEG = state.AEG
    AF = state.AF
    AFG = state.AFG
    AG = state.AG
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABD + ABE + ABF + ABG + AC + ACD + ACE + ACF + ACG + AD + ADE + ADF + ADG + AE + AEF + AEG + AF + AFG + AG)/A_tot


