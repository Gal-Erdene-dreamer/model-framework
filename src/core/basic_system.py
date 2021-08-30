# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:15:38 2020

@author: N.H.J. Geertjens

New system data type, providing the framework for model analysis.
"""
from configparser import RawConfigParser
from collections import namedtuple
from itertools import zip_longest
import os

import pandas as pd
import numpy as np
from scipy.optimize import root, least_squares

from src.core.guess import Guess
from src.analysis.helpers import timer
from src.core.exceptions import InvariantViolation

class System:
    """
    Invariants:
    System parameters are constant across associated conditions
        (\forall var; system.model.constants.has(var); 
        (\forall c; system.conditions.has(c); 
        c.state.get_value(var) == system.conditions[0].state.get_value(var)))
        
    """
    def __init__(self, name, model, titrate, known_parameters, guess = Guess):
        """
        Construct a System object. Every system object is associated with
        a single model file.
        
        Once one or more conditions have been added to the system, the system
        can be solved in order to determine parameters of interest from the
        model definition.
        
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
            Name of the model parameter which was titrated in the data i.e.
            the parameter that corresponds to the concentration values in the
            data.

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
  
        """
        self.name = name
        self.model = model
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
    
    def __iter__(self):
        return iter(self.conditions)
    
    def __len__(self):
        return len(self.conditions)
   
    def add_condition(self, condition, name, data, config_location, **kwargs):
        """
        Add a new condition to this object. It is recommended to use this
        method to add conditions as it makes sure that a condition is always
        associated with only one system.
        
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

        """
        new_condition = condition(name, data, self, config_location, **kwargs)
        new_condition.state.variables().update(self.known_parameters)
        self.conditions.append(new_condition)
        
    def solve_setup(self, max_concentration=float('inf'), 
                    min_concentration=0):
        """
        Performs additional setup before self.solve can be called.
        Makes sure the data_min and data_max values are assigned (used by a 
        number of data functions), setups the fit_data based on the given 
        limits and finally removes any 0 titrate concentrations to prevent 
        divide by zero errors in model definition and allow plotting on log 
        scale.
        
        This is done by calling the condition.solve_setup method on each
        condition.

        Parameters
        ----------
        max_concentration : float, optional
            Exclude all titrate values above the given value during fitting.
            The default is infinity (no exclusion).
        min_concentration : float, optional
            Exclude all titrate values below the given value during fitting.
            The default is 0 (no exclusion).

        Post
        ----
        self.fit_min, self.fit_max,and 
        (condition.state.data_max, condition.state.data_min, condition.fit_data
        \forall conditions in self.conditions) have been set.
        
        """
        # We only want to print the notice once, even if we find multiple
        # zero's.
        zero_flag = False
        self.fit_min = min_concentration
        self.fit_max = max_concentration
        
        for condition in self.conditions:
            zero_detected = condition._solve_setup(max_concentration,
                                               min_concentration)
            if zero_detected is True:
                zero_flag = True
        if zero_flag:
            print()
            print('NOTE: In some conditions a zero titrate concentration was '
                  'detected. Zero concentrations will be used to set '
                  'data limits but will not be fitted.\n')
            
    def system_defined_check(self, fit_parameters):
        """
        This check makes sure that all parameters are either fitted or have
        a known value and makes sure that all total concentrations are > 0.
        Zero values are converted to 1E-20 instead.

        Parameters
        ----------
        fit_parameters : dictionary of string: float
            The parameters that will be fitted and thus dont need to have a
            value assigned yet.

        Raises
        ------
        ValueError
            If any parameter is not defined
            If any total concentration is < 0.

        Returns
        -------
        None.

        """
        # We only want to print the zero concentration note once, regardless
        # of the number of total concentrations that are zero.        
        zero_flag = False
        
        # Check that all parameters are fitted or known
        for parameter in self.model.constants:
            if (parameter not in fit_parameters and 
                parameter not in self.known_parameters.keys()):
                raise ValueError(
                    f'Parameter: {parameter} is in neither fitted_parameters '
                    'nor known_parameters (case sensitive).')
        
        # Check that all _tot concentrations are set.
        required_concentrations = (
            var+"_tot" for var in self.model.independent_species)
        for specie in required_concentrations:
            # skip titrate
            if specie == self.titrate:
                continue
            # must be defined in all conditions
            for condition in self.conditions:
                value = condition.state.get_value(specie)
                # Cant be None
                if value is None:
                    raise ValueError('No value set for total concentration '
                        f'{specie} in {condition.name}. Please use the '
                        "'config.ini' file to define the total concentrations.")
                # Cant be negative.
                if value < 0:
                    raise ValueError('Negative (impossible) concentration '
                            f'detected for: {specie} in {condition.name}')
                # Model cant handle zero, make very small instead
                elif value == 0:
                    condition.state.set_value(specie, 1E-20)
                    zero_flag = True        
        if zero_flag:
            print('\nNOTE: Zero concentration detected for one of the '
                  'total concentrations. These have been converted to '
                  '1E-20 instead to prevent devision by zero.\n')
   
    
    def solve(self, fit_parameters, *, log_transform=True, 
              solve_residuals = True, verbose=1):
        """
        Find the optimal parameter values for this system based on the
        associated conditions. Uses a least-squares optimization approach, 
        starting from the parameter_guess.
        
        By default, a log transformation of the parameters is applied. Instead
        of directly fitting the parameter values, the following
        function is used:
            Parameter[i] = inital_guess[i] * (10 ** x[i])
        where x is initialised as the zero vector.
        This transformation helps greatly in solving problems where  
        parameters have different orders of magnitude and more generally
        speeds up the optimization process.
        
        Parameters
        ----------
        fit_parameters: Dictionary of string: number
            Keys in the dictionary correspond to the parameters to fit,
            values correspond to the initial guess for each variable.
        log_transform : Boolean
            Whether to use the log transform version of the error function
            or not during solving. See above. The default is True.
        solve_residuals : Boolean
            If true, the residuals for the determined solution will be 
            calculated. The default is True.
        verbose : {0, 1}
            How much information the solver prints. 0 is silent, 1 prints
            termination report. The default is 1.
            
        Pre
        ---
        self.error_function pre holds
        len(self.conditions) > 0 
        
        Modifies
        --------
        self.solution
        condition.state \forall condition in self.conditions

        Post
        ----
        self.solution contains a namedtuple with attributes:
            variables: the fitted parameters
            values: array of optimised parameter values
            residuals: pandas dataframe containing the fit residuals if 
                solve_residuals is True else None.
        condition.state reflects the determined optimal parameters 
            \forall condition in self.conditions.
        
        """
        # Check if all parameters are defined
        self.system_defined_check(fit_parameters)
        
        fit_variables = list(fit_parameters.keys())
        variable_guess = list(fit_parameters.values())
        
        # Chose whether to use log-transform.
        if log_transform:
            log_result = least_squares(
                self.error_function, np.zeros(len(fit_variables)),
                verbose = verbose, kwargs={'fit_variables': fit_variables,
                                     'base_value': variable_guess,
                                     'log_transform': True})
            values = (variable_guess*np.power(10, log_result.x))
        else: 
            optimize_result = least_squares(
                self.error_function, variable_guess, args=[fit_variables],
                xtol=None, bounds=(0, np.inf), verbose=verbose)
            values = optimize_result.x
        
        # The last iteration does not have to be the optimal result, set
        # parameter values to the determined solution.
        for par, value in zip(fit_variables, values):
            self.set_parameter(par, value)
        
        # Some anylses do not require the residuals, check if they should
        # be calculated.
        if solve_residuals:
            # Create dataframe from residuals
            data = []
            for condition in self.conditions:
                concentrations = condition.fit_data.index
                error = condition.error_function()
                data.append(pd.Series(
                    error, index=concentrations, name=condition.name))   
            residuals = pd.concat(data, axis=1)
        else:
            residuals = None
            
        # Create and set solution object
        S = namedtuple('Solution', ['variables', 'values', 'residuals'])
        solution = S(fit_variables, values, residuals)
        self.solution = solution

    def error_function(self, variable_values, fit_variables, *,
                       log_transform = False, base_value = None):
        """
        Returns the combined total error for all associated conditions by 
        calling their respective error functions with the given parameters.
        
        Note: Order of parameters is dictated by scipy.optimize.least_squares.        

        Parameters
        ----------
        variable_values : list-like of numbers
            The values for the equal index fit_variables to calculate model
            error for.
        fit_variables : list-like of strings
            Parameters in the condition which should be changed before
            error calculation.
        log_transform : boolean
            If false, treat variable_values as absolute parameter values.
            If true, treat variable_values as powers such that the
            condition.state values are set as:
                condition.state.fit_variables[i] = 
                                    base_value[i] * (10 ** variable_values[i]) 
            base_value cannot be None if log_transform is True.
        base_value : array-like
            If log_transform is True, base_values are used to determine the
            parameter values. Index positions for each base should correspond 
            to the index position in fit_variables.
            
        Pre
        ---
        \forall condition in self.conditions,
            condition.fit_data == series containing concentration, measured 
            value pairs with no nan values.
        len(variable_values) == len(fit_variables)
        if log_transform == True; len(base_values == len (fit_variables))
        
        Raises
        ------
        ValueError
            If any precondition is violated.
            
        Modifies
        --------
        condition.state for each condition in self.conditions
        
        Returns
        -------
        combined_error : numpy.array
            Combined error of all conditions, containing the difference 
            between the model prediction with given variable_values and each 
            measurement in condition.fit_data.

        """
        if base_value is None:
            base_value = []
        if len(fit_variables) != len(variable_values):
            raise ValueError(
                "system.error_function parameter list and guess list "
                "did not have same length.")
        if log_transform and (len(base_value) != len(fit_variables)):
            raise ValueError(
                'condition.error_function: When determining the error using '
                'log_transform = True, base_value must be array-like of shape '
                '(n, ) where n is the number of fit parameters.')
            
        # Adjust the condition parameters based on mode    
        for var, value, base in zip_longest(fit_variables, variable_values, 
                                            base_value):
            var_value = value if not log_transform else base*10**value
            self.set_parameter(var, var_value)
        
        combined_error = np.empty(0)
        for condition in self.conditions:
            specific_error = condition.error_function()
            combined_error = np.append(combined_error, specific_error, axis=0)      
        return combined_error     
        
    def set_solution_state(self):
        """
        Set state of each condition associated with this system to the
        parameters values found in self.solution
        
        Pre
        ---
        self.solution is determined using self.solve()
        
        Modifies
        --------
        condition.state for each condition in self.conditions
        """
        # Set the current state to the solution
        for variable, value in zip(self.solution.variables, 
                                   self.solution.values):
            self.set_parameter(variable, value)
    
    def set_parameter(self, parameter, value):
        """
        Changes a parameter value in the state of all associated conditions.
        
        Prints a warning if a parameter is being set that was not yet defined
        in the state object.

        Parameters
        ----------
        parameter : String
            The parameter to change
        value : float
            The value to set for the given parameter

        Post
        ----
        \forall condition; self.conditions.has(condition);
            condition.state.parameter == value 

        """
        if any((not hasattr(condition.state, parameter) 
                    for condition in self.conditions)):
            print('WARNING: set_parameter was asked to set a parameter '
                  f'which was not yet defined in some condition(s): {parameter}')
        for condition in self.conditions:
            setattr(condition.state, parameter, value)
            
    def get_parameter(self, parameter):
        """
        Returns the current value of the given parameter.

        Parameters
        ----------
        parameter : str
            The name of the parameter.

        Returns
        -------
        The value the parameter

        """
        return self.conditions[0].state.get_value(parameter)
             
    def print_solution(self):
        """
        Print the last determined solution for the system in a verbose format.
        
        Pre
        ---
        self.solution is determined using self.solve.
        
        Returns
        -------
        Prints verbose system information to standard out.
        """
        if self.solution is None:
            raise ValueError('Tried printing solution for system while '
                             'solution is none.')

        RMSE = np.nanmean(
                (self.solution.residuals.to_numpy().flatten() ** 2))**(0.5)

        print(f"---{self.name}---")
        if self.fit_min == 0 and self.fit_max == float('inf'):
            print("Model parameters were determined using all available "
                  "data points.")
        elif self.fit_min == 0:
            print("Model parameters were determined using data points up "
                  f"to titrate concentration {self.fit_max} M.")
        elif self.fit_max == float('inf'):
            print("Model parameters were determined using data points with "
                  f"titrate concentrations of atleast {self.fit_min} M.")
        else:
            print("Model parameters were determined using data points "
                  f"between titrate concentrations {self.fit_min} M and "
                  f"{self.fit_max} M.")
        print("Best parameter estimates are:")
        for parameter, value in zip(self.solution.variables, 
                                    self.solution.values): 
            print(f"    {parameter} : {value:.3e}.")
        print(f"The root mean squared error with this fit is {RMSE:.2e}")
        print("------" + len(self.name)*'-')
        print()
    
        
class Condition:
    """
    Invariants:
        ConcentrationIndex:
            self.data.index = concentration of titrate for corresponding
            measurement columns.
        MeasurementsOnly:
            (\forall col; self.data.columns.has(col); 'measurement' in col)
        TechincalReplicates:
            (\forall col; self.data.columns.has(col) && 'measurement' in col;
             col == technical replicate)

    """  
    def __init__(self, name, data, parent, config_location, **kwargs):
        """
        Create a new condition object, which holds the data for a range
        of titrate values, all other total concentrations being constant;
        A single condition.
        
        It is recommended to create conditions using the 'add_condition'
        method from the system object in order to make sure a condition is
        always linked to only a single system.

        Parameters
        ----------
        name : String
            The name for this condition. This will be displayed
            when plotting multiple conditions for example.
        data : Dataframe
            Dataframe containing the measurement data for this condition.
            Index concentrations in (M) and one or more columns containing 
            'measurement' in the header, corresponding to measured values.
            See the invariants for additional info.
        parent : System type
            The system this condition is associated with.
        config_location : path-like
            The location of the config file to use when setting up the state
            object associated with this condition.

        """
        self.name = name
        self.data = data
        self.system = parent
         
        self.state = State(parent.model)
        self.state.read_config(config_location, self.name)
        
        self.fit_data = None
        
    def _solve_setup(self, max_concentration, min_concentration):
        """
        This function will be called by the system object in order to setup
        the condition before solving the system. Hook method.
        
        The follow values will be set:
        self.state.data_max, self.state.data_min and self.fit_data

        Parameters
        ----------
        max_concentration : float
            Exclude all titrate values above the given value during fitting.
        min_concentration : float
            Exclude all titrate values below the given value during fitting.
            
        Returns
        -------
        True if a zero concentration was found, otherwise none.

        """
        bool_condition = ((self.data.index >= min_concentration) & 
                              (self.data.index <= max_concentration))
        self.fit_data = self.data[bool_condition].mean(axis=1)
        self.fit_data.name = f'{self.name} measured values'
        self.fit_data.dropna(inplace = True)
        
        # data_max and data_min can be manually set as known parameters
        # alternatively determine them from the data if unset.
        if getattr(self.state, 'data_max', None) is None:
            self.state.data_max = self.fit_data.max()
        if getattr(self.state, 'data_min', None) is None:
            self.state.data_min = self.fit_data.min()
            
        if 0 in self.data.index:
            self.data.drop(0, inplace=True)
            if 0 in self.fit_data.index:
                self.fit_data.drop(0, inplace=True)
            return True
        

    def error_function(self):
        """
        Returns the error for each measurement in self.fit_data compared to 
        the model prediction for the current self.state values. 

        Returns
        -------
        error : numpy.array
            Contains the difference between the model prediction and all the
            measurement values in self.fit_data.

        """
        # Determine model prediction and compare to actual data
        concentrations = self.fit_data.index.to_numpy()
        model_result = self.range_to_prediction(concentrations)
        measure_data = self.fit_data
        error = (measure_data - model_result)
        return error  

        
    def range_to_prediction(self, concentrations):
        """
        For each titrate concentration, predict the expected data value 
        based on the system model and current state object parameter values.
        
        If an equilibrium cannot be determined by equilibrate_state for a
        given concentration, np.nan is returned for that concentration.
            
        Parameters
        ----------
        concentrations: list-like
            Titrate concentrations to find prediction values for.
        
        Pre
        ---
        Condition has been assigned to a system
        
        Modifies
        --------
        self.state specie concentrations
        
        Raises
        ------
        ValueError:
            If default guess can not be determined because of None type values.
            
        Returns
        -------
        prediction: numpy.array
            Numpy (n,) array of data predictions (or np.nan if no equilibrium
            could be determined) corresponding to equal index concentration 
            value.
        """
        titrate = self.system.titrate
        prediction = np.zeros(len(concentrations))
        
        for i, concentration in enumerate(concentrations):
            # Update the state with new titrate concentration
            self.state.set_value(titrate, concentration)
            # Get guess for the new state
            guess = self.system.guess.default_guess(self.state)
            equilibrate_success = self.equilibrate_state(guess)
            if equilibrate_success:
                prediction[i] = self.state_to_prediction()
            else:
                prediction[i] = np.nan
                
        return prediction
    
    def equilibrate_state(self, guess):
        """
        Find the equilibrium concentrations for the current state and model,
        and sets the specie concentrations to the determined values.
        
        Multiple methods will be used in turn if an equilibrium cannot be
        determined by the previous method, starting with root solving and
        continuing with least-squares. Succes is determined by
        self.validate_solution.
        
        Parameters
        ----------
        guess: list-like
            Initial guess for the equilibrium concentrations of the dependent
            components to start the solving from.
        
        Modifies
        --------
        self.state concentrations but not constants.
         
        Post
        ----
        if return is True:
            self.state reflects equilibrium conditions
        
        Returns
        -------
        Succes: Boolean
            Wheter a equilibrium was successfully determined based on the
            criteria in self.validate_solution with any of the implemented
            methods.
        """
        root_solution = root(self.system.model.system_equations, guess, 
                        args=self.state) 
        
        if self.validate_solution(root_solution):
            self.system.model.update_state(root_solution.x, self.state)
            return True
        else:
            print('Root solver failed to get valid equilibrium. Switching '
                  'to least-squares algorithm.')
            
        dogbox_solution = least_squares(self.system.model.system_equations, guess, 
                                  bounds=(0,np.inf), args=[self.state],
                                  method='dogbox')
        if self.validate_solution(dogbox_solution):
            self.system.model.update_state(dogbox_solution.x, self.state)
            return True
        else:
            print('Failed to determine equilibrium for current state.')
                        
        return False

    
    def validate_solution(self, solution):
        """
        Validates a solution determined by equilibrate_state.

        Parameters
        ----------
        solution : solution object returned by scipy method.
            The solution to validate.

        Returns
        -------
        bool
            True if the solution passes all criteria otherwise False.

        """
        if solution.success == False:
            return False
        if not all(solution.x > 0):
            return False
        error = sum([abs(residual) for residual in solution.fun])
        
        # This assumes all values are divided by their total concentration,
        # aca all values are O(1).
        if error > 1E-4:
            return False
        
        # All checks passed
        return True

    def state_to_prediction(self):
        """
        Predict measurement data value for self.state based on the model 
        associated with the parent system.
                
        Returns
        -------
        prediction: float
            Data prediction for current state and model
        """
        return self.system.model.data_function(self.state)   
    
    
    def concentrations_at(self, titrate_concentration, guess=None):
        """
        Determines the concentrations of all independent and dependent species
        at the given titrate concentration.
        
        When this method is called for a range of titrate concentrations
        and this range is ordered, than the value returned for 'solution' can
        be entered as a guess for the next call in order to speed up the 
        operation. 

        Parameters
        ----------
        titrate_concentration : float
            The titrate concentration of interest.
        guess: list-like, optional
            Initial guess for the equilibrium concentrations of the dependent
            components to start the root solving from. If none is given, the
            model default guess will be used.

        Raises
        ------
        TypeError
            If default guess can not be determined because of None type values.

        Returns
        -------
        concentrations : Named tuple of two dictionaries and a list.
            A named tuple containing an attribute 'dependent' and an attribute
            'independent'. Each containing a dictionary where the keys
            correspond to the list of parameters found in the model for the
            respective attribute name and the values correspond to the 
            concentrations of those species at the given titrate concentration.
            The final attribute 'solution', is the correctly formated form
            of the independent species, which can be used directly as a guess
            for subsequent function calls, see method description.

        """
        # Set the titrate to the new concentration before determining guess
        self.state.set_value(self.system.titrate, titrate_concentration)
        
        if guess is None:
            guess = self.system.guess.default_guess(self.state)
        C = namedtuple(
                'Concentrations', ['independent', 'dependent', 'solution']) 
        
        equilibrate_success = self.equilibrate_state(guess)
        if equilibrate_success:
            solution = self.state.get_components()
            concentrations = C({}, {}, solution)
            for specie in self.system.model.independent_species:
                concentrations.independent[specie] = self.state.get_value(specie)
            for specie in self.system.model.dependent_species:
                concentrations.dependent[specie] = self.state.get_value(specie)
            return concentrations 
        else:
            concentrations = C({}, {}, None)
            for specie in self.system.model.independent_species:
                concentrations.independent[specie] = np.nan
            for specie in self.system.model.dependent_species:
                concentrations.dependent[specie] = np.nan
            return concentrations 
            
            
            
    
class State:
    """
    Primary function is that of a record type for current concentrations
    """
    def __init__(self, model):
        self.__dict__ = dict.fromkeys(model.variables)
        self.model = model
        
    def read_config(self, file, name=''):
        if not os.path.isfile(file):
            raise ValueError(f'Could not find config file at: {file}.\n'
                     'Please make sure the config file is present in the ' 
                     'input folder.')
        config = RawConfigParser()
        # Set to casesensitive reading
        config.optionxform = lambda option: option
        config.read(file, encoding="utf-8")
        if config.has_section(name):
            for key, value in config.items(name):
                self.__dict__[key] = float(value)
        else:
            for key, value in config.items('DEFAULT'):
                self.__dict__[key] = float(value)

    def variables(self):
        """
        Returns all variables assigned to this state.
        """
        return self.__dict__
    
    def get_value(self, variable):
        """
        Returns the value of the given variable.
        """
        try:
            return self.__dict__[variable]
        except KeyError:
            raise ValueError(f'Variable "{variable}" not present in state '
                             'object.')
    
    def set_value(self, variable, value):
        """
        Set state.variable to value. Should be used only for specie
        concentrations. Parameters can be set from the system.set_parameter.
        
        Raises a value error if the variable is not already in the state.
        """
        if variable in self.model.constants:
            raise InvariantViolation(
                'Model constants should be set from system.set_parameter to '
                'maintain invariants. State.setattr can be used to overide '
                'this check but correct method behaviour is no longer '
                'guarnteed.')
        if hasattr(self, variable):
            setattr(self, variable, value)
        else:
            raise ValueError(
                f'State object does not have attribute: {variable} ' 
                '(case sensitive). Use setattr when you want to manually add '
                'a new parameter.')
            
    def get_components(self):
        """
        Returns the current concentrations of the components for this state,
        in the same order as the equilibrium equations in the model file.
        """
        component_concentrations = [self.get_value(s) 
                                    for s in self.model.independent_species]
        return component_concentrations