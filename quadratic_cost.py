import numpy as np

def quadratic_cost(X, y, hypothesis, derive_a=False):
    m = X.shape[0]
    if not derive_a:
        return (1/2)*(np.power(y - hypothesis(X), 2))
    else:
        return (hypothesis(X) - y)