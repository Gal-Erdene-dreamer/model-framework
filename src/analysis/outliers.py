# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:35:20 2021

@author: N.H.J. Geertjens
"""
import numpy as np
import scipy.stats as stats

class UndeterminedError(Exception):
    pass

def doornbos_critical(alpha, df):
    """
    Calculates doornbos test critical value based on two-sided test, without
    bonferroni correction, for given alpha value and degrees of freedom df.
    """
    return stats.t.ppf(1-(alpha/2), df)


def doornbos_outlier(values, alpha=0.05):
    """
    Checks for outliers using a two-sided doornbos test with given alpha
    value. This specific function was designed for technical replicate outlier
    detection. In this context, no bonferroni correction is applied because
    extreme values will also heavily influence the mean. In this same context,
    the small n also means that only a single outlier can be accurately 
    detected. Finally, in the case that only two unique values exists in y,
    s_k can not be determined and no outliers will be detected.

    Parameters
    ----------
    values : np.array
        The input values (replicates) to be tested for outliers.

    Raises
    ------
    TypeError
        If values.ndim != 1
    UndeterminedError
        If len(set(values[~np.isnan(values)])) < 3

    Returns
    -------
    Boolean Array
        Array of same size as input array where: 
            \forall i; values.has(i); \return[i] == R
            where R: Is outlier.
        
    """
    if values.ndim != 1:
        raise TypeError(
            'Doornobs outlier input should be vector format.')
    
    y = values[~np.isnan(values)] 
    n = y.size    
    # Start with handleing the case where we have only one unique value.
    # This also means no outliers.
    if n > 0 and (y == y[0]).all() == True:
        return np.full(values.size, False)
    
    # Second is the case where there are only two unique values, in this case
    # s_k can not be determined, so raise an exception that can be handled by
    # client code.
    if len(set(y)) < 3:
        raise UndeterminedError(
            "Doornbos outlier detection not defined for two unique values.")
    
    # Remaining cases    
    mean = y.mean()
    std = np.std(y, ddof=1)
    u_k = (values - mean) / std
    upper = (n*(n-2)*u_k**2)
    lower = (n-1)**2-n*u_k**2
    w_k = (upper / lower)**0.5
    critical_value = doornbos_critical(alpha, n-2)
    return w_k >= critical_value

