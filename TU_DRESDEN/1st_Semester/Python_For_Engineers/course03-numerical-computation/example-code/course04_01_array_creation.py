import numpy as np
x0 = np.arange(10) # like range(...) but with arrays
x1 = np.linspace(-10, 10, 200)
        # 200 values: array([-10., -9.899497, ..., 10])
x2 = np.logspace(1, 100, 500) # 500 values, always same ratio

x3 = np.zeros(10) # see also: np.ones(...)
x4 = np.zeros( (3, 5) ) # Caution: takes only **one** argument! (= shape)

x5 = np.eye(4) # 4x4 unity matrix
x6 = np.diag( (4, 3.5, 23) ) # 3x3 diagonal matrix with specified diagonal elements

x7 = np.random.rand(5) # array with 5 random numbers (each between 0 and 1)
x8 = np.random.rand(4, 2) # array with 8 random numbers and shape = (4, 2)

from numpy import r_, c_ # "index tricks" for rows and columns
x9 = r_[6, 5, 4.2] # array([ 6.,  5.,  4.2])
x10 = r_[x9, -84, x3[:2]] # array([ 6.,  5.,  4.2,  -84, 0.,  1.])
x11 = c_[x9, x6 , x5[:-1, :]] # stacking in column direction

assert x11.shape == (3, 8)
