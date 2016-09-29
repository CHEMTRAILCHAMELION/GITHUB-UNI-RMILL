# import sys
import matplotlib.pyplot as plt
import numpy as np

# def main():
d = 2  # distance between song meters (m)
c = 343.2  # speed of sound (m/s)
a = d/c  # time taken between posts

degs = np.linspace(0, 2*np.pi, 181)  # create x axis array of degrees

DegToRad = np.pi/180
deg = 45*DegToRad

TOAdiff = np.cos(degs)

ang = np.arccos(1)

print(degs)
print(TOAdiff)

plt.plot(TOAdiff)
plt.show()
