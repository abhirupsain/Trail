import numpy as np
import matplotlib.pyplot as plt

N = 25
xx = np.linspace(0, 5, N)

# cool trick: two assignments in one line
m, n = 2 , -1

# evaluate equation of straigt line: y = m*x + n
yy = np.polyval([m, n], xx)
yy_noisy = yy + np.random.randn(N)  # add some random noise

# create linear fit (regression 1st order polynomial)
mr, nr = np.polyfit(xx, yy_noisy, 1)  # calculate fit
yyr = np.polyval([mr, nr], xx)  # evaluate the function

plt.plot(xx, yy, 'go--', label="original")
plt.plot(xx, yy_noisy,'k.', label="noisy data")
plt.plot(xx, yyr,'r-', label="regression")
plt.legend()
plt.savefig("regression.png")

plt.show()
