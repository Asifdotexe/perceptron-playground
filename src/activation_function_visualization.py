"""
This module is to visualize the activation functions created in the
src/activation_function_implementation.py script
"""

from src.activation_function_implementation import (sigmoid_function,
                                                    relu_function,
                                                    tanh_function)

# generating a range of values for plotting
# the 0.1 here indicates the step size
list_of_input_values = [i * 0.1 for i in range(-100, 101)]

# generating values for each activation function
sigmoid = [sigmoid_function(input_value) for input_value in list_of_input_values]
relu = [relu_function(input_value) for input_value in list_of_input_values]
tanh = [tanh_function(input_value) for input_value in list_of_input_values]