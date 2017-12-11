import numpy as np
import sigmoid as sigmoid
class Layer:


    def __init__(self, input_n, output_n, is_input=False, is_output=False):
        self.n = input_n
        self.output_n = output_n

        self.is_input = is_input
        self.is_output = is_output

        #set up layer
        self.W = np.random.uniform(size=(input_n+1, output_n))
        self.a = np.zeros((1, input_n+1))
        self.z = np.zeros((1, input_n+1))
        self.d = np.zeros((1, input_n+1))

    def forward_propogate(self, a):
        self.a = a
        a = np.append([1], a).reshape((1, self.n + 1))
        new_z = a.dot(self.W)

        return new_z

    def backward_propogate(self, d, next_layer, activation_function):
        return next_layer.W.T.dot(d) * activation_function(next_layer.z, derive_z=True)

