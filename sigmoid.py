import numpy as np
def sigmoid(x, derive_z=False):
    sig = 1/(1 + np.exp(-x))
    if not derive_z:
        return sig
    else:
        return sig*(1- sig)

