from ANN.Network import Network
from ANN.sigmoid import  sigmoid
from ANN.quadratic_cost import quadratic_cost
import math
import numpy as np

class Agent:
    def __init__(self, generation):
        self.ann = Network(layer_size=[5, 2, 2], activation_function=sigmoid, cost_function=quadratic_cost)
        self.generation = generation
        self.score = 0
        self.fitness = 0
