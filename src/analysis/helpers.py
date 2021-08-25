# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:06:08 2021

@author: N.H.J. Geertjens
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'Function time: {elapsed} s')
        return result
    return wrapper    

def _to_units(number):
    """
    Takes a number and converts it to a SI prefix. Used for textlabel
    purposes. T-A (+12, -18) supported.

    Parameters
    ----------
    number : number
        The number to convert.

    Returns
    -------
    str
        '{scaled_number} {SI-prefix}'

    """
    units = {-12: "T", -9: "G", -6: "M", -3: "K", 0: "",
             3: "m", 6: "µ", 9: "n", 12: "p", 15: "f", 18:"A"}
    k = -12
    while number * 10**k < 1: 
        k += 3
    if k > 18:
        k = 18
    return f"{float(number*10**k):g} {units[k]}"

def _axis_unit_label(multiplier):
    """
    Takes a matplotlib multiplier (e.g. 1e-9) from an axes and converts it 
    for label printing purposes.
    """
    if multiplier == '':
        return '1 '
    else:
        unit = _to_units(float(multiplier.replace('−', '-')))
        return f'{unit}'
        
    