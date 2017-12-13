import numpy as np


class Iter:

    def __init__(self, array):
        self.iterative_array = array
        self.i = 0
        self.index = 0

    def int_to_matrix(self, index):
        self.i = 0
        self.index = index
        self.recurse(self.iterative_array, [], [])

    def recurse(self, array, indexing, dim):
        l_n = len(array)
        dim.append(l_n)
        for n in range(0, l_n):
            holder = indexing
            holder.append(n)
            if not isinstance(array[n], list):
                if self.i == self.index:
                    return array[n], holder, dim
                else:
                    self.i +=1
            else:
                self.recurse(array[n], holder, dim)

    def max(self):
        dimensions = self.recurse(self.iterative_array, [], [])[2]
        m = 1
        for d in range(0,dimensions):
            m = m * dimensions[d]
        return m