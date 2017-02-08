import numpy as np
from numpy.linalg import norm
from math import sqrt




# Basic Statistical Functions
def kld(P,Q,prec=12):
    _P = np.array(P) / norm(P, ord=1)
    _Q = np.array(Q) / norm(Q, ord=1)
    return round(np.sum([v for v in _P * np.log2(_P/_Q) if not np.isnan(v)]),prec)

def jsd(P,Q,prec=12):
    _P = np.array(P) / norm(P, ord=1)
    _Q = np.array(Q) / norm(Q, ord=1)
    M = 0.5 * (_P + _Q)
    return round(0.5 * (kld(_P,M) + kld(_Q,M)),prec)

def rmse(P,Q,prec=12):
    _P = np.array(P)
    _Q = np.array(Q)
    return round(sqrt(np.mean([np.power(_P - _Q,2)])),prec)
