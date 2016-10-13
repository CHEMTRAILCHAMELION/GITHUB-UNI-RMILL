import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.misc import derivative

a = np.linspace(0, 10, 11)

c = np.outer(a, a)


print(c)