import numpy as np


def sigmoid(x, derive_z=False):
    sig = 1/(1 + np.exp(-x))
    if not derive_z:
        return sig
    else:
        return sig*(1-sig)


def scalar(x, derive_z=False):
    if not derive_z:
        return x
    else:
        return np.ones(x.shape)


def reLu(x, derive_z=False):
    if not derive_z:
        return np.maximum(x, 0)
    else:
        return x>0

def tanh(x, derive_z=False):
    htan = (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
    if not derive_z:
        return htan
    else:
        return 1 - np.power(htan, 2)