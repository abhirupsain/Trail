"""
Example script on numpy broadcasting
"""

import numpy as np
import time

E = np.ones((4, 3))  # -> shape=(4, 3)
b = np.array([-1, 2, 7])  # -> shape=(3,)
print(E*b)  # -> shape=(4, 3)

b_13 = b.reshape((1, 3))
print(E*b_13)  # -> shape=(4, 3)

print("\n"*2, "Caution, the next statements result in an error.")
time.sleep(2)

b_31 = b_13.T  # transposing -> shape=(3, 1)
print(E*b_31) # broadcasting error
