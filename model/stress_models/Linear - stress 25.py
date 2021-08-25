"""
Model file created on 2021-08-20 11:06:39.205273 
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
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo + Ap = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp + Aq = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq + Ar = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr + As = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs + At = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt + Au = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu + Av = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv + Aw = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw + Ax = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx; KD
AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx + Ay = AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy; KD



Labeled specie: Aa
data_mode: anisotropy
"""

import numpy as np

# All variables for this model
variables = ['AaAbAc', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt', 'Aa', 'Ap', 'AaAbAcAd', 'Aq', 'As', 'At', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu', 'Ax', 'Av', 'Am', 'Ak', 'AaAbAcAdAeAfAgAhAiAjAkAlAm', 'Ad', 'AaAbAcAdAeAfAgAhAiAj', 'Ay', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAn', 'Ab', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAiAjAk', 'AaAbAcAdAeAfAgAhAiAjAkAl', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv', 'AaAbAcAdAeAfAgAhAi', 'Al', 'Ag', 'KD', 'AaAbAcAdAeAf', 'Ae', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo', 'Ar', 'Ac', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx', 'Ai', 'An', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr', 'Au', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs', 'Ah', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp', 'AaAb', 'Af', 'AaAbAcAdAe', 'Ao', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy', 'Aj', 'Aw', 'Aa_tot', 'Ap_tot', 'Aq_tot', 'As_tot', 'At_tot', 'Ax_tot', 'Av_tot', 'Am_tot', 'Ak_tot', 'Ad_tot', 'Ay_tot', 'Ab_tot', 'Al_tot', 'Ag_tot', 'Ae_tot', 'Ar_tot', 'Ac_tot', 'Ai_tot', 'An_tot', 'Au_tot', 'Ah_tot', 'Af_tot', 'Ao_tot', 'Aj_tot', 'Aw_tot']
# The species for which the concentrations need to be determined
# in order to solve the system. Will have the same order as system_equations.
independent_species = ['Aa', 'Ap', 'Aq', 'As', 'At', 'Ax', 'Av', 'Am', 'Ak', 'Ad', 'Ay', 'Ab', 'Al', 'Ag', 'Ae', 'Ar', 'Ac', 'Ai', 'An', 'Au', 'Ah', 'Af', 'Ao', 'Aj', 'Aw']
# Species who's concentration can be determined from others
dependent_species = ['AaAb', 'AaAbAc', 'AaAbAcAd', 'AaAbAcAdAe', 'AaAbAcAdAeAf', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAi', 'AaAbAcAdAeAfAgAhAiAj', 'AaAbAcAdAeAfAgAhAiAjAk', 'AaAbAcAdAeAfAgAhAiAjAkAl', 'AaAbAcAdAeAfAgAhAiAjAkAlAm', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAn', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy']
# The constant terms in the model
constants = ['KD']
# Which components are labeled / detected in the experiment
labeled_components = ['AaAbAc', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt', 'Aa', 'AaAbAcAd', 'AaAbAcAdAeAfAg', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu', 'AaAbAcAdAeAfAgAhAiAjAkAlAm', 'AaAbAcAdAeAfAgAhAiAj', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAn', 'AaAbAcAdAeAfAgAh', 'AaAbAcAdAeAfAgAhAiAjAk', 'AaAbAcAdAeAfAgAhAiAjAkAl', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv', 'AaAbAcAdAeAfAgAhAi', 'AaAbAcAdAeAf', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp', 'AaAb', 'AaAbAcAdAe', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq', 'AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy'] 

def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
    Aa = concentrations[0]
    Ap = concentrations[1]
    Aq = concentrations[2]
    As = concentrations[3]
    At = concentrations[4]
    Ax = concentrations[5]
    Av = concentrations[6]
    Am = concentrations[7]
    Ak = concentrations[8]
    Ad = concentrations[9]
    Ay = concentrations[10]
    Ab = concentrations[11]
    Al = concentrations[12]
    Ag = concentrations[13]
    Ae = concentrations[14]
    Ar = concentrations[15]
    Ac = concentrations[16]
    Ai = concentrations[17]
    An = concentrations[18]
    Au = concentrations[19]
    Ah = concentrations[20]
    Af = concentrations[21]
    Ao = concentrations[22]
    Aj = concentrations[23]
    Aw = concentrations[24]

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
    Ap_tot = state.Ap_tot
    Aq_tot = state.Aq_tot
    Ar_tot = state.Ar_tot
    As_tot = state.As_tot
    At_tot = state.At_tot
    Au_tot = state.Au_tot
    Av_tot = state.Av_tot
    Aw_tot = state.Aw_tot
    Ax_tot = state.Ax_tot
    Ay_tot = state.Ay_tot
    KD = state.KD

    result = np.zeros(25)
    result[0] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Aa*Ab/KD + Aa - Aa_tot) / Aa_tot
    result[1] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Ap - Ap_tot) / Ap_tot
    result[2] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aq - Aq_tot) / Aq_tot
    result[3] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + As - As_tot) / As_tot
    result[4] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + At - At_tot) / At_tot
    result[5] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Ax - Ax_tot) / Ax_tot
    result[6] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Av - Av_tot) / Av_tot
    result[7] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Am - Am_tot) / Am_tot
    result[8] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Ak - Ak_tot) / Ak_tot
    result[9] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Ad - Ad_tot) / Ad_tot
    result[10] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Ay - Ay_tot) / Ay_tot
    result[11] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Aa*Ab/KD + Ab - Ab_tot) / Ab_tot
    result[12] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Al - Al_tot) / Al_tot
    result[13] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Ag - Ag_tot) / Ag_tot
    result[14] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Ae - Ae_tot) / Ae_tot
    result[15] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Ar - Ar_tot) / Ar_tot
    result[16] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Aa*Ab*Ac*Ad*Ae/KD**4 + Aa*Ab*Ac*Ad/KD**3 + Aa*Ab*Ac/KD**2 + Ac - Ac_tot) / Ac_tot
    result[17] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Ai - Ai_tot) / Ai_tot
    result[18] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + An - An_tot) / An_tot
    result[19] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Au - Au_tot) / Au_tot
    result[20] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Ah - Ah_tot) / Ah_tot
    result[21] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai/KD**8 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah/KD**7 + Aa*Ab*Ac*Ad*Ae*Af*Ag/KD**6 + Aa*Ab*Ac*Ad*Ae*Af/KD**5 + Af - Af_tot) / Af_tot
    result[22] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Ao - Ao_tot) / Ao_tot
    result[23] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao/KD**14 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An/KD**13 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am/KD**12 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al/KD**11 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak/KD**10 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj/KD**9 + Aj - Aj_tot) / Aj_tot
    result[24] = (Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23 + Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22 + Aw - Aw_tot) / Aw_tot
    return result 


def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """
    # Independent variables
    state.Aa = solution[0]
    state.Ap = solution[1]
    state.Aq = solution[2]
    state.As = solution[3]
    state.At = solution[4]
    state.Ax = solution[5]
    state.Av = solution[6]
    state.Am = solution[7]
    state.Ak = solution[8]
    state.Ad = solution[9]
    state.Ay = solution[10]
    state.Ab = solution[11]
    state.Al = solution[12]
    state.Ag = solution[13]
    state.Ae = solution[14]
    state.Ar = solution[15]
    state.Ac = solution[16]
    state.Ai = solution[17]
    state.An = solution[18]
    state.Au = solution[19]
    state.Ah = solution[20]
    state.Af = solution[21]
    state.Ao = solution[22]
    state.Aj = solution[23]
    state.Aw = solution[24]

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
    Ap = state.Ap
    Aq = state.Aq
    Ar = state.Ar
    As = state.As
    At = state.At
    Au = state.Au
    Av = state.Av
    Aw = state.Aw
    Ax = state.Ax
    Ay = state.Ay
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
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap/KD**15
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq/KD**16
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar/KD**17
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As/KD**18
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At/KD**19
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au/KD**20
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av/KD**21
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw/KD**22
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax/KD**23
    state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy = Aa*Ab*Ac*Ad*Ae*Af*Ag*Ah*Ai*Aj*Ak*Al*Am*An*Ao*Ap*Aq*Ar*As*At*Au*Av*Aw*Ax*Ay/KD**24


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
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx
    AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy = state.AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy
    Aa_tot = state.Aa_tot
    data_max = state.data_max
    data_min = state.data_min

    return Aa*data_min/Aa_tot + data_max*(AaAb + AaAbAc + AaAbAcAd + AaAbAcAdAe + AaAbAcAdAeAf + AaAbAcAdAeAfAg + AaAbAcAdAeAfAgAh + AaAbAcAdAeAfAgAhAi + AaAbAcAdAeAfAgAhAiAj + AaAbAcAdAeAfAgAhAiAjAk + AaAbAcAdAeAfAgAhAiAjAkAl + AaAbAcAdAeAfAgAhAiAjAkAlAm + AaAbAcAdAeAfAgAhAiAjAkAlAmAn + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAo + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoAp + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAq + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqAr + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAs + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAt + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAu + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAv + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAw + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAx + AaAbAcAdAeAfAgAhAiAjAkAlAmAnAoApAqArAsAtAuAvAwAxAy)/Aa_tot


