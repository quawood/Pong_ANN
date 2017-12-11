import numpy as np
from Network import Network
from sigmoid import sigmoid
from quadratic_cost import quadratic_cost

network = Network(layer_size=[1, 1], activation_function=sigmoid, cost_function=quadratic_cost)

test = np.array([3]).reshape((1,1))
X = np.array([[1],[2]])
y = np.array([[2],[4]])
network.train(X,y)
print(network.layers[0].weights)
print(network.predict(test))
