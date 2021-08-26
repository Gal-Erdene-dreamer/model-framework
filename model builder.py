"""
Created on Fri Feb 12 11:28:21 2021

@author: N.H.J. Geertjens
"""
# The name of the new model
name = 'example name'

# The equations to build the model from
equations = ("""
A + B = AB; Kd1
AB + C = ABC; Kd2
""")

# Which of the above species is labeled / tracked / measured.
labelled = 'C'

"""
Which data function to use, the relation between the concentrations in the 
model state and the measured experimental data value.
'anisotropy': Default fluorescent anisotropy measurement. All labeled
    comonent free in solution is equal to data_min. Bound to any complex
    produces data_max signal. If there are multiple different contributions
    to the signal, use the custom data mode.
'custom': Create a custom relation by entering it in the field below.
"""
data_mode = 'anisotropy'

"""
The following line only needs to be changed when using the custom data mode.
New variables can be described here and will be added to the model definition.
Please note that the automatic sorting that happens on the equations above
cannot be used here, so it is recommended to run the model builder once
to make sure the correct specie names are used before entering a custom
data input. See the procedure for additional details. """

custom_input = ''

# You do not need to edit anything past this line
#=============================================================================
import src.model_creator as mc
mc.build_model_file(name, equations, labelled, data_mode, custom_input)
