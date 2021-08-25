# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:11:58 2021

@author: N.H.J. Geertjens
"""

header = """# Config file for use with the framework for equilibrium models.
# This file was made using the input_generator. 

# This config file is used to set the total concentrations for species other
# than the titrate. Values under the DEFAULT section will be set for all 
# conditions. Values for individual conditions can be set by creating sections
# with the specific conditions name. The name of a conditions is equal to the 
# corresponding input file name without extention (case sensitive).
# e.g. the input file 'AO_30_uM.csv' will correspond to state 'AO_30_uM' 

# Section names are placed in [brackets]
# variables are defines as:
# key = value

# Note that Section names and keys are both case SeNsItIvE.
# Spaces in key names are allowed and will be taken into account.

# Example; to set the variable 'S_tot' for all conditions to 10 uM:
# [DEFAULT]
# S_tot = 10E-6
#

[DEFAULT]


"""