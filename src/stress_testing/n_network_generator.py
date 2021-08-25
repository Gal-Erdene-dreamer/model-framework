# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:40:01 2021

@author: N.H.J. Geertjens
"""
from itertools import combinations
import string
import numpy as np
np.random.seed(2525354)
n = 10 # > 1
max_size = 4 # > 1

LETTERS = string.ascii_uppercase
COMPONENTS = LETTERS[0:n]

folder = 'F:\_School en opleiding\_Master BMT\_Afstuderen\Model\modelFramework\output\\'
with open(folder+'n_network_generator_reactions.txt', 'w') as f:
    for i in range(2,max_size+1):
        for combi in combinations(COMPONENTS, i):
            equation = f'{"".join(combi[0:-1])} + {combi[-1]} = {"".join(combi)}; Kd\n'
            f.write(equation)
    

print('Done creating stress test files')