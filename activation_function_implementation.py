"""
This script contains code to implement activation functions without
making use of any mathematical libraries from Python

The goal is to implement the following Activation functions:
1. Sigmoid
2. ReLU
3. TanH

additionally will be using matplotlib to plot those activation functions
"""

import math
import matplotlib.pyplot as plt

def sigmoid_function(x: float) -> float:
    """Computes the sigmoid activation function"""
    return 1 / (1 + math.exp(-x))

def relu_function(x: float) -> float:
    """Computes the ReLU activation function"""
    return max(0, int(x))

def tanh_function(x: float) -> float:
    """Computes the hyperbolic tangent function"""
    return ((math.exp(x) - math.exp(-x))
              / (math.exp(x) + math.exp(-x)))