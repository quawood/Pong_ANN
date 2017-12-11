
from Layer import Layer
import numpy as np
class Network:
    layers = []

    def __init__(self, layer_size, activation_function, cost_function):
        self.activation_function = activation_function
        self.cost_function = cost_function
        for l in range(0, len(layer_size)):
            holder = layer_size
            holder.append(0)
            is_input = False
            is_output = False
            if l == 0:
                is_input = True
            elif l == len(layer_size)-1:
                is_output = True
            layer = Layer(input_n=holder[l], output_n=holder[l+1], is_input=is_input, is_output=is_output)
            self.layers.append(layer)
        self.L = len(self.layers)

    def predict(self, x):
        prediction = x

        if x.shape[1] == self.layers[0].n:
            self.layers[0].a = x
            for l in range(0, self.L-1):
                next_z = self.layers[l].forward_propogate(a=prediction)
                prediction = self.activation_function(next_z, derive_z=False)
                self.layers[l+1].z = next_z
                self.layers[l+1].a = prediction

        return prediction

    def gradient_descent(self, eta, max_iterations):

        for l in range(0, self.L-1):
            looping = True

            while looping:
                layer = self.layers[l]
                next_layer = self.layers[l + 1]
                C_derive = (layer.a * next_layer.d)
                layer.W = layer.W - eta * C_derive
                if np.all(C_derive) < 0.05:
                    looping = False

    def train(self, X, y):
        output_layer = self.layers[self.L-1]
        output_error = self.cost_function(X, y, self.predict, derive_a=True)*self.activation_function(output_layer.z, derive_z=True)

        delta_pred = output_error
        for l in range(self.L-1,0,-1 ):
            next_d = self.layers[l].backward_propogate(d=delta_pred,next_layer=self.layers[l-1], activation_function=self.activation_function)
            self.layers[l-1].d = next_d

        self.gradient_descent(0.001, 2000)



