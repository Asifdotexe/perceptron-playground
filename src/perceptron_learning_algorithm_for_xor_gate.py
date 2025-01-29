"""
This script is for creating a perceptron learning algorithm for XOR gate

Ideally, XOR gate is for linearly inseparable data, which means a single
layer perceptron cannot learn it. so this will most likely not work.
"""

import random

# defining input 1, input 2 and the output
# XOR stands for exclusive OR gate and for the truth table, when both the
# signals are some, the output is 0 and when both the signals are different
# then the value is 1
xor_truth_table = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 1),
]

# initializing the weights and bias randomly
weight_1, weight_2 = random.uniform(-1,1), random.uniform(-1, 1)
bias = random.uniform(-1, 1)

# setting the hyperparameters
learning_rate = 0.1
epochs = 10

# creating a step activation function
def step_function(x: float) -> int:
    """Computes the step function based on input"""
    return 1 if x>= 0 else 0

# training a perceptron
# iterating through the entire code for each epoch
for epoch in range(epochs):
    # keeps track of the error value
    total_error = 0
    # iterating through the table and taking a row of data at a time
    for (inputs, target) in xor_truth_table:
        # unpacking the input variable into input a and b
        input_a, input_b = inputs
        # calculated the weighted sum
        weighted_sum = ((weight_1 * input_a)
                        + (weight_2 * input_b)
                        + bias)
        # passing the weighted sum through the step function
        output = step_function(weighted_sum)

        # calculating the error during this epoch
        epoch_error = target - output
        total_error += abs(epoch_error)

        # updating the bias and weights
        weight_1 += learning_rate * epoch_error * input_a
        weight_2 += learning_rate * epoch_error * input_b
        bias += learning_rate * epoch_error

        print(f"Epoch {epoch + 1}: Total Error = {total_error}")

# Final weights after training
print(f"Final Weights: w1={weight_1}, w2={weight_2}, b={bias}")