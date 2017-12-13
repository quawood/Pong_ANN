import numpy as np
from Network import Network
from sigmoid import sigmoid, scalar
import math
from quadratic_cost import quadratic_cost, magnitude

network = Network(layer_size=[2,2], activation_function=scalar, cost_function=quadratic_cost)

test1 = np.array([4478, 5]).reshape((1,2))
data = np.loadtxt('ex1data1.txt', delimiter=',')

X1 = data[:, 0:2]
m = X1.shape[0]
y1 = data[:, 2].reshape((m,1))/100000


test2 = np.array([3]).reshape((1,1))
X2 = np.array([[1],[2],[3],[4],[5]])
y2 = np.array([[2],[4],[6],[8],[10]])


network.train(X1,y1, eta=0.0000001, max_iterations=100000)



