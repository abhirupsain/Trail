import numpy as np
import scipy.interpolate as ip
import matplotlib.pyplot as plt

# original data
x = [1, 2, 3, 4]
y = [2, 0, 1, 3]

plt.plot(x, y, "bx")  # blue crosses
plt.savefig("interpolation0.pdf")

# create linear interpolator function
fnc1 = ip.interp1d(x, y)

# achieve higher x-resolution by evaluation of fnc1
xx = np.linspace(1, 4, 20)
plt.plot(xx, fnc1(xx), "r.-")  # red solid line and dots
plt.savefig("interpolation1.pdf")
plt.show()
