"""
Model file created on 2021-08-20 14:00:55.694133 
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
ABC + D = ABCD; Kd
ABC + E = ABCE; Kd
ABC + F = ABCF; Kd
ABC + G = ABCG; Kd
ABD + E = ABDE; Kd
ABD + F = ABDF; Kd
ABD + G = ABDG; Kd
ABE + F = ABEF; Kd
ABE + G = ABEG; Kd
ABF + G = ABFG; Kd
ACD + E = ACDE; Kd
ACD + F = ACDF; Kd
ACD + G = ACDG; Kd
ACE + F = ACEF; Kd
ACE + G = ACEG; Kd
ACF + G = ACFG; Kd
ADE + F = ADEF; Kd
ADE + G = ADEG; Kd
ADF + G = ADFG; Kd
AEF + G = AEFG; Kd
BCD + E = BCDE; Kd
BCD + F = BCDF; Kd
BCD + G = BCDG; Kd
BCE + F = BCEF; Kd
BCE + G = BCEG; Kd
BCF + G = BCFG; Kd
BDE + F = BDEF; Kd
BDE + G = BDEG; Kd
BDF + G = BDFG; Kd
BEF + G = BEFG; Kd
CDE + F = CDEF; Kd
CDE + G = CDEG; Kd
CDF + G = CDFG; Kd
CEF + G = CEFG; Kd
DEF + G = DEFG; Kd
ABCD + E = ABCDE; Kd
ABCD + F = ABCDF; Kd
ABCD + G = ABCDG; Kd
ABCE + F = ABCEF; Kd
ABCE + G = ABCEG; Kd
ABCF + G = ABCFG; Kd
ABDE + F = ABDEF; Kd
ABDE + G = ABDEG; Kd
ABDF + G = ABDFG; Kd
ABEF + G = ABEFG; Kd
ACDE + F = ACDEF; Kd
ACDE + G = ACDEG; Kd
ACDF + G = ACDFG; Kd
ACEF + G = ACEFG; Kd
ADEF + G = ADEFG; Kd
BCDE + F = BCDEF; Kd
BCDE + G = BCDEG; Kd
BCDF + G = BCDFG; Kd
BCEF + G = BCEFG; Kd
BDEF + G = BDEFG; Kd
CDEF + G = CDEFG; Kd

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['ABC', 'DEFG', 'ABDEG', 'CDEF', 'CDF', 'ABDG', 'ADF', 'BC', 'BCDE', 'ADEF', 'ACEFG', 'F', 'AFG', 'BCG', 'ABCDG', 'ACEF', 'ABCE', 'ABD', 'BE', 'ABCD', 'Kd', 'ACEG', 'ADFG', 'AE', 'ABCG', 'CG', 'CDEG', 'ACE', 'CDG', 'ACDFG', 'CDFG', 'ACDG', 'BDEF', 'BCFG', 'CF', 'ABEF', 'BDFG', 'CE', 'BDE', 'ACD', 'BEFG', 'BG', 'ACDEF', 'BCEFG', 'BDEFG', 'ACFG', 'BCDFG', 'AEFG', 'BDEG', 'ABEFG', 'DG', 'BCDEF', 'CEFG', 'BDG', 'FG', 'ABCDF', 'AD', 'BF', 'ABCEF', 'ABCFG', 'B', 'ABDFG', 'BEF', 'AB', 'AC', 'ADE', 'ABDE', 'ADEFG', 'ABCF', 'ABF', 'ABDEF', 'ABEG', 'BCEG', 'G', 'CD', 'AG', 'ACDE', 'ACDEG', 'BEG', 'BCF', 'ABFG', 'DEG', 'DFG', 'ACDF', 'BDF', 'BCE', 'EG', 'ABCEG', 'BFG', 'EFG', 'ABE', 'ADEG', 'CFG', 'ABCDE', 'BCEF', 'EF', 'ACF', 'BCD', 'AEG', 'AF', 'BCDG', 'ABG', 'CEG', 'BCDF', 'A', 'ACG', 'ADG', 'CDEFG', 'DEF', 'DE', 'E', 'ABDF', 'CDE', 'AEF', 'D', 'BCDEG', 'CEF', 'DF', 'C', 'BD', 'C_tot', 'G_tot', 'A_tot', 'B_tot', 'E_tot', 'D_tot', 'F_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['C', 'G', 'A', 'B', 'E', 'D', 'F']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'BC', 'BD', 'BE', 'BF', 'BG', 'CD', 'CE', 'CF', 'CG', 'DE', 'DF', 'DG', 'EF', 'EG', 'FG', 'ABC', 'ABD', 'ABE', 'ABF', 'ABG', 'ACD', 'ACE', 'ACF', 'ACG', 'ADE', 'ADF', 'ADG', 'AEF', 'AEG', 'AFG', 'BCD', 'BCE', 'BCF', 'BCG', 'BDE', 'BDF', 'BDG', 'BEF', 'BEG', 'BFG', 'CDE', 'CDF', 'CDG', 'CEF', 'CEG', 'CFG', 'DEF', 'DEG', 'DFG', 'EFG', 'ABCD', 'ABCE', 'ABCF', 'ABCG', 'ABDE', 'ABDF', 'ABDG', 'ABEF', 'ABEG', 'ABFG', 'ACDE', 'ACDF', 'ACDG', 'ACEF', 'ACEG', 'ACFG', 'ADEF', 'ADEG', 'ADFG', 'AEFG', 'BCDE', 'BCDF', 'BCDG', 'BCEF', 'BCEG', 'BCFG', 'BDEF', 'BDEG', 'BDFG', 'BEFG', 'CDEF', 'CDEG', 'CDFG', 'CEFG', 'DEFG', 'ABCDE', 'ABCDF', 'ABCDG', 'ABCEF', 'ABCEG', 'ABCFG', 'ABDEF', 'ABDEG', 'ABDFG', 'ABEFG', 'ACDEF', 'ACDEG', 'ACDFG', 'ACEFG', 'ADEFG', 'BCDEF', 'BCDEG', 'BCDFG', 'BCEFG', 'BDEFG', 'CDEFG']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['ABC', 'ABDEG', 'ABDG', 'ADF', 'ADEF', 'ACEFG', 'AFG', 'ABCDG', 'ACEF', 'ABCE', 'ABD', 'ABCD', 'ACEG', 'ADFG', 'AE', 'ABCG', 'ACE', 'ACDFG', 'ACDG', 'ABEF', 'ACD', 'ACDEF', 'ACFG', 'AEFG', 'ABEFG', 'ABCDF', 'AD', 'ABCEF', 'ABCFG', 'ABDFG', 'AB', 'AC', 'ADE', 'ABDE', 'ADEFG', 'ABCF', 'ABF', 'ABDEF', 'ABEG', 'AG', 'ACDE', 'ACDEG', 'ABFG', 'ACDF', 'ABCEG', 'ABE', 'ADEG', 'ABCDE', 'ACF', 'AEG', 'AF', 'ABG', 'A', 'ACG', 'ADG', 'ABDF', 'AEF'] 

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
    result[0] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D*G/Kd**4 + A*B*C*D/Kd**3 + A*B*C*E*F/Kd**4 + A*B*C*E*G/Kd**4 + A*B*C*E/Kd**3 + A*B*C*F*G/Kd**4 + A*B*C*F/Kd**3 + A*B*C*G/Kd**3 + A*B*C/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*E*G/Kd**4 + A*C*D*E/Kd**3 + A*C*D*F*G/Kd**4 + A*C*D*F/Kd**3 + A*C*D*G/Kd**3 + A*C*D/Kd**2 + A*C*E*F*G/Kd**4 + A*C*E*F/Kd**3 + A*C*E*G/Kd**3 + A*C*E/Kd**2 + A*C*F*G/Kd**3 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C/Kd + B*C*D*E*F/Kd**4 + B*C*D*E*G/Kd**4 + B*C*D*E/Kd**3 + B*C*D*F*G/Kd**4 + B*C*D*F/Kd**3 + B*C*D*G/Kd**3 + B*C*D/Kd**2 + B*C*E*F*G/Kd**4 + B*C*E*F/Kd**3 + B*C*E*G/Kd**3 + B*C*E/Kd**2 + B*C*F*G/Kd**3 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C/Kd + C*D*E*F*G/Kd**4 + C*D*E*F/Kd**3 + C*D*E*G/Kd**3 + C*D*E/Kd**2 + C*D*F*G/Kd**3 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D/Kd + C*E*F*G/Kd**3 + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E/Kd + C*F*G/Kd**2 + C*F/Kd + C*G/Kd + C - C_tot) / C_tot
    result[1] = (A*B*C*D*G/Kd**4 + A*B*C*E*G/Kd**4 + A*B*C*F*G/Kd**4 + A*B*C*G/Kd**3 + A*B*D*E*G/Kd**4 + A*B*D*F*G/Kd**4 + A*B*D*G/Kd**3 + A*B*E*F*G/Kd**4 + A*B*E*G/Kd**3 + A*B*F*G/Kd**3 + A*B*G/Kd**2 + A*C*D*E*G/Kd**4 + A*C*D*F*G/Kd**4 + A*C*D*G/Kd**3 + A*C*E*F*G/Kd**4 + A*C*E*G/Kd**3 + A*C*F*G/Kd**3 + A*C*G/Kd**2 + A*D*E*F*G/Kd**4 + A*D*E*G/Kd**3 + A*D*F*G/Kd**3 + A*D*G/Kd**2 + A*E*F*G/Kd**3 + A*E*G/Kd**2 + A*F*G/Kd**2 + A*G/Kd + B*C*D*E*G/Kd**4 + B*C*D*F*G/Kd**4 + B*C*D*G/Kd**3 + B*C*E*F*G/Kd**4 + B*C*E*G/Kd**3 + B*C*F*G/Kd**3 + B*C*G/Kd**2 + B*D*E*F*G/Kd**4 + B*D*E*G/Kd**3 + B*D*F*G/Kd**3 + B*D*G/Kd**2 + B*E*F*G/Kd**3 + B*E*G/Kd**2 + B*F*G/Kd**2 + B*G/Kd + C*D*E*F*G/Kd**4 + C*D*E*G/Kd**3 + C*D*F*G/Kd**3 + C*D*G/Kd**2 + C*E*F*G/Kd**3 + C*E*G/Kd**2 + C*F*G/Kd**2 + C*G/Kd + D*E*F*G/Kd**3 + D*E*G/Kd**2 + D*F*G/Kd**2 + D*G/Kd + E*F*G/Kd**2 + E*G/Kd + F*G/Kd + G - G_tot) / G_tot
    result[2] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D*G/Kd**4 + A*B*C*D/Kd**3 + A*B*C*E*F/Kd**4 + A*B*C*E*G/Kd**4 + A*B*C*E/Kd**3 + A*B*C*F*G/Kd**4 + A*B*C*F/Kd**3 + A*B*C*G/Kd**3 + A*B*C/Kd**2 + A*B*D*E*F/Kd**4 + A*B*D*E*G/Kd**4 + A*B*D*E/Kd**3 + A*B*D*F*G/Kd**4 + A*B*D*F/Kd**3 + A*B*D*G/Kd**3 + A*B*D/Kd**2 + A*B*E*F*G/Kd**4 + A*B*E*F/Kd**3 + A*B*E*G/Kd**3 + A*B*E/Kd**2 + A*B*F*G/Kd**3 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B/Kd + A*C*D*E*F/Kd**4 + A*C*D*E*G/Kd**4 + A*C*D*E/Kd**3 + A*C*D*F*G/Kd**4 + A*C*D*F/Kd**3 + A*C*D*G/Kd**3 + A*C*D/Kd**2 + A*C*E*F*G/Kd**4 + A*C*E*F/Kd**3 + A*C*E*G/Kd**3 + A*C*E/Kd**2 + A*C*F*G/Kd**3 + A*C*F/Kd**2 + A*C*G/Kd**2 + A*C/Kd + A*D*E*F*G/Kd**4 + A*D*E*F/Kd**3 + A*D*E*G/Kd**3 + A*D*E/Kd**2 + A*D*F*G/Kd**3 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D/Kd + A*E*F*G/Kd**3 + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E/Kd + A*F*G/Kd**2 + A*F/Kd + A*G/Kd + A - A_tot) / A_tot
    result[3] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D*G/Kd**4 + A*B*C*D/Kd**3 + A*B*C*E*F/Kd**4 + A*B*C*E*G/Kd**4 + A*B*C*E/Kd**3 + A*B*C*F*G/Kd**4 + A*B*C*F/Kd**3 + A*B*C*G/Kd**3 + A*B*C/Kd**2 + A*B*D*E*F/Kd**4 + A*B*D*E*G/Kd**4 + A*B*D*E/Kd**3 + A*B*D*F*G/Kd**4 + A*B*D*F/Kd**3 + A*B*D*G/Kd**3 + A*B*D/Kd**2 + A*B*E*F*G/Kd**4 + A*B*E*F/Kd**3 + A*B*E*G/Kd**3 + A*B*E/Kd**2 + A*B*F*G/Kd**3 + A*B*F/Kd**2 + A*B*G/Kd**2 + A*B/Kd + B*C*D*E*F/Kd**4 + B*C*D*E*G/Kd**4 + B*C*D*E/Kd**3 + B*C*D*F*G/Kd**4 + B*C*D*F/Kd**3 + B*C*D*G/Kd**3 + B*C*D/Kd**2 + B*C*E*F*G/Kd**4 + B*C*E*F/Kd**3 + B*C*E*G/Kd**3 + B*C*E/Kd**2 + B*C*F*G/Kd**3 + B*C*F/Kd**2 + B*C*G/Kd**2 + B*C/Kd + B*D*E*F*G/Kd**4 + B*D*E*F/Kd**3 + B*D*E*G/Kd**3 + B*D*E/Kd**2 + B*D*F*G/Kd**3 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D/Kd + B*E*F*G/Kd**3 + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E/Kd + B*F*G/Kd**2 + B*F/Kd + B*G/Kd + B - B_tot) / B_tot
    result[4] = (A*B*C*D*E/Kd**4 + A*B*C*E*F/Kd**4 + A*B*C*E*G/Kd**4 + A*B*C*E/Kd**3 + A*B*D*E*F/Kd**4 + A*B*D*E*G/Kd**4 + A*B*D*E/Kd**3 + A*B*E*F*G/Kd**4 + A*B*E*F/Kd**3 + A*B*E*G/Kd**3 + A*B*E/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*E*G/Kd**4 + A*C*D*E/Kd**3 + A*C*E*F*G/Kd**4 + A*C*E*F/Kd**3 + A*C*E*G/Kd**3 + A*C*E/Kd**2 + A*D*E*F*G/Kd**4 + A*D*E*F/Kd**3 + A*D*E*G/Kd**3 + A*D*E/Kd**2 + A*E*F*G/Kd**3 + A*E*F/Kd**2 + A*E*G/Kd**2 + A*E/Kd + B*C*D*E*F/Kd**4 + B*C*D*E*G/Kd**4 + B*C*D*E/Kd**3 + B*C*E*F*G/Kd**4 + B*C*E*F/Kd**3 + B*C*E*G/Kd**3 + B*C*E/Kd**2 + B*D*E*F*G/Kd**4 + B*D*E*F/Kd**3 + B*D*E*G/Kd**3 + B*D*E/Kd**2 + B*E*F*G/Kd**3 + B*E*F/Kd**2 + B*E*G/Kd**2 + B*E/Kd + C*D*E*F*G/Kd**4 + C*D*E*F/Kd**3 + C*D*E*G/Kd**3 + C*D*E/Kd**2 + C*E*F*G/Kd**3 + C*E*F/Kd**2 + C*E*G/Kd**2 + C*E/Kd + D*E*F*G/Kd**3 + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E/Kd + E*F*G/Kd**2 + E*F/Kd + E*G/Kd + E - E_tot) / E_tot
    result[5] = (A*B*C*D*E/Kd**4 + A*B*C*D*F/Kd**4 + A*B*C*D*G/Kd**4 + A*B*C*D/Kd**3 + A*B*D*E*F/Kd**4 + A*B*D*E*G/Kd**4 + A*B*D*E/Kd**3 + A*B*D*F*G/Kd**4 + A*B*D*F/Kd**3 + A*B*D*G/Kd**3 + A*B*D/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*E*G/Kd**4 + A*C*D*E/Kd**3 + A*C*D*F*G/Kd**4 + A*C*D*F/Kd**3 + A*C*D*G/Kd**3 + A*C*D/Kd**2 + A*D*E*F*G/Kd**4 + A*D*E*F/Kd**3 + A*D*E*G/Kd**3 + A*D*E/Kd**2 + A*D*F*G/Kd**3 + A*D*F/Kd**2 + A*D*G/Kd**2 + A*D/Kd + B*C*D*E*F/Kd**4 + B*C*D*E*G/Kd**4 + B*C*D*E/Kd**3 + B*C*D*F*G/Kd**4 + B*C*D*F/Kd**3 + B*C*D*G/Kd**3 + B*C*D/Kd**2 + B*D*E*F*G/Kd**4 + B*D*E*F/Kd**3 + B*D*E*G/Kd**3 + B*D*E/Kd**2 + B*D*F*G/Kd**3 + B*D*F/Kd**2 + B*D*G/Kd**2 + B*D/Kd + C*D*E*F*G/Kd**4 + C*D*E*F/Kd**3 + C*D*E*G/Kd**3 + C*D*E/Kd**2 + C*D*F*G/Kd**3 + C*D*F/Kd**2 + C*D*G/Kd**2 + C*D/Kd + D*E*F*G/Kd**3 + D*E*F/Kd**2 + D*E*G/Kd**2 + D*E/Kd + D*F*G/Kd**2 + D*F/Kd + D*G/Kd + D - D_tot) / D_tot
    result[6] = (A*B*C*D*F/Kd**4 + A*B*C*E*F/Kd**4 + A*B*C*F*G/Kd**4 + A*B*C*F/Kd**3 + A*B*D*E*F/Kd**4 + A*B*D*F*G/Kd**4 + A*B*D*F/Kd**3 + A*B*E*F*G/Kd**4 + A*B*E*F/Kd**3 + A*B*F*G/Kd**3 + A*B*F/Kd**2 + A*C*D*E*F/Kd**4 + A*C*D*F*G/Kd**4 + A*C*D*F/Kd**3 + A*C*E*F*G/Kd**4 + A*C*E*F/Kd**3 + A*C*F*G/Kd**3 + A*C*F/Kd**2 + A*D*E*F*G/Kd**4 + A*D*E*F/Kd**3 + A*D*F*G/Kd**3 + A*D*F/Kd**2 + A*E*F*G/Kd**3 + A*E*F/Kd**2 + A*F*G/Kd**2 + A*F/Kd + B*C*D*E*F/Kd**4 + B*C*D*F*G/Kd**4 + B*C*D*F/Kd**3 + B*C*E*F*G/Kd**4 + B*C*E*F/Kd**3 + B*C*F*G/Kd**3 + B*C*F/Kd**2 + B*D*E*F*G/Kd**4 + B*D*E*F/Kd**3 + B*D*F*G/Kd**3 + B*D*F/Kd**2 + B*E*F*G/Kd**3 + B*E*F/Kd**2 + B*F*G/Kd**2 + B*F/Kd + C*D*E*F*G/Kd**4 + C*D*E*F/Kd**3 + C*D*F*G/Kd**3 + C*D*F/Kd**2 + C*E*F*G/Kd**3 + C*E*F/Kd**2 + C*F*G/Kd**2 + C*F/Kd + D*E*F*G/Kd**3 + D*E*F/Kd**2 + D*F*G/Kd**2 + D*F/Kd + E*F*G/Kd**2 + E*F/Kd + F*G/Kd + F - F_tot) / F_tot
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
    state.ABCD = A*B*C*D/Kd**3
    state.ABCE = A*B*C*E/Kd**3
    state.ABCF = A*B*C*F/Kd**3
    state.ABCG = A*B*C*G/Kd**3
    state.ABDE = A*B*D*E/Kd**3
    state.ABDF = A*B*D*F/Kd**3
    state.ABDG = A*B*D*G/Kd**3
    state.ABEF = A*B*E*F/Kd**3
    state.ABEG = A*B*E*G/Kd**3
    state.ABFG = A*B*F*G/Kd**3
    state.ACDE = A*C*D*E/Kd**3
    state.ACDF = A*C*D*F/Kd**3
    state.ACDG = A*C*D*G/Kd**3
    state.ACEF = A*C*E*F/Kd**3
    state.ACEG = A*C*E*G/Kd**3
    state.ACFG = A*C*F*G/Kd**3
    state.ADEF = A*D*E*F/Kd**3
    state.ADEG = A*D*E*G/Kd**3
    state.ADFG = A*D*F*G/Kd**3
    state.AEFG = A*E*F*G/Kd**3
    state.BCDE = B*C*D*E/Kd**3
    state.BCDF = B*C*D*F/Kd**3
    state.BCDG = B*C*D*G/Kd**3
    state.BCEF = B*C*E*F/Kd**3
    state.BCEG = B*C*E*G/Kd**3
    state.BCFG = B*C*F*G/Kd**3
    state.BDEF = B*D*E*F/Kd**3
    state.BDEG = B*D*E*G/Kd**3
    state.BDFG = B*D*F*G/Kd**3
    state.BEFG = B*E*F*G/Kd**3
    state.CDEF = C*D*E*F/Kd**3
    state.CDEG = C*D*E*G/Kd**3
    state.CDFG = C*D*F*G/Kd**3
    state.CEFG = C*E*F*G/Kd**3
    state.DEFG = D*E*F*G/Kd**3
    state.ABCDE = A*B*C*D*E/Kd**4
    state.ABCDF = A*B*C*D*F/Kd**4
    state.ABCDG = A*B*C*D*G/Kd**4
    state.ABCEF = A*B*C*E*F/Kd**4
    state.ABCEG = A*B*C*E*G/Kd**4
    state.ABCFG = A*B*C*F*G/Kd**4
    state.ABDEF = A*B*D*E*F/Kd**4
    state.ABDEG = A*B*D*E*G/Kd**4
    state.ABDFG = A*B*D*F*G/Kd**4
    state.ABEFG = A*B*E*F*G/Kd**4
    state.ACDEF = A*C*D*E*F/Kd**4
    state.ACDEG = A*C*D*E*G/Kd**4
    state.ACDFG = A*C*D*F*G/Kd**4
    state.ACEFG = A*C*E*F*G/Kd**4
    state.ADEFG = A*D*E*F*G/Kd**4
    state.BCDEF = B*C*D*E*F/Kd**4
    state.BCDEG = B*C*D*E*G/Kd**4
    state.BCDFG = B*C*D*F*G/Kd**4
    state.BCEFG = B*C*E*F*G/Kd**4
    state.BDEFG = B*D*E*F*G/Kd**4
    state.CDEFG = C*D*E*F*G/Kd**4


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
    ABCDG = state.ABCDG
    ABCE = state.ABCE
    ABCEF = state.ABCEF
    ABCEG = state.ABCEG
    ABCF = state.ABCF
    ABCFG = state.ABCFG
    ABCG = state.ABCG
    ABD = state.ABD
    ABDE = state.ABDE
    ABDEF = state.ABDEF
    ABDEG = state.ABDEG
    ABDF = state.ABDF
    ABDFG = state.ABDFG
    ABDG = state.ABDG
    ABE = state.ABE
    ABEF = state.ABEF
    ABEFG = state.ABEFG
    ABEG = state.ABEG
    ABF = state.ABF
    ABFG = state.ABFG
    ABG = state.ABG
    AC = state.AC
    ACD = state.ACD
    ACDE = state.ACDE
    ACDEF = state.ACDEF
    ACDEG = state.ACDEG
    ACDF = state.ACDF
    ACDFG = state.ACDFG
    ACDG = state.ACDG
    ACE = state.ACE
    ACEF = state.ACEF
    ACEFG = state.ACEFG
    ACEG = state.ACEG
    ACF = state.ACF
    ACFG = state.ACFG
    ACG = state.ACG
    AD = state.AD
    ADE = state.ADE
    ADEF = state.ADEF
    ADEFG = state.ADEFG
    ADEG = state.ADEG
    ADF = state.ADF
    ADFG = state.ADFG
    ADG = state.ADG
    AE = state.AE
    AEF = state.AEF
    AEFG = state.AEFG
    AEG = state.AEG
    AF = state.AF
    AFG = state.AFG
    AG = state.AG
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + ABC + ABCD + ABCDE + ABCDF + ABCDG + ABCE + ABCEF + ABCEG + ABCF + ABCFG + ABCG + ABD + ABDE + ABDEF + ABDEG + ABDF + ABDFG + ABDG + ABE + ABEF + ABEFG + ABEG + ABF + ABFG + ABG + AC + ACD + ACDE + ACDEF + ACDEG + ACDF + ACDFG + ACDG + ACE + ACEF + ACEFG + ACEG + ACF + ACFG + ACG + AD + ADE + ADEF + ADEFG + ADEG + ADF + ADFG + ADG + AE + AEF + AEFG + AEG + AF + AFG + AG)/A_tot


