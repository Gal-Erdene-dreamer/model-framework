# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:06:58 2021

@author: N.H.J. Geertjens
"""
import os
import src.localization.input_generator_strings as strings
from src.data_handle import _pre_process_excel


def config_for_excel(path, output):
    """
    Generates a config file for the given excel-like file.
    
    Excel file requirements:
    Only a single worksheet
    Row 1 contains only headers
    Column A contains concentrations, starting at the second row.
    Row 2:n for column B and onward contain measurement results.
    
    Each column containing a header is seen as the start of a new condition.
    The names of the generated files are determined by the headers.
    Names cannot contain '[', ']' or '#'.

    Parameters
    ----------
    path : pathlike
        The input excel file location.
    output : pathlike
        Location in which the files are saved.

    Raises
    ------
    ValueError if:
        Number of detected measurements columns < 1
        The name of a repeat contains an illegal character.
        
    Post
    ----
    Generates a config file for use with this excel-like file.

    """
    # Setup
    df = _pre_process_excel(path)
    names = [name for name in df.columns[1:] if 'Unnamed' not in name]
    
    # Create config
    os.makedirs('output/', exist_ok=True)    
    with open(output+'config.ini', mode='w', encoding="utf-8") as file:
        # Get the config header from strings file.
        file.write(strings.header)
        for name in names:
            file.write(f'[{name}]\n\n\n')
    print('Config created and moved to output folder.')