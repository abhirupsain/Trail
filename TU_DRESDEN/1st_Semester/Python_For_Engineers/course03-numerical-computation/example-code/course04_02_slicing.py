import numpy as np
a = np.arange(18) * 2.0  # 1d array
A = np.array( [ [0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11] ] )  # 2d array

x1 = a[3] #  element with index 3 (-> 6.0)
x2 = a[3:6] # elements 3 to 5   -> array([  6.,   8.,  10.])
x3 = a[-3:] # from 3rd-last element to the end -> array([30., 32., 34.])
# Caution: a, x2 and x3 share the data (they are only "views" to the data)
a[-2:] *= -1 # change the data in a and observe the change in x3:
print(x3) # -> [-30., -32., -34.]

# for 2d arrays: first index -> row; second index column; separator: comma
y1 = A[:, 0] # first column of A (index 0)
y2 = A[1, :3 ] # first three elements of the second column (index 1)
