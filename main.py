"""
This file contains the code for the following:

1. Perceptron gate implementation and simulation of the following gates
    a. AND
    b. OR
    c. NAND
    d. NOR
"""

from typing import Callable

def perceptron(weights: list[float], bias: float) -> Callable[[list[int]],int]:
    """ Create a perceptron function with given weights and bias.

    :param weights: List of weights given for inputs.
    :type weights: list[float]
    :param bias: Bias Term
    :type bias: float
    :returns: A function that computes the perceptron output for given inputs
    :rtype: Callable[[list[int],int]
    """
    def perceptron_function(inputs: list[int]) -> int:
        """Computing the output for a given set of inputs.

        :param inputs: List of binary inputs, should contain either 0 or 1
        :type inputs: list[int]
        :return: Binary output (0 or 1) based on weighted sum and bias.
        :rtype: int
        """
        # weighted sum = Σ (weights[i] * input[i]) + bias
        weighted_sum = sum(weight * input_value for weight, input_value in
                           zip(weights, inputs)) + bias
        return 1 if weighted_sum > 0 else 0

    return perceptron_function