# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:12:17 2021

@author: Lycolus
"""

from src.core.basic_system import System
from src.core.exceptions import AnalysisTypeError
from src.core.guess import Guess

class AnalysisSystem(System):
    def __init__(self, name, model, titrate, known_parameters, guess = Guess):
        """
        Construct a System object. Every system object is associated with
        a single model file.
        
        This system-type is designed in order to facilitate analysis without
        experimental data. As such, only a single condition can be added
        and all parameters need to be defined as known_parameters.
        
        Parameters
        ----------
        name : String
            The name of this system, used for printing and plotting.
        model : Python module reference
            Reference to a python module containing the functions required for
            a model definition. 
            See the example model files or use the model creator designed for 
            this purpose: 'src/model_creator.py' for more information on the
            format of a model file.
        titrate : String
            Name of the model parameter which will be considered as titrated
            for plotting and analysis purposes. 
            There is an important distinction between the total concentration
            (total amount of the specie present in the system) and the free
            concentration of that specie (the amount that is not bound to
            other species with the current conditions). 
            Here, the name corresponding to the total concentration should be
            provided. This value always ends in '_tot'.
        known_parameters : Dictionary of string: float
            Parameters within the model that have a known or set value.
            Given as parameter: value pairs. 
        guess : src.core.guess object
            The object that will determine the initial guess for this system.
            The default is src.core.guess.Guess
            
        Raises
        ------
        ValueError
            If Titrate is not found in model file.variables.
            If known_parameters does not include all parameters in the model

        """
        self.name = name
        self.model = model
        undeclared_parameters = [par for par in model.constants 
                                 if par not in known_parameters.keys()]
        if len(undeclared_parameters) > 0:
            raise ValueError(
                'Declaring all model constants as known_parameters is '
                'required for analysis-type System.\n'
                'missing parameters: {}'.format(*undeclared_parameters))
        self.known_parameters = known_parameters
        if titrate in self.model.variables:
           self.titrate = titrate
        else:
            raise ValueError(
                f"System could not find titrate: '{titrate}' in the model "
                "parameters. Please check the input (case sensitive).")
        self.guess = Guess(self)
        self.conditions = []
        self.solution = None
    
    def add_condition(self, condition, name, data, config_location, **kwargs):
        """
        Add a new condition to this object. It is recommended to use this
        method to add conditions as it makes sure that a condition is always
        associated with only one system. An analysis type system can have
        only one condition associated with it.
        
        All parameters in self.known_values will be copied to the new 
        condition.state after creation.
        
        In order to support multiple implementations of the condition object
        the condition type that needs to be created can specified and all
        additional named arguments will be passed to the init function by
        **kwargs.

        Parameters
        ----------
        condition : Condition class
            The type of new condition object to create. The default
            implementation is the 'Condition' class. 
        name : String
            The name for the new condition object. This will be displayed
            when plotting multiple conditions for example.
        data : Dataframe
            Dataframe containing the measurement data for this condition.
            See the specific condition invariants and documentation for the
            format required.
        config_location : path-like
            The location of the config file to use when setting up the state
            object associated with the new condition.
        **kwargs : optional
            Additional named arguments that will be passed to the __init__ 
            function of the condition specified.

        Raises
        ------
        AnalysisTypeError
            If more than one condition is added to this system
            
        """
        if len(self.conditions) == 0:
            new_condition = condition(name, data, self, config_location, 
                                      **kwargs)
            new_condition.state.variables().update(self.known_parameters)
            new_condition.state.data_min = 0
            new_condition.state.data_max = 1
            self.conditions.append(new_condition)
        else:
            raise AnalysisTypeError('Multiple conditions not allowed for '
                                    'analysis type.')
        
    def solve_setup(self, *args, **kwargs):
        raise AnalysisTypeError('Solving not supported for analysis type.')
        
    def solve(self, *args, **kwargs):
        raise AnalysisTypeError('Solving not supported for analysis type.')
            
    def set_solution_state(self, *args, **kwargs):
        raise AnalysisTypeError('Solving not supported for analysis type.')
                    
    def print_solution(self, *args, **kwargs):
        raise AnalysisTypeError('Solving not supported - cannot print ' 
                                'solution.')
        
    def error_function(self, *args, **kwargs):
        raise AnalysisTypeError('Analysis system has no data to compare '
                                'prediction against.')
        