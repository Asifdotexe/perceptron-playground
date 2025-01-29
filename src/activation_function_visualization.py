"""
This module is to visualize the activation functions created in the
src/activation_function_implementation.py script
"""

import matplotlib.pyplot as plt
from activation_function_implementation import (sigmoid_function,
                                                    relu_function,
                                                    tanh_function)

# generating a range of values for plotting
# the 0.1 here indicates the step size
list_of_input_values = [i * 0.1 for i in range(-100, 101)]

# generating values for each activation function
sigmoid = [sigmoid_function(input_value) for input_value in list_of_input_values]
relu = [relu_function(input_value) for input_value in list_of_input_values]
tanh = [tanh_function(input_value) for input_value in list_of_input_values]

# plotting the activation function
plt.figure(figsize=(10,6))

# plotting sigmoid
plt.subplot(3, 1, 1)
plt.plot(list_of_input_values, sigmoid, label="Sigmoid", color="blue")
plt.title("Activation Function: Sigmoid")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)

# plotting relu
plt.subplot(3, 1, 2)
plt.plot(list_of_input_values, relu, label='Relu', color="red")
plt.title("Activation Function: ReLU")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)

# plotting tanH
plt.subplot(3, 1, 3)
plt.plot(list_of_input_values, tanh, label='TanH', color="Green")
plt.title("Activation Function: TanH")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)

# displaying the plot
plt.tight_layout()
plt.show()