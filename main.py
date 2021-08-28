"""
Created on Thu Nov 12 10:37:48 2020
@author: N.H.J. Geertjens

Run the main program from here
"""

# Name of the model, should be located in the model folder
model = "your model"

# The name of the folder that contains the input data / config files.
input_folder = "input/"

"""
Determine what kind of system should be greated.
'combined': Treat all experiments as seperate conditions for the same
    system. (Multiple measurements, one common set of parameters)
'separate': Treat all experiments as separate systems, each with only a 
    single condition associated. Determines parameters for each.
    (Multiple systems, same analysis)
'analysis': Set up a system that has no experimental data associated with it.
    Requires the additional_arguments 'min_concentration' and
    'max_concentration' which determine the default titration range used
    by many analyses. Parameters cannot be fitted to this system.
"""
setup_type = "combined"

"""
Which variable corresponds to the concentrations in the input file.
Make sure to list the parameter corresponding to the total concentration here, 
not the free concentration. This will always end in '_tot'.
"""
titrate = 'R_tot'

"""
Define which parameters should be fitted before analysis is performed.
{'parameter_1': value, 'parameter_2': value}
"""
fit_parameters = {'KD':1E-3, 'Alpha':35}

"""
Define the known value for any remaining parameters in the chosen model,
same format as the fit_parameters.
"""
known_parameters = {}

# Which analyses to perform after fitting any unknown parameters.
analysis = ['plot_model']

"""
Enter any additional arguments to customise analysis behavior. Make sure
there is a comma between each argument.
"""
additional_arguments = {
    'argument_name': 'value', 
    'another_argument': 'value'
    }


"For regular use, nothing past this line needs to be changed."
#=============================================================================#       
from src.driver import run
systems = run(model = model,
    input_folder = input_folder,
    setup_type = setup_type,
    titrate = titrate,
    fit_parameters = fit_parameters,
    known_parameters = known_parameters,
    analysis = analysis,
    style = './matplotlibStyle/default.mplstyle',
    **additional_arguments)

"""
It is possible to perform other operations on 'systems' here if desired.
"""
pass

