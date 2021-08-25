"""
Model file created on 2021-08-20 11:05:40.861519 
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
AaAbAcAdAeAfAgAhAiAj + Ak = AaAbAcAdAeAfAgAhAiAjAk; KD
AaAbAcAdAeAfAgAhAiAjAk + Al = AaAbAcAdAeAfAgAhAiAjAkAl; KD
AaAbAcAdAeAfAgAhAiAjAkAl + Am = AaAbAcAdAeAfAgAhAiAjAkAlAm; KD
AaAbAcAdAeAfAgAhAiAjAkAlAm + An = AaAbAcAdAeAfAgAhAiAjAkAlAmAn; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAn + Ao = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo; KD

Labeled specie: Aa
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['AaAbAc', 'Ae', 'Aa', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo', 'Ac', 'AaAbAcAd', 'KD', 'AaAbAcAdAeAfAg', 'Am', 'Ak', 'AaAbAcAdAeAfAgAhAiAjAkAlAm', 'Ai', 'Ad', 'AaAbAcAdAeAfAgAhAiAj', 'An', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAn', 'Ab', 'Ah', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAiAjAk', 'AaAbAcAdAeAfAgAhAiAjAkAl', 'AaAb', 'AaAbAcAdAeAfAgAhAi', 'Af', 'AaAbAcAdAe', 'Al', 'Ao', 'Ag', 'Aj', 'AaAbAcAdAeAf', 'Ae_tot', 'Aa_tot', 'Ac_tot', 'Am_tot', 'Ak_tot', 'Ai_tot', 'Ad_tot', 'An_tot', 'Ab_tot', 'Ah_tot', 'Af_tot', 'Al_tot', 'Ao_tot', 'Ag_tot', 'Aj_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['Ae', 'Aa', 'Ac', 'Am', 'Ak', 'Ai', 'Ad', 'An', 'Ab', 'Ah', 'Af', 'Al', 'Ao', 'Ag', 'Aj']
# Species who's concentration can be determined from others
dependent_species = ['AaAb', 'AaAbAc', 'AaAbAcAd', 'AaAbAcAdAe', 'AaAbAcAdAeAf', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAi', 'AaAbAcAdAeAfAgAhAiAj', 'AaAbAcAdAeAfAgAhAiAjAk', 'AaAbAcAdAeAfAgAhAiAjAkAl', 'AaAbAcAdAeAfAgAhAiAjAkAlAm', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAn', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo']
# The constant terms in the model
constants = ['KD']
# Which components are labeled / detected in the experiment
labeled_components = ['AaAbAc', 'Aa', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo', 'AaAbAcAd', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAhAiAjAkAlAm', 'AaAbAcAdAeAfAgAhAiAj', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAn', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAiAjAk', 'AaAbAcAdAeAfAgAhAiAjAkAl', 'AaAb', 'AaAbAcAdAeAfAgAhAi', 'AaAbAcAdAe', 'AaAbAcAdAeAf'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    Ae = concentrations[0]
    Aa = concentrations[1]
    Ac = concentrations[2]
    Am = concentrations[3]
    Ak = concentrations[4]
    Ai = concentrations[5]
    Ad = concentrations[6]
    An = concentrations[7]
    Ab = concentrations[8]
    Ah = concentrations[9]
    Af = concentrations[10]
    Al = concentrations[11]
    Ao = concentrations[12]
    Ag = concentrations[13]
    Aj = concentrations[14]

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
    Ak_tot = state.Ak_tot
    Al_tot = state.Al_tot
    Am_tot = state.Am_tot
    An_tot = state.An_tot
    Ao_tot = state.Ao_tot
    KD = state.KD

    result = np.zeros(15)
    result[0] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Ae - Ae_tot) / Ae_tot
    result[1] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Aa*Ab/KD + Aa - Aa_tot) / Aa_tot
    result[2] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Ac - Ac_tot) / Ac_tot
    result[3] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Am - Am_tot) / Am_tot
    result[4] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Ak - Ak_tot) / Ak_tot
    result[5] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Ai - Ai_tot) / Ai_tot
    result[6] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Ad - Ad_tot) / Ad_tot
    result[7] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + An - An_tot) / An_tot
    result[8] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Aa*Ab/KD + Ab - Ab_tot) / Ab_tot
    result[9] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Ah - Ah_tot) / Ah_tot
    result[10] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Af - Af_tot) / Af_tot
    result[11] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Al - Al_tot) / Al_tot
    result[12] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Ao - Ao_tot) / Ao_tot
    result[13] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Ag - Ag_tot) / Ag_tot
    result[14] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aj - Aj_tot) / Aj_tot
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
    state.Am = solution[3]
    state.Ak = solution[4]
    state.Ai = solution[5]
    state.Ad = solution[6]
    state.An = solution[7]
    state.Ab = solution[8]
    state.Ah = solution[9]
    state.Af = solution[10]
    state.Al = solution[11]
    state.Ao = solution[12]
    state.Ag = solution[13]
    state.Aj = solution[14]

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
    Ak = state.Ak
    Al = state.Al
    Am = state.Am
    An = state.An
    Ao = state.Ao
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
    state.AaAbAcAdAeAfAgAhAiAjAk = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10
    state.AaAbAcAdAeAfAgAhAiAjAkAl = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11
    state.AaAbAcAdAeAfAgAhAiAjAkAlAm = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAn = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14


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
    AaAbAcAdAeAfAgAhAiAjAk = state.AaAbAcAdAeAfAgAhAiAjAk
    AaAbAcAdAeAfAgAhAiAjAkAl = state.AaAbAcAdAeAfAgAhAiAjAkAl
    AaAbAcAdAeAfAgAhAiAjAkAlAm = state.AaAbAcAdAeAfAgAhAiAjAkAlAm
    AaAbAcAdAeAfAgAhAiAjAkAlAmAn = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAn
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo
    Aa_tot = state.Aa_tot
    data_max = state.data_max
    data_min = state.data_min

    return Aa*data_min/Aa_tot + data_max*(AaAb + AaAbAc + AaAbAcAd + AaAbAcAdAe + AaAbAcAdAeAf + AaAbAcAdAeAfAg + AaAbAcAdAeAfAgAh + AaAbAcAdAeAfAgAhAi + AaAbAcAdAeAfAgAhAiAj + AaAbAcAdAeAfAgAhAiAjAk + AaAbAcAdAeAfAgAhAiAjAkAl + AaAbAcAdAeAfAgAhAiAjAkAlAm + AaAbAcAdAeAfAgAhAiAjAkAlAmAn + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo)/Aa_tot


