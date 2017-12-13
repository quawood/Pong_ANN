import numpy as np


def quadratic_cost(x, y, hypothesis, derive_a=False):
    d = y - hypothesis(x)
    if not derive_a:
        return (1/2)*np.apply_along_axis(magnitude, 1, d)
    else:
        return -(d)


def magnitude(v):
    mag = v.dot(v.T)
    return np.power(mag, (1/2))