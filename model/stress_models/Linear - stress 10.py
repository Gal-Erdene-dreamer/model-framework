"""
Model file created on 2021-08-20 11:01:38.285155 
Created using the automatic src/model_creator.py process.

Original input parameters
Equations:
Aa + Ab = AaAb; KD
AaAb + Ac = AaAbAc; KD
AaAbAc + Ad = AaAbAcAd; KD
AaAbAcAd + Ae = AaAbAcAdAe; KD
AaAbAcAdAe + Af = AaAbAcAdAeAf; KD
AaAbAcAdAeAf + Ag = AaAbAcAdAeAfAg; KD
AaAbAcAdAeAfAg + Ah = AaAbAcAdAeAfAgAh; KD
AaAbAcAdAeAfAgAh + Ai = AaAbAcAdAeAfAgAhAi; KD
AaAbAcAdAeAfAgAhAi + Aj = AaAbAcAdAeAfAgAhAiAj; KD

Labeled specie: Aa
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['AaAbAc', 'Ae', 'Aa', 'Ac', 'AaAbAcAd', 'KD', 'AaAbAcAdAeAfAg', 'Ai', 'Ad', 'AaAbAcAdAeAfAgAhAiAj', 'Ab', 'Ah', 'AaAbAcAdAeAfAgAh', 'AaAb', 'AaAbAcAdAeAfAgAhAi', 'Af', 'AaAbAcAdAe', 'Ag', 'Aj', 'AaAbAcAdAeAf', 'Ae_tot', 'Aa_tot', 'Ac_tot', 'Ai_tot', 'Ad_tot', 'Ab_tot', 'Ah_tot', 'Af_tot', 'Ag_tot', 'Aj_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['Ae', 'Aa', 'Ac', 'Ai', 'Ad', 'Ab', 'Ah', 'Af', 'Ag', 'Aj']
# Species who's concentration can be determined from others
dependent_species = ['AaAb', 'AaAbAc', 'AaAbAcAd', 'AaAbAcAdAe', 'AaAbAcAdAeAf', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAi', 'AaAbAcAdAeAfAgAhAiAj']
# The constant terms in the model
constants = ['KD']
# Which components are labeled / detected in the experiment
labeled_components = ['AaAbAc', 'Aa', 'AaAbAcAd', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAhAiAj', 'AaAbAcAdAeAfAgAh', 'AaAb', 'AaAbAcAdAeAfAgAhAi', 'AaAbAcAdAe', 'AaAbAcAdAeAf'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    Ae = concentrations[0]
    Aa = concentrations[1]
    Ac = concentrations[2]
    Ai = concentrations[3]
    Ad = concentrations[4]
    Ab = concentrations[5]
    Ah = concentrations[6]
    Af = concentrations[7]
    Ag = concentrations[8]
    Aj = concentrations[9]

    # Readability
    Aa_tot = state.Aa_tot
    Ab_tot = state.Ab_tot
    Ac_tot = state.Ac_tot
    Ad_tot = state.Ad_tot
    Ae_tot = state.Ae_tot
    Af_tot = state.Af_tot
    Ag_tot = state.Ag_tot
    Ah_tot = state.Ah_tot
    Ai_tot = state.Ai_tot
    Aj_tot = state.Aj_tot
    KD = state.KD

    result = np.zeros(10)
    result[0] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Ae - Ae_tot) / Ae_tot
    result[1] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Aa*Ab/KD + Aa - Aa_tot) / Aa_tot
    result[2] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Ac - Ac_tot) / Ac_tot
    result[3] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Ai - Ai_tot) / Ai_tot
    result[4] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Ad - Ad_tot) / Ad_tot
    result[5] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Aa*Ab/KD + Ab - Ab_tot) / Ab_tot
    result[6] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Ah - Ah_tot) / Ah_tot
    result[7] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Af - Af_tot) / Af_tot
    result[8] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Ag - Ag_tot) / Ag_tot
    result[9] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aj - Aj_tot) / Aj_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.Ae = solution[0]
    state.Aa = solution[1]
    state.Ac = solution[2]
    state.Ai = solution[3]
    state.Ad = solution[4]
    state.Ab = solution[5]
    state.Ah = solution[6]
    state.Af = solution[7]
    state.Ag = solution[8]
    state.Aj = solution[9]

    # Readability 
    Aa = state.Aa
    Ab = state.Ab
    Ac = state.Ac
    Ad = state.Ad
    Ae = state.Ae
    Af = state.Af
    Ag = state.Ag
    Ah = state.Ah
    Ai = state.Ai
    Aj = state.Aj
    KD = state.KD

    # Dependent variables
    state.AaAb = Aa*Ab/KD
    state.AaAbAc = Aa*Ab*Ac/KD**2
    state.AaAbAcAd = Aa*Ab*Ac*Ad/KD**3
    state.AaAbAcAdAe = Aa*Ab*Ac*Ad*Ae/KD**4
    state.AaAbAcAdAeAf = Aa*Ab*Ac*Ad*Ae*Af/KD**5
    state.AaAbAcAdAeAfAg = Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6
    state.AaAbAcAdAeAfAgAh = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7
    state.AaAbAcAdAeAfAgAhAi = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8
    state.AaAbAcAdAeAfAgAhAiAj = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9


def data_function(state):
    """
    Function to map state object to experimental data values.
    """
    # Readability
    Aa = state.Aa
    AaAb = state.AaAb
    AaAbAc = state.AaAbAc
    AaAbAcAd = state.AaAbAcAd
    AaAbAcAdAe = state.AaAbAcAdAe
    AaAbAcAdAeAf = state.AaAbAcAdAeAf
    AaAbAcAdAeAfAg = state.AaAbAcAdAeAfAg
    AaAbAcAdAeAfAgAh = state.AaAbAcAdAeAfAgAh
    AaAbAcAdAeAfAgAhAi = state.AaAbAcAdAeAfAgAhAi
    AaAbAcAdAeAfAgAhAiAj = state.AaAbAcAdAeAfAgAhAiAj
    Aa_tot = state.Aa_tot
    data_max = state.data_max
    data_min = state.data_min

    return Aa*data_min/Aa_tot + data_max*(AaAb + AaAbAc + AaAbAcAd + AaAbAcAdAe + AaAbAcAdAeAf + AaAbAcAdAeAfAg + AaAbAcAdAeAfAgAh + AaAbAcAdAeAfAgAhAi + AaAbAcAdAeAfAgAhAiAj)/Aa_tot


