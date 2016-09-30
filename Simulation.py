# import sys
import matplotlib.pyplot as plt
import numpy as np

# def main():
d = 1  # distance between song meters (m)
c = 343.2  # speed of sound (m/s)
a = d/c  # time taken between posts

degs = np.linspace(0, np.pi, 91)  # create x axis array of degrees

DegToRad = np.pi/180 # convert degrees to radians
deg = 45*DegToRad # find our angle in radians

TOAdiff = np.cos(degs)*d # get our TOA difference from the
dyTOA = 10*np.gradient(TOAdiff,degs)

ang = np.arccos(1)

print(TOAdiff[0:5])
print(dyTOA[0:5])

plt.plot(TOAdiff)
plt.plot(dyTOA)
plt.show()
