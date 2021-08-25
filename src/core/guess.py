# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:23:20 2021

@author: N.H.J. Geertjens
"""


class Guess():
    """
    The task of this class it to determine the default guess for a system 
    based on the model associated with it. It combines the adapter and 
    template design patterns, offering the hook method '_define_guess'.
    A default implementation is given.
    
    A class was chosen based on the desire to have the ability to
    easily add a different implementation of the default guess without having
    to change the basic elements of the framework.
    """
    def __init__(self, system):
        """
        Create new guess object for the specified system

        Parameters
        ----------
        system : System object
            The system object to provide guess for.

        """
        self.model = system.model
        
    def _define_guess(self, state):
        """
        Hook method for determination of the initial guess. This method
        should return a list of floats that can be used as initial guess for
        the associated system. The order of this lists should be equal to 
        the order expected in the model equilibrium_equations.
        
        This default implementation returns all independent_species as free
        in solution.
        """
        return [getattr(state, (specie + '_tot')) 
                    for specie in self.model.independent_species]
        
    def default_guess(self, state):
        """
        This method provides the intial guess that is needed in order to solve
        the system_equations.
        
        Implements adapter pattern.

        Parameters
        ----------
        state : state object
            The state for which to get the guess.
        
        Raises
        ------
        ValueError
            if one of the variables required for initial guess returns None
            
        Returns
        -------
        initial_guess : list of floats
            The intial guess for the solver as a list of numbers.

        """
        initial_guess = self._define_guess(state)
        if None in initial_guess:
            raise ValueError(
                'default_guess found a None value while determining '
                'initial_guess. Make sure all required species are defined.')
        return initial_guess