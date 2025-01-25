"""
This file contains the code for Perceptron Logic Gates Implementation
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

# defining the logic gates using defined weights and bias
logic_gates = {
    # outputs 1 when both inputs are 1
    "AND": perceptron(weights=[1,1], bias=-1.5),
    # outputs 1 when either of the input is 1
    "OR": perceptron(weights=[1,1], bias=-0.5),
    # outputs 1 unless both inputs are 1
    'NAND': perceptron(weights=[-1, -1], bias=1.5),
    # outputs 1 with both inputs are 0
    "NOR": perceptron(weights=[-1, -1], bias=0.5)
}