# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:06:58 2021

@author: N.H.J. Geertjens


! README !
----------
Legacy on 16-8-2021
This file was made legacy by the possiblity to directly use the input excel
file to create the dataframes instead of first creating .csv files.

However, this code might still be usefull if a situation arrises where the
intermediate csv input files are required. In the case of paired data (NMR)
for example.
"""

import pandas as pd
import src.localization.input_generator_strings as strings

def input_from_excel(path, output):
    """
    Generates input files and config file from an excel file containing all
    measurements.
    
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
    Generates input files and config file for use with the model framework
    in the given output folder.

    """
    print('Generating input files... ', end='')
    # Setup
    forbidden_chars = ['[', ']', '#', ';']
    df = pd.read_excel(path)
    concentration = df.iloc[:,0]
    measurements = len(df.columns)-1
    if measurements < 1:
        raise ValueError(
            'No measurement collumns detected, please check input.')
    
    header_index = [i+1 for i, name in enumerate(df.columns[1:]) 
                    if 'Unnamed' not in name]
    n_headers = len(header_index)
    names = []
    
    # Create condition .csv files
    for i, start in enumerate(header_index):
        if (i + 1) < n_headers:
            stop = header_index[i+1]
        else:
            stop = measurements + 1
            
        colls = df.iloc[:,start:stop]
        headers = ['concentration'] + ['measurement_' + str(nr) 
                                       for nr in range(1, len(colls.columns)+1)]
        name = df.columns[start]
        
        if any(char in name for char in forbidden_chars):
            raise ValueError("Headers / Names cannot contain these characters: "
                              f"{', '.join(forbidden_chars)}")
            
        result = pd.concat([concentration, colls], axis=1)
        result.columns = headers
        result.to_csv(output+name+'.csv', index=False, sep=';')
        names.append(name)
        
    # Create config    
    with open(output+'config.ini', mode='w', encoding="utf-8") as file:
        file.write(strings.header)
        for name in names:
            file.write(f'[{name}]\n\n\n')
    print('done.')
    print('Files moved to output folder.')
            
def _colNr(n):
    """
    Helper function to convert a 1-indexed number to an excel column name.
    """
    string = []
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string.append(chr(65 + remainder))
    return "".join(string[::-1])