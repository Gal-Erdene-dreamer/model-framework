# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:12:13 2021

@author: N.H.J. Geertjens
"""
from datetime import datetime

strings ={
'header': (
'"""\n'
f'Model file created on {datetime.now()} \n'
'Created using the automatic src/model_creator.py process.\n\n'
'Original input parameters\n'
'Equations:'),

'imports': ('import numpy as np\n\n'),
'variables_base': ('# All variables for this model\n'),
'labeled_base': (
    '# Which components are labeled / detected in the experiment\n'),
'independent_base': (
    '# The species for which the concentrations need to be determined\n'
    '# in order to solve the system. Will have the same order as ' 
    'system_equations.\n'),
'dependent_base': (
    "# Species who's concentration can be determined from others\n"),
'constants_base': ('# The constant terms in the model\n'),
'equations_base':(
'''def system_equations(concentrations, state):
    """
    The equilibrium equations for this system. If an input result in the zero
    vector, that input is a solution to the system.
    """
    # Potential solution of the system
'''),
'update_base':(
'''def update_state(solution, state):
    """
    Given a solution to the system_equations, update the state object to 
    reflect this solution.
    """\n'''),
'data_base':(
'''def data_function(state):
    """
    Function to map state object to experimental data values.
    """\n''')
}