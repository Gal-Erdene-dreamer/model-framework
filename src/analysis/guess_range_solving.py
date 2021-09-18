# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:50:25 2021

@author: N.H.J. Geertjens
"""
import pandas as pd
import numpy as np


def latin_hypercube_sample(n, m):
    """
    Latin hypercube sampling of n strata with m dimensions. This simple
    implementation assumes uniform distributions. 
    """
    lower = np.arange(n)/n
    upper = np.arange(1,n+1)/n
    points = np.random.uniform(low = lower, high = upper, size = [m,n])
    for i in range(1,m):
        np.random.shuffle(points[i,:])
    return points.T

def latin_hypercube_sample_log(n, first_guess, second_guess):
    """
    Use a latin hypercube like approach to create samples evenly distrubted
    across a log scale instead of a linear scale.
    """
    sequence = np.geomspace(first_guess, second_guess, n+1)
    lower = sequence[:-1]
    upper = sequence[1:]
    points = np.random.uniform(low = lower, high = upper)
    for i in range(1, len(first_guess)):
        np.random.shuffle(points[:,i])
    return points
    

def range_solver(system, *, range_fit_parameters=None, range_n = 10,
                 log_scale = True):
    """
    Solve the system starting from multiple intial guess values using 
    latin hypercube sampling.
    
    See src.post_process range_solver for details.
    """
    if range_fit_parameters is None:
        raise ValueError('range_fit_parameters additional argument '
                'should be a dictionary of tuples where each key is a '
                'fit parameter. \ne.g. for fit_parameters Kd and Alpha:\n'
                '"range_fit_parameters": {"Kd": (1E-5, 1E-3), "Alpha": (10, 1000)}')
    
    
    # Get the lower, upper and diff of each parameter
    first_guess = np.array([value[1] for value in range_fit_parameters.values()])
    second_guess =  np.array([value[0] for value in range_fit_parameters.values()])
    diffs = first_guess - second_guess
    
    # Create the LHC
    if log_scale:
        lhc_guess = latin_hypercube_sample_log(range_n, first_guess, 
                                               second_guess)
    else:
        m = len(range_fit_parameters)
        cube = latin_hypercube_sample(n=range_n, m=m)
        lhc_guess = cube * diffs + second_guess
        
    # Determine solutions
    solutions = []  
    n = len(lhc_guess)
    print('Range solver determined initial guess values, starting solver..')
    for i, guess in enumerate(lhc_guess):
        print(f'Solving run {i+1}/ {n}')
        # Fit_parameters order does not have to be equal to range_fit_parameters
        system.solve(dict(zip(range_fit_parameters.keys(), guess)), verbose=0)
        ssr = (system.solution.residuals**2).to_numpy(na_value=0).sum()
        solutions.append(np.append(system.solution.values, ssr))
    
    # Prepare and present the results
    df = pd.DataFrame(np.stack(solutions))
    df.columns = [*range_fit_parameters.keys()] + ['SSR']
    df.sort_values(by=['SSR'], inplace=True)
    print('Determined parameter values:')
    print(df)
    return df
    