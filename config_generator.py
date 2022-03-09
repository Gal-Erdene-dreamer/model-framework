# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:10:56 2021

@author: N.H.J. Geertjens

This tool helps to create a config file for a specific excel file containing
measurement data.

The top row of the file should contain headers, the first column the titrate 
concentrations and all other columns contain measurement data.
This format can be achieved with a direct copy from e.g. graphpad.

The _examples/example_input.xlsx file shows an example with one duplo
measurements and two triplo measurements.
The _examples/example_excel_input.xlsx shows an exampla with many different
measurements.

The generated config file is moved to the output folder.
"""

# Where is the input file located
input_file = 'input/example_data.xlsx'

# You do not need to change anything past this line #
#============================================================================#
import src.config_creator as cc
cc.config_for_excel(input_file, 'output/')
