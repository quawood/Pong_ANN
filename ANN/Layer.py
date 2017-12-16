import numpy as np
import math

class Layer:
    def __init__(self, input_n, output_n, is_input=False, is_output=False):
        self.n = input_n
        self.output_n = output_n

        self.is_input = is_input
        self.is_output = is_output

        #set up layer



        #USE Glorot and Bengio's method for calculating random weights using special distribution
        r = 0
        if is_input:
            r = 4 * math.sqrt(6 / (output_n))
        elif is_output:
            r = 4 * math.sqrt(6 / (input_n))
        else:
            r = 4 * math.sqrt(6 / (input_n+output_n))

        self.W = np.random.uniform(low = -r, high=r, size=(input_n+1, output_n))

        self.a = np.zeros((1, input_n+1))
        self.z = np.zeros((1, input_n+1))
        self.d = np.zeros((1, input_n+1))

    def forward_propogate(self, a):
        m = a.shape[0]
        a = np.concatenate((np.ones((m,1)),a),axis=1)
        self.a = a
        self.z = a

        new_z = a.dot(self.W)

        return new_z

    def backward_propogate(self, d, next_layer, activation_function):
        part1 = d.dot(next_layer.W.T)
        part2 = activation_function(next_layer.z, derive_z=True)
        return part1*part2

