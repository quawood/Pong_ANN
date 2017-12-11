import numpy as np
from Network import Network
from sigmoid import sigmoid
from quadratic_cost import quadratic_cost

network = Network(layer_size=[5, 5, 3], activation_function=sigmoid, cost_function=quadratic_cost)

test = np.array([1,1,1,1,1]).reshape((1,5))

print(network.predict(test))