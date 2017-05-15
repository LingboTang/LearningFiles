import numpy as np


def mypolyval(p, x):
	_p = list(p)
	res = _p.pop(0)
	while _p:
		res = res * x + _p.pop(0)
	return res

vpolyval = np.vectorize(mypolyval, excluded=['p'])
vpolyval(p=[1,2,3],x=[0,1])