# import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

d = 2  # distance between song meters (m)
c = 343.2  # speed of sound (m/s)
tMax = d/c  # Max time taken between posts. Time equals distance divided by speed.

degs = np.linspace(0, np.pi, 181)  # create array of radians from 0 to pi(180 degrees), 181 points, 1 per degree


def toadiff(x):
    return np.cos(x)  # calculate the time of arrival difference


# Calculate Change in TOADiff over angle
def dytoadiff(toad):
    return abs(derivative(toad, degs, dx=1e-10))


def d2ytoadiff(dytoad):
    return abs(derivative(dytoad, degs, dx=1e-10))

dyTOADiff = dytoadiff(toadiff)
d2yTOADiff = d2ytoadiff(dytoadiff(toadiff))

print(toadiff(degs), " = TOADiff")
print(dyTOADiff, " = dyTOADiff")
plt.plot(abs(toadiff(degs)))
plt.plot(dyTOADiff)
plt.plot(d2yTOADiff)
plt.show()
