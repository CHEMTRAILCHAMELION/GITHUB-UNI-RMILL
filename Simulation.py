import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.misc import derivative


d = 2  # distance between song meters (m)
>>>>>>> origin/master
c = 343.2  # speed of sound (m/s)
tMax = d/c  # Max time taken between posts. Time equals distance divided by speed.

<<<<<<< HEAD
degs = np.linspace(0, np.pi, 91)  # create x axis array of degrees

DegToRad = np.pi/180 # convert degrees to radians
deg = 45*DegToRad # find our angle in radians

TOAdiff = np.cos(degs)*d # get our TOA difference from the
dyTOA = 10*np.gradient(TOAdiff,degs)
=======
degs = np.linspace(0, np.pi, 181)  # create array of radians from 0 to pi(180 degrees), 181 points, 1 per degree

x, y, z = symbols('x y z')

<<<<<<< HEAD
test = diff(cos(x), x)


def toadiff(a):
    return np.cos(a)  # calculate the time of arrival difference
||||||| merged common ancestors
def toadiff(x):
    return np.cos(x)  # calculate the time of arrival difference
=======
def toadiff(x):
    return np.cos(x)  # calculate the time of arrival difference
>>>>>>> origin/master

>>>>>>> a323ac0fbdba562a729e405a78aaa4b7621ce574

<<<<<<< HEAD
print(TOAdiff[0:5])
print(dyTOA[0:5])

plt.plot(TOAdiff)
plt.plot(dyTOA)
=======
# Calculate Change in TOADiff over angle
def dytoadiff(toad):
    return abs(derivative(toad, degs, dx=1e-10))


# def d2ytoadiff(dytoad):
 #   return abs(derivative(dytoad, degs, dx=1e-10))

dyTOADiff = dytoadiff(toadiff)
# d2yTOADiff = d2ytoadiff(dytoadiff(toadiff))

print(toadiff(degs), " = TOADiff")
print(dyTOADiff, " = dyTOADiff")
print(test)
plt.plot(abs(toadiff(degs)))
plt.plot(dyTOADiff)
<<<<<<< HEAD
# plt.plot(d2yTOADiff)
||||||| merged common ancestors
plt.plot(d2yTOADiff)
=======
plt.plot(d2yTOADiff)
>>>>>>> origin/master
>>>>>>> a323ac0fbdba562a729e405a78aaa4b7621ce574
plt.show()

