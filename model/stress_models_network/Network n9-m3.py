"""
Model file created on 2021-08-20 14:03:10.863731 
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
A + I = AI; Kd
B + C = BC; Kd
B + D = BD; Kd
B + E = BE; Kd
B + F = BF; Kd
B + G = BG; Kd
B + H = BH; Kd
B + I = BI; Kd
C + D = CD; Kd
C + E = CE; Kd
C + F = CF; Kd
C + G = CG; Kd
C + H = CH; Kd
C + I = CI; Kd
D + E = DE; Kd
D + F = DF; Kd
D + G = DG; Kd
D + H = DH; Kd
D + I = DI; Kd
E + F = EF; Kd
E + G = EG; Kd
E + H = EH; Kd
E + I = EI; Kd
F + G = FG; Kd
F + H = FH; Kd
F + I = FI; Kd
G + H = GH; Kd
G + I = GI; Kd
H + I = HI; Kd
AB + C = ABC; Kd
AB + D = ABD; Kd
AB + E = ABE; Kd
AB + F = ABF; Kd
AB + G = ABG; Kd
AB + H = ABH; Kd
AB + I = ABI; Kd
AC + D = ACD; Kd
AC + E = ACE; Kd
AC + F = ACF; Kd
AC + G = ACG; Kd
AC + H = ACH; Kd
AC + I = ACI; Kd
AD + E = ADE; Kd
AD + F = ADF; Kd
AD + G = ADG; Kd
AD + H = ADH; Kd
AD + I = ADI; Kd
AE + F = AEF; Kd
AE + G = AEG; Kd
AE + H = AEH; Kd
AE + I = AEI; Kd
AF + G = AFG; Kd
AF + H = AFH; Kd
AF + I = AFI; Kd
AG + H = AGH; Kd
AG + I = AGI; Kd
AH + I = AHI; Kd
BC + D = BCD; Kd
BC + E = BCE; Kd
BC + F = BCF; Kd
BC + G = BCG; Kd
BC + H = BCH; Kd
BC + I = BCI; Kd
BD + E = BDE; Kd
BD + F = BDF; Kd
BD + G = BDG; Kd
BD + H = BDH; Kd
BD + I = BDI; Kd
BE + F = BEF; Kd
BE + G = BEG; Kd
BE + H = BEH; Kd
BE + I = BEI; Kd
BF + G = BFG; Kd
BF + H = BFH; Kd
BF + I = BFI; Kd
BG + H = BGH; Kd
BG + I = BGI; Kd
BH + I = BHI; Kd
CD + E = CDE; Kd
CD + F = CDF; Kd
CD + G = CDG; Kd
CD + H = CDH; Kd
CD + I = CDI; Kd
CE + F = CEF; Kd
CE + G = CEG; Kd
CE + H = CEH; Kd
CE + I = CEI; Kd
CF + G = CFG; Kd
CF + H = CFH; Kd
CF + I = CFI; Kd
CG + H = CGH; Kd
CG + I = CGI; Kd
CH + I = CHI; Kd
DE + F = DEF; Kd
DE + G = DEG; Kd
DE + H = DEH; Kd
DE + I = DEI; Kd
DF + G = DFG; Kd
DF + H = DFH; Kd
DF + I = DFI; Kd
DG + H = DGH; Kd
DG + I = DGI; Kd
DH + I = DHI; Kd
EF + G = EFG; Kd
EF + H = EFH; Kd
EF + I = EFI; Kd
EG + H = EGH; Kd
EG + I = EGI; Kd
EH + I = EHI; Kd
FG + H = FGH; Kd
FG + I = FGI; Kd
FH + I = FHI; Kd
GH + I = GHI; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['CDH', 'ACH', 'EFH', 'CDF', 'ADF', 'BC', 'F', 'GI', 'BHI', 'AFI', 'CEH', 'GH', 'DH', 'CFI', 'ACE', 'CDG', 'BCH', 'DI', 'CF', 'BDE', 'ACD', 'BCI', 'BDG', 'FG', 'BF', 'B', 'BEF', 'AC', 'AEH', 'FI', 'EI', 'ABI', 'BEH', 'CHI', 'CD', 'AG', 'DGH', 'I', 'BEG', 'BCF', 'CGI', 'DFG', 'CFH', 'BEI', 'BDF', 'BCE', 'BFG', 'EFG', 'CFG', 'EFI', 'EF', 'BGH', 'BCD', 'AF', 'ABG', 'CEG', 'A', 'ACG', 'ADG', 'DE', 'E', 'AEF', 'D', 'EGH', 'CEF', 'DF', 'ABC', 'BH', 'ABH', 'HI', 'AFG', 'BCG', 'DHI', 'GHI', 'ABD', 'H', 'BE', 'BI', 'Kd', 'AE', 'BFI', 'CG', 'AEI', 'EHI', 'AGI', 'BDH', 'DGI', 'CE', 'CH', 'BDI', 'BG', 'FHI', 'AHI', 'DG', 'FH', 'AFH', 'ADH', 'DEH', 'AD', 'EGI', 'AB', 'ADE', 'ACI', 'ABF', 'ADI', 'G', 'DFI', 'BGI', 'DEG', 'CGH', 'DFH', 'EG', 'DEI', 'ABE', 'EH', 'ACF', 'AH', 'AEG', 'FGH', 'FGI', 'AGH', 'AI', 'DEF', 'CDE', 'CDI', 'BFH', 'CI', 'CEI', 'C', 'BD', 'F_tot', 'B_tot', 'I_tot', 'A_tot', 'E_tot', 'D_tot', 'H_tot', 'G_tot', 'C_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['F', 'B', 'I', 'A', 'E', 'D', 'H', 'G', 'C']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'DE', 'DF', 'DG', 'DH', 'DI', 'EF', 'EG', 'EH', 'EI', 'FG', 'FH', 'FI', 'GH', 'GI', 'HI', 'ABC', 'ABD', 'ABE', 'ABF', 'ABG', 'ABH', 'ABI', 'ACD', 'ACE', 'ACF', 'ACG', 'ACH', 'ACI', 'ADE', 'ADF', 'ADG', 'ADH', 'ADI', 'AEF', 'AEG', 'AEH', 'AEI', 'AFG', 'AFH', 'AFI', 'AGH', 'AGI', 'AHI', 'BCD', 'BCE', 'BCF', 'BCG', 'BCH', 'BCI', 'BDE', 'BDF', 'BDG', 'BDH', 'BDI', 'BEF', 'BEG', 'BEH', 'BEI', 'BFG', 'BFH', 'BFI', 'BGH', 'BGI', 'BHI', 'CDE', 'CDF', 'CDG', 'CDH', 'CDI', 'CEF', 'CEG', 'CEH', 'CEI', 'CFG', 'CFH', 'CFI', 'CGH', 'CGI', 'CHI', 'DEF', 'DEG', 'DEH', 'DEI', 'DFG', 'DFH', 'DFI', 'DGH', 'DGI', 'DHI', 'EFG', 'EFH', 'EFI', 'EGH', 'EGI', 'EHI', 'FGH', 'FGI', 'FHI', 'GHI']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ACH', 'ADF', 'AFI', 'ACE', 'ACD', 'AC', 'AEH', 'ABI', 'AG', 'AF', 'ABG', 'A', 'ACG', 'ADG', 'AEF', 'ABC', 'ABH', 'AFG', 'ABD', 'AE', 'AEI', 'AGI', 'AHI', 'AFH', 'ADH', 'AD', 'AB', 'ADE', 'ACI', 'ABF', 'ADI', 'ABE', 'ACF', 'AH', 'AEG', 'AGH', 'AI'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    F = concentrations[0]
    B = concentrations[1]
    I = concentrations[2]
    A = concentrations[3]
    E = concentrations[4]
    D = concentrations[5]
    H = concentrations[6]
    G = concentrations[7]
    C = concentrations[8]

    # Readability
    A_tot = state.A_tot
    B_tot = state.B_tot
    C_tot = state.C_tot
    D_tot = state.D_tot
    E_tot = state.E_tot
    F_tot = state.F_tot
    G_tot = state.G_tot
    H_tot = state.H_tot
    I_tot = state.I_tot
    Kd = state.Kd

    result = np.zeros(9)
    result[0] = (A*B*F/Kd**2 + A*C*F/Kd**2 + A*D*F/Kd**2 + A*E*F/Kd**2 + A*F*G/Kd**2 + A*F*H/Kd**2 + A*F*I/Kd**2 + A*F/Kd + B*C*F/Kd**2 + B*D*F/Kd**2 + B*E*F/Kd**2 + B*F*G/Kd**2 + B*F*H/Kd**2 + B*F*I/Kd**2 + B*F/Kd + C*D*F/Kd**2 + C*E*F/Kd**2 + C*F*G/Kd**2 + C*F*H/Kd**2 + C*F*I/Kd**2 + C*F/Kd + D*E*F/Kd**2 + D*F*G/Kd**2 + D*F*H/Kd**2 + D*F*I/Kd**2 + D*F/Kd + E*F*G/Kd**2 + E*F*H/Kd**2 + E*F*I/Kd**2 + E*F/Kd + F*G*H/Kd**2 + F*G*I/Kd**2 + F*G/Kd + F*H*I/Kd**2 + F*H/Kd + F*I/Kd + F - F_tot) / F_tot
    result[1] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B*H/Kd**2 + A*B*I/Kd**2 + A*B/Kd + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C*H/Kd**2 + B*C*I/Kd**2 + B*C/Kd + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D*H/Kd**2 + B*D*I/Kd**2 + B*D/Kd + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E*H/Kd**2 + B*E*I/Kd**2 + B*E/Kd + B*F*G/Kd**2 + B*F*H/Kd**2 + B*F*I/Kd**2 + B*F/Kd + B*G*H/Kd**2 + B*G*I/Kd**2 + B*G/Kd + B*H*I/Kd**2 + B*H/Kd + B*I/Kd + B - B_tot) / B_tot
    result[2] = (A*B*I/Kd**2 + A*C*I/Kd**2 + A*D*I/Kd**2 + A*E*I/Kd**2 + A*F*I/Kd**2 + A*G*I/Kd**2 + A*H*I/Kd**2 + A*I/Kd + B*C*I/Kd**2 + B*D*I/Kd**2 + B*E*I/Kd**2 + B*F*I/Kd**2 + B*G*I/Kd**2 + B*H*I/Kd**2 + B*I/Kd + C*D*I/Kd**2 + C*E*I/Kd**2 + C*F*I/Kd**2 + C*G*I/Kd**2 + C*H*I/Kd**2 + C*I/Kd + D*E*I/Kd**2 + D*F*I/Kd**2 + D*G*I/Kd**2 + D*H*I/Kd**2 + D*I/Kd + E*F*I/Kd**2 + E*G*I/Kd**2 + E*H*I/Kd**2 + E*I/Kd + F*G*I/Kd**2 + F*H*I/Kd**2 + F*I/Kd + G*H*I/Kd**2 + G*I/Kd + H*I/Kd + I - I_tot) / I_tot
    result[3] = (A*B*C/Kd**2 + A*B*D/Kd**2 + A*B*E/Kd**2 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B*H/Kd**2 + A*B*I/Kd**2 + A*B/Kd + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C*H/Kd**2 + A*C*I/Kd**2 + A*C/Kd + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D*H/Kd**2 + A*D*I/Kd**2 + A*D/Kd + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E*H/Kd**2 + A*E*I/Kd**2 + A*E/Kd + A*F*G/Kd**2 + A*F*H/Kd**2 + A*F*I/Kd**2 + A*F/Kd + A*G*H/Kd**2 + A*G*I/Kd**2 + A*G/Kd + A*H*I/Kd**2 + A*H/Kd + A*I/Kd + A - A_tot) / A_tot
    result[4] = (A*B*E/Kd**2 + A*C*E/Kd**2 + A*D*E/Kd**2 + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E*H/Kd**2 + A*E*I/Kd**2 + A*E/Kd + B*C*E/Kd**2 + B*D*E/Kd**2 + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E*H/Kd**2 + B*E*I/Kd**2 + B*E/Kd + C*D*E/Kd**2 + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E*H/Kd**2 + C*E*I/Kd**2 + C*E/Kd + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E*H/Kd**2 + D*E*I/Kd**2 + D*E/Kd + E*F*G/Kd**2 + E*F*H/Kd**2 + E*F*I/Kd**2 + E*F/Kd + E*G*H/Kd**2 + E*G*I/Kd**2 + E*G/Kd + E*H*I/Kd**2 + E*H/Kd + E*I/Kd + E - E_tot) / E_tot
    result[5] = (A*B*D/Kd**2 + A*C*D/Kd**2 + A*D*E/Kd**2 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D*H/Kd**2 + A*D*I/Kd**2 + A*D/Kd + B*C*D/Kd**2 + B*D*E/Kd**2 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D*H/Kd**2 + B*D*I/Kd**2 + B*D/Kd + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D*H/Kd**2 + C*D*I/Kd**2 + C*D/Kd + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E*H/Kd**2 + D*E*I/Kd**2 + D*E/Kd + D*F*G/Kd**2 + D*F*H/Kd**2 + D*F*I/Kd**2 + D*F/Kd + D*G*H/Kd**2 + D*G*I/Kd**2 + D*G/Kd + D*H*I/Kd**2 + D*H/Kd + D*I/Kd + D - D_tot) / D_tot
    result[6] = (A*B*H/Kd**2 + A*C*H/Kd**2 + A*D*H/Kd**2 + A*E*H/Kd**2 + A*F*H/Kd**2 + A*G*H/Kd**2 + A*H*I/Kd**2 + A*H/Kd + B*C*H/Kd**2 + B*D*H/Kd**2 + B*E*H/Kd**2 + B*F*H/Kd**2 + B*G*H/Kd**2 + B*H*I/Kd**2 + B*H/Kd + C*D*H/Kd**2 + C*E*H/Kd**2 + C*F*H/Kd**2 + C*G*H/Kd**2 + C*H*I/Kd**2 + C*H/Kd + D*E*H/Kd**2 + D*F*H/Kd**2 + D*G*H/Kd**2 + D*H*I/Kd**2 + D*H/Kd + E*F*H/Kd**2 + E*G*H/Kd**2 + E*H*I/Kd**2 + E*H/Kd + F*G*H/Kd**2 + F*H*I/Kd**2 + F*H/Kd + G*H*I/Kd**2 + G*H/Kd + H*I/Kd + H - H_tot) / H_tot
    result[7] = (A*B*G/Kd**2 + A*C*G/Kd**2 + A*D*G/Kd**2 + A*E*G/Kd**2 + A*F*G/Kd**2 + A*G*H/Kd**2 + A*G*I/Kd**2 + A*G/Kd + B*C*G/Kd**2 + B*D*G/Kd**2 + B*E*G/Kd**2 + B*F*G/Kd**2 + B*G*H/Kd**2 + B*G*I/Kd**2 + B*G/Kd + C*D*G/Kd**2 + C*E*G/Kd**2 + C*F*G/Kd**2 + C*G*H/Kd**2 + C*G*I/Kd**2 + C*G/Kd + D*E*G/Kd**2 + D*F*G/Kd**2 + D*G*H/Kd**2 + D*G*I/Kd**2 + D*G/Kd + E*F*G/Kd**2 + E*G*H/Kd**2 + E*G*I/Kd**2 + E*G/Kd + F*G*H/Kd**2 + F*G*I/Kd**2 + F*G/Kd + G*H*I/Kd**2 + G*H/Kd + G*I/Kd + G - G_tot) / G_tot
    result[8] = (A*B*C/Kd**2 + A*C*D/Kd**2 + A*C*E/Kd**2 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C*H/Kd**2 + A*C*I/Kd**2 + A*C/Kd + B*C*D/Kd**2 + B*C*E/Kd**2 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C*H/Kd**2 + B*C*I/Kd**2 + B*C/Kd + C*D*E/Kd**2 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D*H/Kd**2 + C*D*I/Kd**2 + C*D/Kd + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E*H/Kd**2 + C*E*I/Kd**2 + C*E/Kd + C*F*G/Kd**2 + C*F*H/Kd**2 + C*F*I/Kd**2 + C*F/Kd + C*G*H/Kd**2 + C*G*I/Kd**2 + C*G/Kd + C*H*I/Kd**2 + C*H/Kd + C*I/Kd + C - C_tot) / C_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.F = solution[0]
    state.B = solution[1]
    state.I = solution[2]
    state.A = solution[3]
    state.E = solution[4]
    state.D = solution[5]
    state.H = solution[6]
    state.G = solution[7]
    state.C = solution[8]

    # Readability 
    A = state.A
    B = state.B
    C = state.C
    D = state.D
    E = state.E
    F = state.F
    G = state.G
    H = state.H
    I = state.I
    Kd = state.Kd

    # Dependent variables
    state.AB = A*B/Kd
    state.AC = A*C/Kd
    state.AD = A*D/Kd
    state.AE = A*E/Kd
    state.AF = A*F/Kd
    state.AG = A*G/Kd
    state.AH = A*H/Kd
    state.AI = A*I/Kd
    state.BC = B*C/Kd
    state.BD = B*D/Kd
    state.BE = B*E/Kd
    state.BF = B*F/Kd
    state.BG = B*G/Kd
    state.BH = B*H/Kd
    state.BI = B*I/Kd
    state.CD = C*D/Kd
    state.CE = C*E/Kd
    state.CF = C*F/Kd
    state.CG = C*G/Kd
    state.CH = C*H/Kd
    state.CI = C*I/Kd
    state.DE = D*E/Kd
    state.DF = D*F/Kd
    state.DG = D*G/Kd
    state.DH = D*H/Kd
    state.DI = D*I/Kd
    state.EF = E*F/Kd
    state.EG = E*G/Kd
    state.EH = E*H/Kd
    state.EI = E*I/Kd
    state.FG = F*G/Kd
    state.FH = F*H/Kd
    state.FI = F*I/Kd
    state.GH = G*H/Kd
    state.GI = G*I/Kd
    state.HI = H*I/Kd
    state.ABC = A*B*C/Kd**2
    state.ABD = A*B*D/Kd**2
    state.ABE = A*B*E/Kd**2
    state.ABF = A*B*F/Kd**2
    state.ABG = A*B*G/Kd**2
    state.ABH = A*B*H/Kd**2
    state.ABI = A*B*I/Kd**2
    state.ACD = A*C*D/Kd**2
    state.ACE = A*C*E/Kd**2
    state.ACF = A*C*F/Kd**2
    state.ACG = A*C*G/Kd**2
    state.ACH = A*C*H/Kd**2
    state.ACI = A*C*I/Kd**2
    state.ADE = A*D*E/Kd**2
    state.ADF = A*D*F/Kd**2
    state.ADG = A*D*G/Kd**2
    state.ADH = A*D*H/Kd**2
    state.ADI = A*D*I/Kd**2
    state.AEF = A*E*F/Kd**2
    state.AEG = A*E*G/Kd**2
    state.AEH = A*E*H/Kd**2
    state.AEI = A*E*I/Kd**2
    state.AFG = A*F*G/Kd**2
    state.AFH = A*F*H/Kd**2
    state.AFI = A*F*I/Kd**2
    state.AGH = A*G*H/Kd**2
    state.AGI = A*G*I/Kd**2
    state.AHI = A*H*I/Kd**2
    state.BCD = B*C*D/Kd**2
    state.BCE = B*C*E/Kd**2
    state.BCF = B*C*F/Kd**2
    state.BCG = B*C*G/Kd**2
    state.BCH = B*C*H/Kd**2
    state.BCI = B*C*I/Kd**2
    state.BDE = B*D*E/Kd**2
    state.BDF = B*D*F/Kd**2
    state.BDG = B*D*G/Kd**2
    state.BDH = B*D*H/Kd**2
    state.BDI = B*D*I/Kd**2
    state.BEF = B*E*F/Kd**2
    state.BEG = B*E*G/Kd**2
    state.BEH = B*E*H/Kd**2
    state.BEI = B*E*I/Kd**2
    state.BFG = B*F*G/Kd**2
    state.BFH = B*F*H/Kd**2
    state.BFI = B*F*I/Kd**2
    state.BGH = B*G*H/Kd**2
    state.BGI = B*G*I/Kd**2
    state.BHI = B*H*I/Kd**2
    state.CDE = C*D*E/Kd**2
    state.CDF = C*D*F/Kd**2
    state.CDG = C*D*G/Kd**2
    state.CDH = C*D*H/Kd**2
    state.CDI = C*D*I/Kd**2
    state.CEF = C*E*F/Kd**2
    state.CEG = C*E*G/Kd**2
    state.CEH = C*E*H/Kd**2
    state.CEI = C*E*I/Kd**2
    state.CFG = C*F*G/Kd**2
    state.CFH = C*F*H/Kd**2
    state.CFI = C*F*I/Kd**2
    state.CGH = C*G*H/Kd**2
    state.CGI = C*G*I/Kd**2
    state.CHI = C*H*I/Kd**2
    state.DEF = D*E*F/Kd**2
    state.DEG = D*E*G/Kd**2
    state.DEH = D*E*H/Kd**2
    state.DEI = D*E*I/Kd**2
    state.DFG = D*F*G/Kd**2
    state.DFH = D*F*H/Kd**2
    state.DFI = D*F*I/Kd**2
    state.DGH = D*G*H/Kd**2
    state.DGI = D*G*I/Kd**2
    state.DHI = D*H*I/Kd**2
    state.EFG = E*F*G/Kd**2
    state.EFH = E*F*H/Kd**2
    state.EFI = E*F*I/Kd**2
    state.EGH = E*G*H/Kd**2
    state.EGI = E*G*I/Kd**2
    state.EHI = E*H*I/Kd**2
    state.FGH = F*G*H/Kd**2
    state.FGI = F*G*I/Kd**2
    state.FHI = F*H*I/Kd**2
    state.GHI = G*H*I/Kd**2


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
    ABI = state.ABI
    AC = state.AC
    ACD = state.ACD
    ACE = state.ACE
    ACF = state.ACF
    ACG = state.ACG
    ACH = state.ACH
    ACI = state.ACI
    AD = state.AD
    ADE = state.ADE
    ADF = state.ADF
    ADG = state.ADG
    ADH = state.ADH
    ADI = state.ADI
    AE = state.AE
    AEF = state.AEF
    AEG = state.AEG
    AEH = state.AEH
    AEI = state.AEI
    AF = state.AF
    AFG = state.AFG
    AFH = state.AFH
    AFI = state.AFI
    AG = state.AG
    AGH = state.AGH
    AGI = state.AGI
    AH = state.AH
    AHI = state.AHI
    AI = state.AI
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABD + ABE + ABF + ABG + ABH + ABI + AC + ACD + ACE + ACF + ACG + ACH + ACI + AD + ADE + ADF + ADG + ADH + ADI + AE + AEF + AEG + AEH + AEI + AF + AFG + AFH + AFI + AG + AGH + AGI + AH + AHI + AI)/A_tot


