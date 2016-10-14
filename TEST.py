from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.misc import derivative


a = np.linspace(0, 10, 11)
b = np.linspace(0, 100, 11)

c = np.outer(a**2, b)

A, B = np.meshgrid(a, b)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(A, B, c)

print(c)
plt.show()

