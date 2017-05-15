import numpy as np
from scipy.integrate import quad


def integrand(t, n, x):
	return np.exp(-x*t) / t**n

def expint(n, x):
	return quad(integrand, 1, np.inf, args(n,x))[0]

vec_expint = np.vectorize(expint)

print(vec_expint(3,np.arange(1.0, 4.0, 0.01)))