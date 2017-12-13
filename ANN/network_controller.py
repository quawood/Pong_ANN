import numpy as np

from ANN.Network import Network
from ANN.quadratic_cost import quadratic_cost
from ANN.sigmoid import scalar

network = Network(layer_size=[2,3,2], activation_function=scalar, cost_function=quadratic_cost)

test1 = np.array([4478, 5]).reshape((1,2))
data = np.loadtxt('ANN/ex1data1.txt', delimiter=',')

X1 = data[:, 0:2]
m = X1.shape[0]
y1 = data[:, 2].reshape((m,1))/100000


test2 = np.array([2,2]).reshape((1,2))
X2 = np.array([[1,1],[2,2],[3,3],[4,4],[5,5]])
y2 = np.array([[2,2],[4,4],[6,6],[8,8],[10,10]])

print(X2.flatten())

# network.train(X2,y2, eta=0.01, max_iterations=10000)
#
# print(network.predict(test2))
#


