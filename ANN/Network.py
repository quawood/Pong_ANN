import numpy as np

from ANN.Layer import Layer


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
            for l in range(0, self.L-1):
                next_z = self.layers[l].forward_propogate(a=prediction)
                prediction = self.activation_function(next_z, derive_z=False)
                self.layers[l+1].z = next_z
                self.layers[l+1].a = prediction

        return prediction

    def gradient_descent(self, eta, max_iterations):
        m = self.X.shape[0]
        for l in range(self.L - 1, 0, -1):
            looping = True
            i  = 0
            while looping:
                weight_size = self.layers[l-1].W.shape[0]
                C_derive = (self.layers[l-1].a.T).dot(self.layers[l].d)
                if not l == self.L-1:

                    last = C_derive[:,C_derive.shape[1]-1].reshape((weight_size,1))
                    first = np.delete(C_derive, np.s_[-1:], axis=1)
                    C_derive = first+last


                self.layers[l-1].W = self.layers[l-1].W - (eta/m) * C_derive

                self.back_prop(self.X, self.y)

                i += 1
                if i == max_iterations:
                    looping = False


    def train(self, X, y, eta, max_iterations):
        m = X.shape[0]
        self.X = X
        self.y = y
        self.back_prop(X,y)

        self.gradient_descent(eta, max_iterations)

    def back_prop(self, X, y):
        output_layer = self.layers[self.L-1]
        nabla_c = self.cost_function(X, y, self.predict, derive_a=True)
        sigmoid_prime = self.activation_function(output_layer.z, derive_z=True)
        output_error = nabla_c*sigmoid_prime

        delta_pred = output_error
        self.layers[self.L-1].d = delta_pred
        m = self.X.shape[0]
        for l in range(self.L-1,0,-1 ):
            if not l == 0:
                weight_size = self.layers[l - 1].W.shape[0]
                delm = delta_pred
                if l < self.L - 1:
                    last = delm[:, delm.shape[1] - 1].reshape((m, 1))
                    first = np.delete(delm, np.s_[-1:], axis=1)
                    delm = first + last


                delta_pred = self.layers[l].backward_propogate(d=delm, next_layer=self.layers[l - 1],
                                                               activation_function=self.activation_function)
                self.layers[l - 1].d = delta_pred