"""
Model file created on 2021-08-20 14:01:36.854293 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
A + B = AB; Kd
A + C = AC; Kd
A + D = AD; Kd
A + E = AE; Kd
A + F = AF; Kd
A + G = AG; Kd
A + H = AH; Kd
B + C = BC; Kd
B + D = BD; Kd
B + E = BE; Kd
B + F = BF; Kd
B + G = BG; Kd
B + H = BH; Kd
C + D = CD; Kd
C + E = CE; Kd
C + F = CF; Kd
C + G = CG; Kd
C + H = CH; Kd
D + E = DE; Kd
D + F = DF; Kd
D + G = DG; Kd
D + H = DH; Kd
E + F = EF; Kd
E + G = EG; Kd
E + H = EH; Kd
F + G = FG; Kd
F + H = FH; Kd
G + H = GH; Kd
AB + C = ABC; Kd
AB + D = ABD; Kd
AB + E = ABE; Kd
AB + F = ABF; Kd
AB + G = ABG; Kd
AB + H = ABH; Kd
AC + D = ACD; Kd
AC + E = ACE; Kd
AC + F = ACF; Kd
AC + G = ACG; Kd
AC + H = ACH; Kd
AD + E = ADE; Kd
AD + F = ADF; Kd
AD + G = ADG; Kd
AD + H = ADH; Kd
AE + F = AEF; Kd
AE + G = AEG; Kd
AE + H = AEH; Kd
AF + G = AFG; Kd
AF + H = AFH; Kd
AG + H = AGH; Kd
BC + D = BCD; Kd
BC + E = BCE; Kd
BC + F = BCF; Kd
BC + G = BCG; Kd
BC + H = BCH; Kd
BD + E = BDE; Kd
BD + F = BDF; Kd
BD + G = BDG; Kd
BD + H = BDH; Kd
BE + F = BEF; Kd
BE + G = BEG; Kd
BE + H = BEH; Kd
BF + G = BFG; Kd
BF + H = BFH; Kd
BG + H = BGH; Kd
CD + E = CDE; Kd
CD + F = CDF; Kd
CD + G = CDG; Kd
CD + H = CDH; Kd
CE + F = CEF; Kd
CE + G = CEG; Kd
CE + H = CEH; Kd
CF + G = CFG; Kd
CF + H = CFH; Kd
CG + H = CGH; Kd
DE + F = DEF; Kd
DE + G = DEG; Kd
DE + H = DEH; Kd
DF + G = DFG; Kd
DF + H = DFH; Kd
DG + H = DGH; Kd
EF + G = EFG; Kd
EF + H = EFH; Kd
EG + H = EGH; Kd
FG + H = FGH; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['CDH', 'ACH', 'ABC', 'EFH', 'BH', 'CDF', 'ADF', 'BC', 'ABH', 'F', 'AFG', 'BCG', 'ABD', 'H', 'BE', 'Kd', 'CEH', 'GH', 'AE', 'CG', 'DH', 'ACE', 'CDG', 'BCH', 'CF', 'BDH', 'CE', 'BDE', 'ACD', 'CH', 'BG', 'DG', 'FH', 'AFH', 'ADH', 'FG', 'BDG', 'AD', 'BF', 'DEH', 'B', 'BEF', 'AB', 'AC', 'ADE', 'AEH', 'ABF', 'G', 'BEH', 'CD', 'AG', 'DGH', 'BEG', 'BCF', 'DEG', 'CFH', 'DFG', 'BDF', 'CGH', 'DFH', 'BCE', 'EG', 'BFG', 'EFG', 'ABE', 'EH', 'CFG', 'EF', 'ACF', 'AH', 'BCD', 'AEG', 'AF', 'BGH', 'FGH', 'ABG', 'AGH', 'CEG', 'A', 'ACG', 'ADG', 'DEF', 'DE', 'E', 'CDE', 'AEF', 'D', 'EGH', 'CEF', 'BFH', 'DF', 'C', 'BD', 'B_tot', 'F_tot', 'G_tot', 'A_tot', 'E_tot', 'D_tot', 'H_tot', 'C_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['B', 'F', 'G', 'A', 'E', 'D', 'H', 'C']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'CD', 'CE', 'CF', 'CG', 'CH', 'DE', 'DF', 'DG', 'DH', 'EF', 'EG', 'EH', 'FG', 'FH', 'GH', 'ABC', 'ABD', 'ABE', 'ABF', 'ABG', 'ABH', 'ACD', 'ACE', 'ACF', 'ACG', 'ACH', 'ADE', 'ADF', 'ADG', 'ADH', 'AEF', 'AEG', 'AEH', 'AFG', 'AFH', 'AGH', 'BCD', 'BCE', 'BCF', 'BCG', 'BCH', 'BDE', 'BDF', 'BDG', 'BDH', 'BEF', 'BEG', 'BEH', 'BFG', 'BFH', 'BGH', 'CDE', 'CDF', 'CDG', 'CDH', 'CEF', 'CEG', 'CEH', 'CFG', 'CFH', 'CGH', 'DEF', 'DEG', 'DEH', 'DFG', 'DFH', 'DGH', 'EFG', 'EFH', 'EGH', 'FGH']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ACH', 'ABC', 'ADF', 'ABH', 'AFG', 'ABD', 'AE', 'ACE', 'ACD', 'AFH', 'ADH', 'AD', 'AB', 'AC', 'ADE', 'AEH', 'ABF', 'AG', 'ABE', 'ACF', 'AH', 'AEG', 'AF', 'ABG', 'AGH', 'A', 'ACG', 'ADG', 'AEF'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    B = concentrations[0]
    F = concentrations[1]
    G = concentrations[2]
    A = concentrations[3]
    E = concentrations[4]
    D = concentrations[5]
    H = concentrations[6]
    C = concentrations[7]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    C_tot = state.C_tot
    D_tot = state.D_tot
    E_tot = state.E_tot
    F_tot = state.F_tot
    G_tot = state.G_tot
    H_tot = state.H_tot
    Kd = state.Kd

    result = np.zeros(8)
    result[0] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B*H/Kd**2 + A*B/Kd + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C*H/Kd**2 + B*C/Kd + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D*H/Kd**2 + B*D/Kd + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E*H/Kd**2 + B*E/Kd + B*F*G/Kd**2 + B*F*H/Kd**2 + B*F/Kd + B*G*H/Kd**2 + B*G/Kd + B*H/Kd + B - B_tot) / B_tot
    result[1] = (A*B*F/Kd**2 + A*C*F/Kd**2 + A*D*F/Kd**2 + A*E*F/Kd**2 + A*F*G/Kd**2 + A*F*H/Kd**2 + A*F/Kd + B*C*F/Kd**2 + B*D*F/Kd**2 + B*E*F/Kd**2 + B*F*G/Kd**2 + B*F*H/Kd**2 + B*F/Kd + C*D*F/Kd**2 + C*E*F/Kd**2 + C*F*G/Kd**2 + C*F*H/Kd**2 + C*F/Kd + D*E*F/Kd**2 + D*F*G/Kd**2 + D*F*H/Kd**2 + D*F/Kd + E*F*G/Kd**2 + E*F*H/Kd**2 + E*F/Kd + F*G*H/Kd**2 + F*G/Kd + F*H/Kd + F - F_tot) / F_tot
    result[2] = (A*B*G/Kd**2 + A*C*G/Kd**2 + A*D*G/Kd**2 + A*E*G/Kd**2 + A*F*G/Kd**2 + A*G*H/Kd**2 + A*G/Kd + B*C*G/Kd**2 + B*D*G/Kd**2 + B*E*G/Kd**2 + B*F*G/Kd**2 + B*G*H/Kd**2 + B*G/Kd + C*D*G/Kd**2 + C*E*G/Kd**2 + C*F*G/Kd**2 + C*G*H/Kd**2 + C*G/Kd + D*E*G/Kd**2 + D*F*G/Kd**2 + D*G*H/Kd**2 + D*G/Kd + E*F*G/Kd**2 + E*G*H/Kd**2 + E*G/Kd + F*G*H/Kd**2 + F*G/Kd + G*H/Kd + G - G_tot) / G_tot
    result[3] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B*H/Kd**2 + A*B/Kd + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C*H/Kd**2 + A*C/Kd + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D*H/Kd**2 + A*D/Kd + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E*H/Kd**2 + A*E/Kd + A*F*G/Kd**2 + A*F*H/Kd**2 + A*F/Kd + A*G*H/Kd**2 + A*G/Kd + A*H/Kd + A - A_tot) / A_tot
    result[4] = (A*B*E/Kd**2 + A*C*E/Kd**2 + A*D*E/Kd**2 + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E*H/Kd**2 + A*E/Kd + B*C*E/Kd**2 + B*D*E/Kd**2 + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E*H/Kd**2 + B*E/Kd + C*D*E/Kd**2 + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E*H/Kd**2 + C*E/Kd + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E*H/Kd**2 + D*E/Kd + E*F*G/Kd**2 + E*F*H/Kd**2 + E*F/Kd + E*G*H/Kd**2 + E*G/Kd + E*H/Kd + E - E_tot) / E_tot
    result[5] = (A*B*D/Kd**2 + A*C*D/Kd**2 + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D*H/Kd**2 + A*D/Kd + B*C*D/Kd**2 + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D*H/Kd**2 + B*D/Kd + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D*H/Kd**2 + C*D/Kd + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E*H/Kd**2 + D*E/Kd + D*F*G/Kd**2 + D*F*H/Kd**2 + D*F/Kd + D*G*H/Kd**2 + D*G/Kd + D*H/Kd + D - D_tot) / D_tot
    result[6] = (A*B*H/Kd**2 + A*C*H/Kd**2 + A*D*H/Kd**2 + A*E*H/Kd**2 + A*F*H/Kd**2 + A*G*H/Kd**2 + A*H/Kd + B*C*H/Kd**2 + B*D*H/Kd**2 + B*E*H/Kd**2 + B*F*H/Kd**2 + B*G*H/Kd**2 + B*H/Kd + C*D*H/Kd**2 + C*E*H/Kd**2 + C*F*H/Kd**2 + C*G*H/Kd**2 + C*H/Kd + D*E*H/Kd**2 + D*F*H/Kd**2 + D*G*H/Kd**2 + D*H/Kd + E*F*H/Kd**2 + E*G*H/Kd**2 + E*H/Kd + F*G*H/Kd**2 + F*H/Kd + G*H/Kd + H - H_tot) / H_tot
    result[7] = (A*B*C/Kd**2 + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C*H/Kd**2 + A*C/Kd + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C*H/Kd**2 + B*C/Kd + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D*H/Kd**2 + C*D/Kd + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E*H/Kd**2 + C*E/Kd + C*F*G/Kd**2 + C*F*H/Kd**2 + C*F/Kd + C*G*H/Kd**2 + C*G/Kd + C*H/Kd + C - C_tot) / C_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.B = solution[0]
    state.F = solution[1]
    state.G = solution[2]
    state.A = solution[3]
    state.E = solution[4]
    state.D = solution[5]
    state.H = solution[6]
    state.C = solution[7]

    # Readability 
    A = state.A
    B = state.B
    C = state.C
    D = state.D
    E = state.E
    F = state.F
    G = state.G
    H = state.H
    Kd = state.Kd

    # Dependent variables
    state.AB = A*B/Kd
    state.AC = A*C/Kd
    state.AD = A*D/Kd
    state.AE = A*E/Kd
    state.AF = A*F/Kd
    state.AG = A*G/Kd
    state.AH = A*H/Kd
    state.BC = B*C/Kd
    state.BD = B*D/Kd
    state.BE = B*E/Kd
    state.BF = B*F/Kd
    state.BG = B*G/Kd
    state.BH = B*H/Kd
    state.CD = C*D/Kd
    state.CE = C*E/Kd
    state.CF = C*F/Kd
    state.CG = C*G/Kd
    state.CH = C*H/Kd
    state.DE = D*E/Kd
    state.DF = D*F/Kd
    state.DG = D*G/Kd
    state.DH = D*H/Kd
    state.EF = E*F/Kd
    state.EG = E*G/Kd
    state.EH = E*H/Kd
    state.FG = F*G/Kd
    state.FH = F*H/Kd
    state.GH = G*H/Kd
    state.ABC = A*B*C/Kd**2
    state.ABD = A*B*D/Kd**2
    state.ABE = A*B*E/Kd**2
    state.ABF = A*B*F/Kd**2
    state.ABG = A*B*G/Kd**2
    state.ABH = A*B*H/Kd**2
    state.ACD = A*C*D/Kd**2
    state.ACE = A*C*E/Kd**2
    state.ACF = A*C*F/Kd**2
    state.ACG = A*C*G/Kd**2
    state.ACH = A*C*H/Kd**2
    state.ADE = A*D*E/Kd**2
    state.ADF = A*D*F/Kd**2
    state.ADG = A*D*G/Kd**2
    state.ADH = A*D*H/Kd**2
    state.AEF = A*E*F/Kd**2
    state.AEG = A*E*G/Kd**2
    state.AEH = A*E*H/Kd**2
    state.AFG = A*F*G/Kd**2
    state.AFH = A*F*H/Kd**2
    state.AGH = A*G*H/Kd**2
    state.BCD = B*C*D/Kd**2
    state.BCE = B*C*E/Kd**2
    state.BCF = B*C*F/Kd**2
    state.BCG = B*C*G/Kd**2
    state.BCH = B*C*H/Kd**2
    state.BDE = B*D*E/Kd**2
    state.BDF = B*D*F/Kd**2
    state.BDG = B*D*G/Kd**2
    state.BDH = B*D*H/Kd**2
    state.BEF = B*E*F/Kd**2
    state.BEG = B*E*G/Kd**2
    state.BEH = B*E*H/Kd**2
    state.BFG = B*F*G/Kd**2
    state.BFH = B*F*H/Kd**2
    state.BGH = B*G*H/Kd**2
    state.CDE = C*D*E/Kd**2
    state.CDF = C*D*F/Kd**2
    state.CDG = C*D*G/Kd**2
    state.CDH = C*D*H/Kd**2
    state.CEF = C*E*F/Kd**2
    state.CEG = C*E*G/Kd**2
    state.CEH = C*E*H/Kd**2
    state.CFG = C*F*G/Kd**2
    state.CFH = C*F*H/Kd**2
    state.CGH = C*G*H/Kd**2
    state.DEF = D*E*F/Kd**2
    state.DEG = D*E*G/Kd**2
    state.DEH = D*E*H/Kd**2
    state.DFG = D*F*G/Kd**2
    state.DFH = D*F*H/Kd**2
    state.DGH = D*G*H/Kd**2
    state.EFG = E*F*G/Kd**2
    state.EFH = E*F*H/Kd**2
    state.EGH = E*G*H/Kd**2
    state.FGH = F*G*H/Kd**2


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
    ABH = state.ABH
    AC = state.AC
    ACD = state.ACD
    ACE = state.ACE
    ACF = state.ACF
    ACG = state.ACG
    ACH = state.ACH
    AD = state.AD
    ADE = state.ADE
    ADF = state.ADF
    ADG = state.ADG
    ADH = state.ADH
    AE = state.AE
    AEF = state.AEF
    AEG = state.AEG
    AEH = state.AEH
    AF = state.AF
    AFG = state.AFG
    AFH = state.AFH
    AG = state.AG
    AGH = state.AGH
    AH = state.AH
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABD + ABE + ABF + ABG + ABH + AC + ACD + ACE + ACF + ACG + ACH + AD + ADE + ADF + ADG + ADH + AE + AEF + AEG + AEH + AF + AFG + AFH + AG + AGH + AH)/A_tot


