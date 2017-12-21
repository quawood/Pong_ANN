import numpy as np


def quadratic_cost(x, y, hypothesis, derive_a=False):
    d = y - hypothesis(x)

    if not derive_a:
        return (1/2)*np.apply_along_axis(magnitude, 1, d)
    else:
        return -(d)


def softmax(x, y, hypothesis, derive_a=False):
    y_size = y.shape[1]
    trans = np.array([np.nonzero(row)[0] for row in y])

    prediction = hypothesis(x)

    sf = np.zeros((x.shape[0], 1))
    i = 0
    for k in trans.flatten():
        sf[i] = np.exp(prediction[i][k]) / (sum(np.exp(prediction[i])))
        i += 1
    return -sum(sf)


def magnitude(v):
    mag = v.dot(v.T)
    return np.power(mag, (1/2))
