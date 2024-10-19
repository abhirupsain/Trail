import numpy as np
import matplotlib.pyplot as plt
import mandelcy # unser Cython Modul (macht die eigentliche Arbeit)

import time


# define section of the Gaussian number plane
min_x = -1.5
max_x =  0.15
min_y = -1.5
max_y = min_y + max_x - min_x

# to have same section like numba script
min_x = -2; max_x =  1; min_y = -1.5

nb_iterations = 255

dataarray = np.zeros((1000, 1000), dtype=np.uint8)

# execution of the compiled code

t0 = time.time()
mandelcy.create_fractal(min_x, max_x, min_y, nb_iterations, dataarray)
print(time.time() - t0)

# Transpose and reverse order along first axis
dataarray = dataarray.T[::-1, :]

plt.imshow(dataarray, extent=(min_x, max_x, min_y, max_x), cmap=plt.cm.plasma)
plt.savefig("mandel-cython.png")
plt.show()
