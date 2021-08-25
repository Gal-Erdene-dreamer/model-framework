# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:11:48 2021

@author: N.H.J. Geertjens

This tool was designed to stress test the model and see how many components
could be handled before failure.

First i decide the number of components i would like to run by changing the n
value.
Then a 'config' and a 'reactions' file are created.
The config file can be used as is for the system, the reactions file holds
the reactions to be entered in the modelbuilder. I used titrate Aa, but this 
setting and the other following ones do not influence the results as the model
is not related to actual data in these tests.
"""
import string
LETTERS = string.ascii_uppercase
def get_name(i):
    if i > (len(LETTERS)**2):
        raise ValueError('Value too high')
    result = ''
    result += LETTERS[i // len(LETTERS)]
    i -= (i // len(LETTERS)) * len(LETTERS)
    result += LETTERS[i].lower()
    return(result)     
    

config_header ="""
# Config file for use with the Model Project.

# Please note that:
# section names are placed in [brackets]
# and section names are [CaSe SeNsiTivE]
# the name of a section corresponds to the name of the file (without extention).

# variables are defines as:
# key = value
# Keys have been configured to be case SeNsEtIvE!
# Also note that whitespaces in keys are taken into account!

# Default values for State objectes related to the systems can be set in the
# following section. If there is a section with the same name as the System 
# object name, that section will take priority over this default section.

[DEFAULT]
KD = 30
Aa_tot = 15
"""

# Number of components
n = 70

pre = 'F:\_School en opleiding\_Master BMT\_Afstuderen\Model\modelProject\output\\'
with open(pre+'n_generator_reactions.txt', 'w') as f, open(pre+'config.ini', 'w') as f2:
    if n < 2:
        raise ValueError('Does not work with less than 2 components')
    f2.write(config_header)    
    previous = get_name(0)
    for i in range(1,n):
        new = get_name(i)
        f.write(f'{previous} + {new} = {previous}{new}; KD\n')
        f2.write(f'{new}_tot = 15\n') 
        previous = previous+new

print('Done creating stress test files')
