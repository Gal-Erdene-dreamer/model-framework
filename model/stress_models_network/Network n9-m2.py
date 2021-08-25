"""
Model file created on 2021-08-20 14:04:40.720014 
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

Labeled specie: A
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['FG', 'AD', 'BF', 'B', 'BH', 'AB', 'AC', 'FI', 'BC', 'F', 'HI', 'G', 'EI', 'GI', 'CD', 'AG', 'I', 'H', 'BE', 'BI', 'Kd', 'FH', 'GH', 'AE', 'CG', 'DH', 'EG', 'EH', 'DI', 'EF', 'AH', 'CF', 'AF', 'CE', 'A', 'CH', 'AI', 'BG', 'DE', 'E', 'D', 'CI', 'DG', 'DF', 'C', 'BD', 'B_tot', 'F_tot', 'G_tot', 'A_tot', 'E_tot', 'I_tot', 'D_tot', 'H_tot', 'C_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['B', 'F', 'G', 'A', 'E', 'I', 'D', 'H', 'C']
# Species who's concentration can be determined from others
dependent_species = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'DE', 'DF', 'DG', 'DH', 'DI', 'EF', 'EG', 'EH', 'EI', 'FG', 'FH', 'FI', 'GH', 'GI', 'HI']
# The constant terms in the model
constants = ['Kd']
# Which components are labeled / detected in the experiment
labeled_components = ['AD', 'AB', 'AC', 'AG', 'AE', 'AH', 'AF', 'A', 'AI'] 

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
    I = concentrations[5]
    D = concentrations[6]
    H = concentrations[7]
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
    result[0] = (A*B/Kd + B*C/Kd + B*D/Kd + B*E/Kd + B*F/Kd + B*G/Kd + B*H/Kd + B*I/Kd + B - B_tot) / B_tot
    result[1] = (A*F/Kd + B*F/Kd + C*F/Kd + D*F/Kd + E*F/Kd + F*G/Kd + F*H/Kd + F*I/Kd + F - F_tot) / F_tot
    result[2] = (A*G/Kd + B*G/Kd + C*G/Kd + D*G/Kd + E*G/Kd + F*G/Kd + G*H/Kd + G*I/Kd + G - G_tot) / G_tot
    result[3] = (A*B/Kd + A*C/Kd + A*D/Kd + A*E/Kd + A*F/Kd + A*G/Kd + A*H/Kd + A*I/Kd + A - A_tot) / A_tot
    result[4] = (A*E/Kd + B*E/Kd + C*E/Kd + D*E/Kd + E*F/Kd + E*G/Kd + E*H/Kd + E*I/Kd + E - E_tot) / E_tot
    result[5] = (A*I/Kd + B*I/Kd + C*I/Kd + D*I/Kd + E*I/Kd + F*I/Kd + G*I/Kd + H*I/Kd + I - I_tot) / I_tot
    result[6] = (A*D/Kd + B*D/Kd + C*D/Kd + D*E/Kd + D*F/Kd + D*G/Kd + D*H/Kd + D*I/Kd + D - D_tot) / D_tot
    result[7] = (A*H/Kd + B*H/Kd + C*H/Kd + D*H/Kd + E*H/Kd + F*H/Kd + G*H/Kd + H*I/Kd + H - H_tot) / H_tot
    result[8] = (A*C/Kd + B*C/Kd + C*D/Kd + C*E/Kd + C*F/Kd + C*G/Kd + C*H/Kd + C*I/Kd + C - C_tot) / C_tot
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
    state.I = solution[5]
    state.D = solution[6]
    state.H = solution[7]
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


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    A = state.A
    AB = state.AB
    AC = state.AC
    AD = state.AD
    AE = state.AE
    AF = state.AF
    AG = state.AG
    AH = state.AH
    AI = state.AI
    A_tot = state.A_tot
    data_max = state.data_max
    data_min = state.data_min

    return A*data_min/A_tot + data_max*(AB + AC + AD + AE + AF + AG + AH + AI)/A_tot


