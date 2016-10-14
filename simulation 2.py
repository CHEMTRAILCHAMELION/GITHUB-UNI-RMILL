from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.misc import derivative

TOADiffChangeS = np.linspace(0, 0.5, 101)  # Time of arrival diff in seconds
TOADiffChangeM = np.linspace(0, (0.5*343.2), 101)  # Time of arrival diff in meters

SMDist = np.linspace(0, 2, 21)  # Song Meter distance in meters

i = 1

# matz = np.matrix('TOADiffChangeM; SMDist')

# while i <= 1000:
#    ANSWER = np.arccos(TOADiffChangeM/SMDist[i])
#     i += 1

AoverH = np.outer(TOADiffChangeS, 1/SMDist)
Angles = 90-((180/np.pi) * np.arccos(AoverH))

X, Y = np.meshgrid(SMDist, TOADiffChangeS)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Angles)
ax.plot_wireframe(X, Y, 15, color='red')

# print(TOADiffChangeM)
# print("YUP = ", YUP)
# plt.plot(YUP)
print(AoverH)
print('Angles = ', Angles)
ax.set_xlabel('Song Meter Distance (m)')
ax.set_ylabel('Time of Arrival Diff Error(s)')
ax.set_zlabel('Error in Angle (degs)')
plt.show()

