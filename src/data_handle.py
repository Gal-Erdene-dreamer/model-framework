# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:38:03 2020

@author: N.H.J. Geertjens
"""
import glob

import pandas as pd

def process_csv(folder):
    """
    Read in all .csv files in the input folder, process them and return them
    as a dictionary of dataframes.
    
    Processing:
        -key of dataframe corresponds with name of file
        -Columns are all lower case, no trailing and leading whitespaces
        -Column 'concentration' is used as index.
        -All columns which do not contain '*measurement*' are dropped
    
    Raises
    ------
    ValueError
        If no measurement columns are detected in a processed .csv file
        or if no csv files are detected in the input folder.
    
    return:
        dictionary with as keys the file names. Each key containins a 
        pandas dataframe with the values contained in the file with processing
        applied.    
    """
    data = {}
    #Glob is a unix style module used to retrieve files/pathnames matching a patern.
    for file in glob.glob(folder + '/*.csv'):
        # Determine the filename
        name = file[file.rfind("\\")+1:file.rfind(".csv")]
        df = pd.read_csv(file, header=0, delimiter=';')
        df.columns= df.columns.str.strip().str.lower()
        df.set_index('concentration', inplace=True)
        df = df.filter(like="measurement", axis=1)
        if len(df.columns) < 1:
            raise ValueError(
                "Processed dataframe contains no measurements columns. "+
                "Please check the input file format.")
        data[name] = df
    if len(data.keys()) == 0:
      raise ValueError(
          "No correct .csv files found during data import in folder: "
          f"{folder}.")
    return data

def process_excel(folder):
    """
    Process an excel-like type file in the input folder for use with the
    framework.
    
    Supports xlsx, xls and ods file types.

    Parameters
    ----------
    folder : pathlike
        The folder to look for the input file.

    Raises
    ------
    TypeError
        If no files of the allowed types are found.
        If multiple files of a allowed type are found.
    ValueError
        If format violations are found by pre process check.  

    Returns
    -------
    data : dictionary
        data_name: dataframe pairs. With the name determined by the header
        in the excel file and the data the measurements corresponding to that
        header.

    """
    data_types = ['xlsx', 'xls', 'ods']
    # Try different file formats
    for extention in data_types:
        file = _file_finder(folder, extention)
        if file is not None:
            break
        
    # Check if a file was found
    if file is None:
      raise TypeError(
          "None of file types: '{}' found in input folder: {}".format(
              ', '.join(data_types), folder))       
    df = _pre_process_excel(file)
    
    # Setup
    data = {}
    concentration = df.iloc[:,0]
    header_index = [i+1 for i, name in enumerate(df.columns[1:]) 
                    if 'Unnamed' not in name]
    n_headers = len(header_index)

    # Create dataframes
    for i, start in enumerate(header_index):
        if (i + 1) < n_headers:
            stop = header_index[i+1]
        else:
            stop = len(df.columns)
        colls = df.iloc[:,start:stop]
        headers = ['concentration'] + ['measurement_' + str(nr) 
                                       for nr in range(1, len(colls.columns)+1)]
        name = df.columns[start]
        result = pd.concat([concentration, colls], axis=1)
        result.columns = headers
        result.set_index('concentration', inplace=True)
        data[name] = result
    return data


def _file_finder(folder, extention):
    """
    Find all files of the given extention in folder. If there is exactly one
    return it. If there are multiple, raise value error.
    Otherwise, return None.
    """
    files = glob.glob(folder + f'/*.{extention}')
    if len(files) == 1:
        return files[0]
    elif len(files) > 1:
        raise TypeError(f'Multiple files found with extention: ".{extention}".'
                'Please make sure there is only one file of the input type in'
                ' the input folder.')
    else:
        return None

def _pre_process_excel(file):
    """
    Pre-process a excel-like file. 
    Check if there at least 2 columns and that each of the measurement names
    is valid within the config and python environment using _excel_name_check.
    """
    df = pd.read_excel(file)
    measurements = len(df.columns)-1
    if measurements < 1:
        raise ValueError(
            f'No measurement collumns detected in file: {file}.\n'
            'Please check the input file.')
    for header in df.columns[1:]:
        _excel_name_check(header)    
    return df
    
def _excel_name_check(name):
    """
    Check that the given name is valid for use in both config.ini files and
    the python environment.
    """
    forbidden_chars = ['[', ']', '#', ';', '\\']
    if any(char in name for char in forbidden_chars):
        raise ValueError("Headers / Names cannot contain these characters: "
                      f"{' '.join(forbidden_chars)}\n"
                      f"{name}")
    
