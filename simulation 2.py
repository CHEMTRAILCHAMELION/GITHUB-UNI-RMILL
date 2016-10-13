import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.misc import derivative

TOADiffChangeS = np.linspace(0, 0.1, 1001)  # Time of arrival diff in seconds
TOADiffChangeM = np.linspace(0, (0.1*343.2), 1001)  # Time of arrival diff in meters

SMDist = np.linspace(0, 10, 1001)  # Song Meter distance in meters

i = 1

# matz = np.matrix('TOADiffChangeM; SMDist')

# while i <= 1000:
#    ANSWER = np.arccos(TOADiffChangeM/SMDist[i])
#     i += 1
TranTOADM = np.transpose(TOADiffChangeM)

YUP = np.outer(SMDist, TranTOADM)

print(TOADiffChangeM)
print("YUP = ", YUP)
plt.plot(YUP)
plt.show()

