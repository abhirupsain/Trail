import numpy as np
from scipy import optimize

def fnc2(x):
    return (x + 2.3*np.cos(x) - 1)**2 # quadratic equation error

res = optimize.minimize(fnc2, 0) # Optimization with initial estimate 0
# check:
print(res.x, res.x + 2.3*np.cos(res.x)) # -> [-0.7236326] [1.00000004]

# now with limits and with changed start estimation -> other solution
res = optimize.minimize(fnc2, 0.5, bounds=[(0, 3)])
# check:
print(res.x, res.x + 2.3*np.cos(res.x)) # -> [2.03999505] [1.00000003]
