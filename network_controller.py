import numpy as np
from Network import Network
from sigmoid import sigmoid
from quadratic_cost import quadratic_cost

def scalar(x, derive_z=False):
    if derive_z:
        return np.ones(x.shape)
    else:
        return x


network = Network(layer_size=[1, 1], activation_function=scalar, cost_function=quadratic_cost)

test = np.array([3]).reshape((1,1))
X = np.array([[1],[2],[3],[4]])
y = np.array([[2],[4],[6],[8]])
network.train(X,y)

print(network.predict(test))

