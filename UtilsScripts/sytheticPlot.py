import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def model(x,y):
    if (random.randint(0,2) == 1):
        return -0.2273*float(x) -2.1145*float(y) + 11.8885 - 37.7764
    return -0.2273*float(x) -2.1145*float(y) - 37.7764

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-3.0, 3.0, 0.1)
X, Y = np.meshgrid(x, y)
zs = np.array([model(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
