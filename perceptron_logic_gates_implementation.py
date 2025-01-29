"""
This file contains the code for Perceptron Logic Gates Implementation
where we will be implementing and testing the following gates
AND, OR, NAND, NOR
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

# creating a function to test the logic gates
def test_gates(gate_name: str, gate: Callable[[list[int]],int]) -> None:
    """ Test all the possible outputs of a 2-input perceptron logic gate

    :param gate_name: Name of the gate
    :type gate_name: str
    :param gate: Function representing the logic gate
    :type gate: Callable[[list[int]],int]
    """
    print(f"Testing {gate_name} gate")
    print("Input 1 | Input 2 | Output")
    print("---------------------------")
    for input_1 in [0,1]:
        for input_2 in [0,1]:
            output = gate([input_1, input_2])
            print(f"   {input_1}    |    {input_2}    |   {output}")
    print()

def main() -> None:
    """Main function to test all the gates."""
    for gate_name, gate in logic_gates.items():
        test_gates(gate_name, gate)

if __name__ == "__main__":
    main()