"""
Created on Fri Feb 12 11:28:21 2021

@author: N.H.J. Geertjens
"""
# The name of the new model
name = 'example_model'

# The equations to build the model from
system_description = ("""
R + P = PR; Kd1
PR + S = PRS; Kd2 / Alpha
R + S = RS; Kd2
RS + P = PRS; Kd1/ Alpha
""")

"""
Which data function to use, the relation between the concentrations in the 
model state and the measured experimental data value.
'anisotropy': Default fluorescent anisotropy measurement. All labelled
    component free in solution is equal to data_min. Bound to ANY complex
    produces data_max signal. If there are multiple different contributions
    to the signal, use the custom data mode. 
    
    This mode can also be used for other measurements following a similar 
    pattern as long as the signal contributions of different species can be 
    summed.
'inverse_anisotropy': Inverted anisotropy mode. Unbound labelled component 
    results in high signal while all complexes containing the labelled
    component result in low signal.
'itc': One-to-one ITC binding data. NOTE: Expects the system energy, G, 
    NOT delta G as measurement data. Zero is defined as the energy at zero 
    bound complex. The measurement data is thus the summed energy change
    of all injections up to that point.
    Exothermic and endothermic measurements are both supported. 
    Make sure the labelled component is the component in the cell.
    Use custom for more complex situations.
'custom': Create a custom relation by entering it in the field below.
"""
data_function = 'anisotropy'

"""
In case of default data faction: which component is labeled / tracked / 
measured in the experiment. For the custom data function see below. """
labelled = 'P'

"""
The following line only needs to be changed when using the custom data function.
New variables can be described here and will be added to the model definition.
Please note that the automatic sorting that happens on the equations above
cannot be used here, so it is recommended to run the model builder once
to make sure the correct specie names are used before entering a custom
data input. See the procedure for additional details. 
"""
custom_input = ''

# You do not need to edit anything past this line
#=============================================================================
import src.model_creator as mc
mc.build_model_file(name = name, equations = system_description, 
                    labeled = labelled, data_mode = data_function, 
                    custom_input = custom_input)


