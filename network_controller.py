import numpy as np
from Network import Network
from sigmoid import sigmoid, scalar
import math
from quadratic_cost import quadratic_cost, magnitude

network = Network(layer_size= [1,1,1], activation_function=scalar, cost_function=quadratic_cost)

test = np.array([3]).reshape((1,1))
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([[2],[4],[6],[8],[10]])

network.train(X,y, 0.01, 10000)

print(network.predict(np.array([[3]]).reshape((1,1))))

