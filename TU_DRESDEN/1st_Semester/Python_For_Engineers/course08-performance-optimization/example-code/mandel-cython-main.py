import numpy as np
import matplotlib.pyplot as plt
import mandelcy  # our Cython module (for the real work)

import time

# define section of the Gaussian number plane
min_x = -1.5
max_x =  0.15
min_y = -1.5
max_y = min_y + max_x - min_x

# to have same section like numba script
# min_x = -2; max_x =  1; min_y = -1.5

nb_iterations = 255

t1 = time.time()
dataarray = np.zeros((500, 500), dtype=np.uint8)
t2 = time.time()
print("Time needed", t2 - t1)

# execution of the compiled code
mandelcy.create_fractal(min_x, max_x, min_y, nb_iterations, dataarray)

dataarray = dataarray.T[::-1, :]  # Transpose and reverse order along first axis

plt.imshow(dataarray, extent=(min_x, max_x, min_y, max_x), cmap=plt.cm.plasma)
plt.savefig("mandel-cython.png")
plt.show()
