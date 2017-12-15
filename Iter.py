import numpy as np
import copy

class Iter:


    def __init__(self, index):
        self.i = 0
        self.index = index
        self.index_value = 0
        self.index_vector = []
        self.running = False

    def int_to_matrix(self, array):
        self.i = 0
        self.index_vector = []
        self.index_value = 0
        self.running = True
        self.recurse(array, [])
        return self.index_value, tuple(self.index_vector)

    def recurse(self, array, indexing):
        l_n = len(array)
        for n in range(0, l_n):
            if self.running:
                now = copy.deepcopy(indexing)
                now.append(n)

                if not isinstance(array[n], list):

                    if self.i == self.index:
                        self.index_value = array[n]
                        self.index_vector = now
                        self.running = False
                    self.i = self.index + 1

                else:
                    self.recurse(array[n], now)
