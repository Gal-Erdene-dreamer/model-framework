"""
Model file created on 2021-08-20 14:02:23.206104 
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
ABC + D = ABCD; Kd
ABC + E = ABCE; Kd
ABC + F = ABCF; Kd
ABC + G = ABCG; Kd
ABC + H = ABCH; Kd
ABD + E = ABDE; Kd
ABD + F = ABDF; Kd
ABD + G = ABDG; Kd
ABD + H = ABDH; Kd
ABE + F = ABEF; Kd
ABE + G = ABEG; Kd
ABE + H = ABEH; Kd
ABF + G = ABFG; Kd
ABF + H = ABFH; Kd
ABG + H = ABGH; Kd
ACD + E = ACDE; Kd
ACD + F = ACDF; Kd
ACD + G = ACDG; Kd
ACD + H = ACDH; Kd
ACE + F = ACEF; Kd
ACE + G = ACEG; Kd
ACE + H = ACEH; Kd
ACF + G = ACFG; Kd
ACF + H = ACFH; Kd
ACG + H = ACGH; Kd
ADE + F = ADEF; Kd
ADE + G = ADEG; Kd
ADE + H = ADEH; Kd
ADF + G = ADFG; Kd
ADF + H = ADFH; Kd
ADG + H = ADGH; Kd
AEF + G = AEFG; Kd
AEF + H = AEFH; Kd
AEG + H = AEGH; Kd
AFG + H = AFGH; Kd
BCD + E = BCDE; Kd
BCD + F = BCDF; Kd
BCD + G = BCDG; Kd
BCD + H = BCDH; Kd
BCE + F = BCEF; Kd
BCE + G = BCEG; Kd
BCE + H = BCEH; Kd
BCF + G = BCFG; Kd
BCF + H = BCFH; Kd
BCG + H = BCGH; Kd
BDE + F = BDEF; Kd
BDE + G = BDEG; Kd
BDE + H = BDEH; Kd
BDF + G = BDFG; Kd
BDF + H = BDFH; Kd
BDG + H = BDGH; Kd
BEF + G = BEFG; Kd
BEF + H = BEFH; Kd
BEG + H = BEGH; Kd
BFG + H = BFGH; Kd
CDE + F = CDEF; Kd
CDE + G = CDEG; Kd
CDE + H = CDEH; Kd
CDF + G = CDFG; Kd
CDF + H = CDFH; Kd
CDG + H = CDGH; Kd
CEF + G = CEFG; Kd
CEF + H = CEFH; Kd
CEG + H = CEGH; Kd
CFG + H = CFGH; Kd
DEF + G = DEFG; Kd
DEF + H = DEFH; Kd
DEG + H = DEGH; Kd
DFG + H = DFGH; Kd
EFG + H = EFGH; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['CDH', 'ACH', 'ADGH', 'EFH', 'DEFG', 'CDEF', 'CDF', 'ADF', 'BC', 'ADEF', 'F', 'DFGH', 'ACEF', 'ADFH', 'ABCE', 'CDGH', 'ABCD', 'ACEG', 'CEH', 'GH', 'ADFG', 'ABCG', 'DH', 'CDEG', 'ACE', 'CDG', 'CDFG', 'BCH', 'BDEH', 'BCFG', 'CF', 'BDE', 'ACD', 'CEGH', 'BEFG', 'AEFH', 'ACFG', 'CEFH', 'AEFG', 'BDEG', 'BDGH', 'CEFG', 'BDG', 'FG', 'BF', 'B', 'BEF', 'AC', 'AEH', 'ABEH', 'BCEH', 'ABGH', 'ADEH', 'BDFH', 'BCEG', 'BEH', 'CD', 'AG', 'ACDE', 'DGH', 'BEG', 'BCF', 'ABFG', 'ACEH', 'DFG', 'CFH', 'BDF', 'ABDH', 'DEFH', 'BCE', 'AFGH', 'BFG', 'EFG', 'CFG', 'EF', 'BGH', 'BCD', 'BCDG', 'AF', 'BEGH', 'ABG', 'CEG', 'BEFH', 'A', 'ACG', 'ADG', 'ACDH', 'DE', 'E', 'AEF', 'D', 'EGH', 'CEF', 'DF', 'ACFH', 'ABC', 'BH', 'BCDE', 'ABDG', 'ABH', 'AFG', 'BCG', 'BFGH', 'ABD', 'BCFH', 'BCGH', 'H', 'BE', 'Kd', 'AE', 'CG', 'ACDG', 'BDEF', 'BDH', 'ABEF', 'EFGH', 'AEGH', 'BDFG', 'CE', 'CH', 'BG', 'DG', 'FH', 'CDEH', 'AFH', 'ADH', 'DEH', 'AD', 'AB', 'ADE', 'ABDE', 'BCDH', 'ABCF', 'ABF', 'ABEG', 'G', 'DEG', 'ACDF', 'CGH', 'DFH', 'EG', 'ABFH', 'ADEG', 'ABE', 'EH', 'CDFH', 'BCEF', 'ACF', 'AH', 'AEG', 'FGH', 'CFGH', 'AGH', 'BCDF', 'ABCH', 'DEF', 'ABDF', 'CDE', 'BFH', 'ACGH', 'DEGH', 'C', 'BD', 'B_tot', 'F_tot', 'G_tot', 'A_tot', 'E_tot', 'D_tot', 'H_tot', 'C_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['B', 'F', 'G', 'A', 'E', 'D', 'H', 'C']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'CD', 'CE', 'CF', 'CG', 'CH', 'DE', 'DF', 'DG', 'DH', 'EF', 'EG', 'EH', 'FG', 'FH', 'GH', 'ABC', 'ABD', 'ABE', 'ABF', 'ABG', 'ABH', 'ACD', 'ACE', 'ACF', 'ACG', 'ACH', 'ADE', 'ADF', 'ADG', 'ADH', 'AEF', 'AEG', 'AEH', 'AFG', 'AFH', 'AGH', 'BCD', 'BCE', 'BCF', 'BCG', 'BCH', 'BDE', 'BDF', 'BDG', 'BDH', 'BEF', 'BEG', 'BEH', 'BFG', 'BFH', 'BGH', 'CDE', 'CDF', 'CDG', 'CDH', 'CEF', 'CEG', 'CEH', 'CFG', 'CFH', 'CGH', 'DEF', 'DEG', 'DEH', 'DFG', 'DFH', 'DGH', 'EFG', 'EFH', 'EGH', 'FGH', 'ABCD', 'ABCE', 'ABCF', 'ABCG', 'ABCH', 'ABDE', 'ABDF', 'ABDG', 'ABDH', 'ABEF', 'ABEG', 'ABEH', 'ABFG', 'ABFH', 'ABGH', 'ACDE', 'ACDF', 'ACDG', 'ACDH', 'ACEF', 'ACEG', 'ACEH', 'ACFG', 'ACFH', 'ACGH', 'ADEF', 'ADEG', 'ADEH', 'ADFG', 'ADFH', 'ADGH', 'AEFG', 'AEFH', 'AEGH', 'AFGH', 'BCDE', 'BCDF', 'BCDG', 'BCDH', 'BCEF', 'BCEG', 'BCEH', 'BCFG', 'BCFH', 'BCGH', 'BDEF', 'BDEG', 'BDEH', 'BDFG', 'BDFH', 'BDGH', 'BEFG', 'BEFH', 'BEGH', 'BFGH', 'CDEF', 'CDEG', 'CDEH', 'CDFG', 'CDFH', 'CDGH', 'CEFG', 'CEFH', 'CEGH', 'CFGH', 'DEFG', 'DEFH', 'DEGH', 'DFGH', 'EFGH']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ACH', 'ADGH', 'ADF', 'ADEF', 'ACEF', 'ADFH', 'ABCE', 'ABCD', 'ACEG', 'ADFG', 'ABCG', 'ACE', 'ACD', 'AEFH', 'ACFG', 'AEFG', 'AC', 'AEH', 'ABEH', 'ABGH', 'ADEH', 'AG', 'ACDE', 'ABFG', 'ACEH', 'ABDH', 'AFGH', 'AF', 'ABG', 'A', 'ACG', 'ADG', 'ACDH', 'AEF', 'ACFH', 'ABC', 'ABDG', 'ABH', 'AFG', 'ABD', 'AE', 'ACDG', 'ABEF', 'AEGH', 'AFH', 'ADH', 'AD', 'AB', 'ADE', 'ABDE', 'ABCF', 'ABF', 'ABEG', 'ACDF', 'ABFH', 'ADEG', 'ABE', 'ACF', 'AH', 'AEG', 'AGH', 'ABCH', 'ABDF', 'ACGH'] 

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
    result[0] = (A*B*C*D/Kd**3 + A*B*C*E/Kd**3 + A*B*C*F/Kd**3 + A*B*C*G/Kd**3 + A*B*C*H/Kd**3 + A*B*C/Kd**2 + A*B*D*E/Kd**3 + A*B*D*F/Kd**3 + A*B*D*G/Kd**3 + A*B*D*H/Kd**3 + A*B*D/Kd**2 + A*B*E*F/Kd**3 + A*B*E*G/Kd**3 + A*B*E*H/Kd**3 + A*B*E/Kd**2 + A*B*F*G/Kd**3 + A*B*F*H/Kd**3 + A*B*F/Kd**2 + A*B*G*H/Kd**3 + A*B*G/Kd**2 + A*B*H/Kd**2 + A*B/Kd + B*C*D*E/Kd**3 + B*C*D*F/Kd**3 + B*C*D*G/Kd**3 + B*C*D*H/Kd**3 + B*C*D/Kd**2 + B*C*E*F/Kd**3 + B*C*E*G/Kd**3 + B*C*E*H/Kd**3 + B*C*E/Kd**2 + B*C*F*G/Kd**3 + B*C*F*H/Kd**3 + B*C*F/Kd**2 + B*C*G*H/Kd**3 + B*C*G/Kd**2 + B*C*H/Kd**2 + B*C/Kd + B*D*E*F/Kd**3 + B*D*E*G/Kd**3 + B*D*E*H/Kd**3 + B*D*E/Kd**2 + B*D*F*G/Kd**3 + B*D*F*H/Kd**3 + B*D*F/Kd**2 + B*D*G*H/Kd**3 + B*D*G/Kd**2 + B*D*H/Kd**2 + B*D/Kd + B*E*F*G/Kd**3 + B*E*F*H/Kd**3 + B*E*F/Kd**2 + B*E*G*H/Kd**3 + B*E*G/Kd**2 + B*E*H/Kd**2 + B*E/Kd + B*F*G*H/Kd**3 + B*F*G/Kd**2 + B*F*H/Kd**2 + B*F/Kd + B*G*H/Kd**2 + B*G/Kd + B*H/Kd + B - B_tot) / B_tot
    result[1] = (A*B*C*F/Kd**3 + A*B*D*F/Kd**3 + A*B*E*F/Kd**3 + A*B*F*G/Kd**3 + A*B*F*H/Kd**3 + A*B*F/Kd**2 + A*C*D*F/Kd**3 + A*C*E*F/Kd**3 + A*C*F*G/Kd**3 + A*C*F*H/Kd**3 + A*C*F/Kd**2 + A*D*E*F/Kd**3 + A*D*F*G/Kd**3 + A*D*F*H/Kd**3 + A*D*F/Kd**2 + A*E*F*G/Kd**3 + A*E*F*H/Kd**3 + A*E*F/Kd**2 + A*F*G*H/Kd**3 + A*F*G/Kd**2 + A*F*H/Kd**2 + A*F/Kd + B*C*D*F/Kd**3 + B*C*E*F/Kd**3 + B*C*F*G/Kd**3 + B*C*F*H/Kd**3 + B*C*F/Kd**2 + B*D*E*F/Kd**3 + B*D*F*G/Kd**3 + B*D*F*H/Kd**3 + B*D*F/Kd**2 + B*E*F*G/Kd**3 + B*E*F*H/Kd**3 + B*E*F/Kd**2 + B*F*G*H/Kd**3 + B*F*G/Kd**2 + B*F*H/Kd**2 + B*F/Kd + C*D*E*F/Kd**3 + C*D*F*G/Kd**3 + C*D*F*H/Kd**3 + C*D*F/Kd**2 + C*E*F*G/Kd**3 + C*E*F*H/Kd**3 + C*E*F/Kd**2 + C*F*G*H/Kd**3 + C*F*G/Kd**2 + C*F*H/Kd**2 + C*F/Kd + D*E*F*G/Kd**3 + D*E*F*H/Kd**3 + D*E*F/Kd**2 + D*F*G*H/Kd**3 + D*F*G/Kd**2 + D*F*H/Kd**2 + D*F/Kd + E*F*G*H/Kd**3 + E*F*G/Kd**2 + E*F*H/Kd**2 + E*F/Kd + F*G*H/Kd**2 + F*G/Kd + F*H/Kd + F - F_tot) / F_tot
    result[2] = (A*B*C*G/Kd**3 + A*B*D*G/Kd**3 + A*B*E*G/Kd**3 + A*B*F*G/Kd**3 + A*B*G*H/Kd**3 + A*B*G/Kd**2 + A*C*D*G/Kd**3 + A*C*E*G/Kd**3 + A*C*F*G/Kd**3 + A*C*G*H/Kd**3 + A*C*G/Kd**2 + A*D*E*G/Kd**3 + A*D*F*G/Kd**3 + A*D*G*H/Kd**3 + A*D*G/Kd**2 + A*E*F*G/Kd**3 + A*E*G*H/Kd**3 + A*E*G/Kd**2 + A*F*G*H/Kd**3 + A*F*G/Kd**2 + A*G*H/Kd**2 + A*G/Kd + B*C*D*G/Kd**3 + B*C*E*G/Kd**3 + B*C*F*G/Kd**3 + B*C*G*H/Kd**3 + B*C*G/Kd**2 + B*D*E*G/Kd**3 + B*D*F*G/Kd**3 + B*D*G*H/Kd**3 + B*D*G/Kd**2 + B*E*F*G/Kd**3 + B*E*G*H/Kd**3 + B*E*G/Kd**2 + B*F*G*H/Kd**3 + B*F*G/Kd**2 + B*G*H/Kd**2 + B*G/Kd + C*D*E*G/Kd**3 + C*D*F*G/Kd**3 + C*D*G*H/Kd**3 + C*D*G/Kd**2 + C*E*F*G/Kd**3 + C*E*G*H/Kd**3 + C*E*G/Kd**2 + C*F*G*H/Kd**3 + C*F*G/Kd**2 + C*G*H/Kd**2 + C*G/Kd + D*E*F*G/Kd**3 + D*E*G*H/Kd**3 + D*E*G/Kd**2 + D*F*G*H/Kd**3 + D*F*G/Kd**2 + D*G*H/Kd**2 + D*G/Kd + E*F*G*H/Kd**3 + E*F*G/Kd**2 + E*G*H/Kd**2 + E*G/Kd + F*G*H/Kd**2 + F*G/Kd + G*H/Kd + G - G_tot) / G_tot
    result[3] = (A*B*C*D/Kd**3 + A*B*C*E/Kd**3 + A*B*C*F/Kd**3 + A*B*C*G/Kd**3 + A*B*C*H/Kd**3 + A*B*C/Kd**2 + A*B*D*E/Kd**3 + A*B*D*F/Kd**3 + A*B*D*G/Kd**3 + A*B*D*H/Kd**3 + A*B*D/Kd**2 + A*B*E*F/Kd**3 + A*B*E*G/Kd**3 + A*B*E*H/Kd**3 + A*B*E/Kd**2 + A*B*F*G/Kd**3 + A*B*F*H/Kd**3 + A*B*F/Kd**2 + A*B*G*H/Kd**3 + A*B*G/Kd**2 + A*B*H/Kd**2 + A*B/Kd + A*C*D*E/Kd**3 + A*C*D*F/Kd**3 + A*C*D*G/Kd**3 + A*C*D*H/Kd**3 + A*C*D/Kd**2 + A*C*E*F/Kd**3 + A*C*E*G/Kd**3 + A*C*E*H/Kd**3 + A*C*E/Kd**2 + A*C*F*G/Kd**3 + A*C*F*H/Kd**3 + A*C*F/Kd**2 + A*C*G*H/Kd**3 + A*C*G/Kd**2 + A*C*H/Kd**2 + A*C/Kd + A*D*E*F/Kd**3 + A*D*E*G/Kd**3 + A*D*E*H/Kd**3 + A*D*E/Kd**2 + A*D*F*G/Kd**3 + A*D*F*H/Kd**3 + A*D*F/Kd**2 + A*D*G*H/Kd**3 + A*D*G/Kd**2 + A*D*H/Kd**2 + A*D/Kd + A*E*F*G/Kd**3 + A*E*F*H/Kd**3 + A*E*F/Kd**2 + A*E*G*H/Kd**3 + A*E*G/Kd**2 + A*E*H/Kd**2 + A*E/Kd + A*F*G*H/Kd**3 + A*F*G/Kd**2 + A*F*H/Kd**2 + A*F/Kd + A*G*H/Kd**2 + A*G/Kd + A*H/Kd + A - A_tot) / A_tot
    result[4] = (A*B*C*E/Kd**3 + A*B*D*E/Kd**3 + A*B*E*F/Kd**3 + A*B*E*G/Kd**3 + A*B*E*H/Kd**3 + A*B*E/Kd**2 + A*C*D*E/Kd**3 + A*C*E*F/Kd**3 + A*C*E*G/Kd**3 + A*C*E*H/Kd**3 + A*C*E/Kd**2 + A*D*E*F/Kd**3 + A*D*E*G/Kd**3 + A*D*E*H/Kd**3 + A*D*E/Kd**2 + A*E*F*G/Kd**3 + A*E*F*H/Kd**3 + A*E*F/Kd**2 + A*E*G*H/Kd**3 + A*E*G/Kd**2 + A*E*H/Kd**2 + A*E/Kd + B*C*D*E/Kd**3 + B*C*E*F/Kd**3 + B*C*E*G/Kd**3 + B*C*E*H/Kd**3 + B*C*E/Kd**2 + B*D*E*F/Kd**3 + B*D*E*G/Kd**3 + B*D*E*H/Kd**3 + B*D*E/Kd**2 + B*E*F*G/Kd**3 + B*E*F*H/Kd**3 + B*E*F/Kd**2 + B*E*G*H/Kd**3 + B*E*G/Kd**2 + B*E*H/Kd**2 + B*E/Kd + C*D*E*F/Kd**3 + C*D*E*G/Kd**3 + C*D*E*H/Kd**3 + C*D*E/Kd**2 + C*E*F*G/Kd**3 + C*E*F*H/Kd**3 + C*E*F/Kd**2 + C*E*G*H/Kd**3 + C*E*G/Kd**2 + C*E*H/Kd**2 + C*E/Kd + D*E*F*G/Kd**3 + D*E*F*H/Kd**3 + D*E*F/Kd**2 + D*E*G*H/Kd**3 + D*E*G/Kd**2 + D*E*H/Kd**2 + D*E/Kd + E*F*G*H/Kd**3 + E*F*G/Kd**2 + E*F*H/Kd**2 + E*F/Kd + E*G*H/Kd**2 + E*G/Kd + E*H/Kd + E - E_tot) / E_tot
    result[5] = (A*B*C*D/Kd**3 + A*B*D*E/Kd**3 + A*B*D*F/Kd**3 + A*B*D*G/Kd**3 + A*B*D*H/Kd**3 + A*B*D/Kd**2 + A*C*D*E/Kd**3 + A*C*D*F/Kd**3 + A*C*D*G/Kd**3 + A*C*D*H/Kd**3 + A*C*D/Kd**2 + A*D*E*F/Kd**3 + A*D*E*G/Kd**3 + A*D*E*H/Kd**3 + A*D*E/Kd**2 + A*D*F*G/Kd**3 + A*D*F*H/Kd**3 + A*D*F/Kd**2 + A*D*G*H/Kd**3 + A*D*G/Kd**2 + A*D*H/Kd**2 + A*D/Kd + B*C*D*E/Kd**3 + B*C*D*F/Kd**3 + B*C*D*G/Kd**3 + B*C*D*H/Kd**3 + B*C*D/Kd**2 + B*D*E*F/Kd**3 + B*D*E*G/Kd**3 + B*D*E*H/Kd**3 + B*D*E/Kd**2 + B*D*F*G/Kd**3 + B*D*F*H/Kd**3 + B*D*F/Kd**2 + B*D*G*H/Kd**3 + B*D*G/Kd**2 + B*D*H/Kd**2 + B*D/Kd + C*D*E*F/Kd**3 + C*D*E*G/Kd**3 + C*D*E*H/Kd**3 + C*D*E/Kd**2 + C*D*F*G/Kd**3 + C*D*F*H/Kd**3 + C*D*F/Kd**2 + C*D*G*H/Kd**3 + C*D*G/Kd**2 + C*D*H/Kd**2 + C*D/Kd + D*E*F*G/Kd**3 + D*E*F*H/Kd**3 + D*E*F/Kd**2 + D*E*G*H/Kd**3 + D*E*G/Kd**2 + D*E*H/Kd**2 + D*E/Kd + D*F*G*H/Kd**3 + D*F*G/Kd**2 + D*F*H/Kd**2 + D*F/Kd + D*G*H/Kd**2 + D*G/Kd + D*H/Kd + D - D_tot) / D_tot
    result[6] = (A*B*C*H/Kd**3 + A*B*D*H/Kd**3 + A*B*E*H/Kd**3 + A*B*F*H/Kd**3 + A*B*G*H/Kd**3 + A*B*H/Kd**2 + A*C*D*H/Kd**3 + A*C*E*H/Kd**3 + A*C*F*H/Kd**3 + A*C*G*H/Kd**3 + A*C*H/Kd**2 + A*D*E*H/Kd**3 + A*D*F*H/Kd**3 + A*D*G*H/Kd**3 + A*D*H/Kd**2 + A*E*F*H/Kd**3 + A*E*G*H/Kd**3 + A*E*H/Kd**2 + A*F*G*H/Kd**3 + A*F*H/Kd**2 + A*G*H/Kd**2 + A*H/Kd + B*C*D*H/Kd**3 + B*C*E*H/Kd**3 + B*C*F*H/Kd**3 + B*C*G*H/Kd**3 + B*C*H/Kd**2 + B*D*E*H/Kd**3 + B*D*F*H/Kd**3 + B*D*G*H/Kd**3 + B*D*H/Kd**2 + B*E*F*H/Kd**3 + B*E*G*H/Kd**3 + B*E*H/Kd**2 + B*F*G*H/Kd**3 + B*F*H/Kd**2 + B*G*H/Kd**2 + B*H/Kd + C*D*E*H/Kd**3 + C*D*F*H/Kd**3 + C*D*G*H/Kd**3 + C*D*H/Kd**2 + C*E*F*H/Kd**3 + C*E*G*H/Kd**3 + C*E*H/Kd**2 + C*F*G*H/Kd**3 + C*F*H/Kd**2 + C*G*H/Kd**2 + C*H/Kd + D*E*F*H/Kd**3 + D*E*G*H/Kd**3 + D*E*H/Kd**2 + D*F*G*H/Kd**3 + D*F*H/Kd**2 + D*G*H/Kd**2 + D*H/Kd + E*F*G*H/Kd**3 + E*F*H/Kd**2 + E*G*H/Kd**2 + E*H/Kd + F*G*H/Kd**2 + F*H/Kd + G*H/Kd + H - H_tot) / H_tot
    result[7] = (A*B*C*D/Kd**3 + A*B*C*E/Kd**3 + A*B*C*F/Kd**3 + A*B*C*G/Kd**3 + A*B*C*H/Kd**3 + A*B*C/Kd**2 + A*C*D*E/Kd**3 + A*C*D*F/Kd**3 + A*C*D*G/Kd**3 + A*C*D*H/Kd**3 + A*C*D/Kd**2 + A*C*E*F/Kd**3 + A*C*E*G/Kd**3 + A*C*E*H/Kd**3 + A*C*E/Kd**2 + A*C*F*G/Kd**3 + A*C*F*H/Kd**3 + A*C*F/Kd**2 + A*C*G*H/Kd**3 + A*C*G/Kd**2 + A*C*H/Kd**2 + A*C/Kd + B*C*D*E/Kd**3 + B*C*D*F/Kd**3 + B*C*D*G/Kd**3 + B*C*D*H/Kd**3 + B*C*D/Kd**2 + B*C*E*F/Kd**3 + B*C*E*G/Kd**3 + B*C*E*H/Kd**3 + B*C*E/Kd**2 + B*C*F*G/Kd**3 + B*C*F*H/Kd**3 + B*C*F/Kd**2 + B*C*G*H/Kd**3 + B*C*G/Kd**2 + B*C*H/Kd**2 + B*C/Kd + C*D*E*F/Kd**3 + C*D*E*G/Kd**3 + C*D*E*H/Kd**3 + C*D*E/Kd**2 + C*D*F*G/Kd**3 + C*D*F*H/Kd**3 + C*D*F/Kd**2 + C*D*G*H/Kd**3 + C*D*G/Kd**2 + C*D*H/Kd**2 + C*D/Kd + C*E*F*G/Kd**3 + C*E*F*H/Kd**3 + C*E*F/Kd**2 + C*E*G*H/Kd**3 + C*E*G/Kd**2 + C*E*H/Kd**2 + C*E/Kd + C*F*G*H/Kd**3 + C*F*G/Kd**2 + C*F*H/Kd**2 + C*F/Kd + C*G*H/Kd**2 + C*G/Kd + C*H/Kd + C - C_tot) / C_tot
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
    state.ABCD = A*B*C*D/Kd**3
    state.ABCE = A*B*C*E/Kd**3
    state.ABCF = A*B*C*F/Kd**3
    state.ABCG = A*B*C*G/Kd**3
    state.ABCH = A*B*C*H/Kd**3
    state.ABDE = A*B*D*E/Kd**3
    state.ABDF = A*B*D*F/Kd**3
    state.ABDG = A*B*D*G/Kd**3
    state.ABDH = A*B*D*H/Kd**3
    state.ABEF = A*B*E*F/Kd**3
    state.ABEG = A*B*E*G/Kd**3
    state.ABEH = A*B*E*H/Kd**3
    state.ABFG = A*B*F*G/Kd**3
    state.ABFH = A*B*F*H/Kd**3
    state.ABGH = A*B*G*H/Kd**3
    state.ACDE = A*C*D*E/Kd**3
    state.ACDF = A*C*D*F/Kd**3
    state.ACDG = A*C*D*G/Kd**3
    state.ACDH = A*C*D*H/Kd**3
    state.ACEF = A*C*E*F/Kd**3
    state.ACEG = A*C*E*G/Kd**3
    state.ACEH = A*C*E*H/Kd**3
    state.ACFG = A*C*F*G/Kd**3
    state.ACFH = A*C*F*H/Kd**3
    state.ACGH = A*C*G*H/Kd**3
    state.ADEF = A*D*E*F/Kd**3
    state.ADEG = A*D*E*G/Kd**3
    state.ADEH = A*D*E*H/Kd**3
    state.ADFG = A*D*F*G/Kd**3
    state.ADFH = A*D*F*H/Kd**3
    state.ADGH = A*D*G*H/Kd**3
    state.AEFG = A*E*F*G/Kd**3
    state.AEFH = A*E*F*H/Kd**3
    state.AEGH = A*E*G*H/Kd**3
    state.AFGH = A*F*G*H/Kd**3
    state.BCDE = B*C*D*E/Kd**3
    state.BCDF = B*C*D*F/Kd**3
    state.BCDG = B*C*D*G/Kd**3
    state.BCDH = B*C*D*H/Kd**3
    state.BCEF = B*C*E*F/Kd**3
    state.BCEG = B*C*E*G/Kd**3
    state.BCEH = B*C*E*H/Kd**3
    state.BCFG = B*C*F*G/Kd**3
    state.BCFH = B*C*F*H/Kd**3
    state.BCGH = B*C*G*H/Kd**3
    state.BDEF = B*D*E*F/Kd**3
    state.BDEG = B*D*E*G/Kd**3
    state.BDEH = B*D*E*H/Kd**3
    state.BDFG = B*D*F*G/Kd**3
    state.BDFH = B*D*F*H/Kd**3
    state.BDGH = B*D*G*H/Kd**3
    state.BEFG = B*E*F*G/Kd**3
    state.BEFH = B*E*F*H/Kd**3
    state.BEGH = B*E*G*H/Kd**3
    state.BFGH = B*F*G*H/Kd**3
    state.CDEF = C*D*E*F/Kd**3
    state.CDEG = C*D*E*G/Kd**3
    state.CDEH = C*D*E*H/Kd**3
    state.CDFG = C*D*F*G/Kd**3
    state.CDFH = C*D*F*H/Kd**3
    state.CDGH = C*D*G*H/Kd**3
    state.CEFG = C*E*F*G/Kd**3
    state.CEFH = C*E*F*H/Kd**3
    state.CEGH = C*E*G*H/Kd**3
    state.CFGH = C*F*G*H/Kd**3
    state.DEFG = D*E*F*G/Kd**3
    state.DEFH = D*E*F*H/Kd**3
    state.DEGH = D*E*G*H/Kd**3
    state.DFGH = D*F*G*H/Kd**3
    state.EFGH = E*F*G*H/Kd**3


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
    ABCF = state.ABCF
    ABCG = state.ABCG
    ABCH = state.ABCH
    ABD = state.ABD
    ABDE = state.ABDE
    ABDF = state.ABDF
    ABDG = state.ABDG
    ABDH = state.ABDH
    ABE = state.ABE
    ABEF = state.ABEF
    ABEG = state.ABEG
    ABEH = state.ABEH
    ABF = state.ABF
    ABFG = state.ABFG
    ABFH = state.ABFH
    ABG = state.ABG
    ABGH = state.ABGH
    ABH = state.ABH
    AC = state.AC
    ACD = state.ACD
    ACDE = state.ACDE
    ACDF = state.ACDF
    ACDG = state.ACDG
    ACDH = state.ACDH
    ACE = state.ACE
    ACEF = state.ACEF
    ACEG = state.ACEG
    ACEH = state.ACEH
    ACF = state.ACF
    ACFG = state.ACFG
    ACFH = state.ACFH
    ACG = state.ACG
    ACGH = state.ACGH
    ACH = state.ACH
    AD = state.AD
    ADE = state.ADE
    ADEF = state.ADEF
    ADEG = state.ADEG
    ADEH = state.ADEH
    ADF = state.ADF
    ADFG = state.ADFG
    ADFH = state.ADFH
    ADG = state.ADG
    ADGH = state.ADGH
    ADH = state.ADH
    AE = state.AE
    AEF = state.AEF
    AEFG = state.AEFG
    AEFH = state.AEFH
    AEG = state.AEG
    AEGH = state.AEGH
    AEH = state.AEH
    AF = state.AF
    AFG = state.AFG
    AFGH = state.AFGH
    AFH = state.AFH
    AG = state.AG
    AGH = state.AGH
    AH = state.AH
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABCD + ABCE + ABCF + ABCG + ABCH + ABD + ABDE + ABDF + ABDG + ABDH + ABE + ABEF + ABEG + ABEH + ABF + ABFG + ABFH + ABG + ABGH + ABH + AC + ACD + ACDE + ACDF + ACDG + ACDH + ACE + ACEF + ACEG + ACEH + ACF + ACFG + ACFH + ACG + ACGH + ACH + AD + ADE + ADEF + ADEG + ADEH + ADF + ADFG + ADFH + ADG + ADGH + ADH + AE + AEF + AEFG + AEFH + AEG + AEGH + AEH + AF + AFG + AFGH + AFH + AG + AGH + AH)/A_tot


