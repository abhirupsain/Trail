import numpy as np
from scipy.integrate import solve_ivp

delta = .1
omega_2 = 2**2
def rhs(t, z):
    """ rhs means 'right hand side [function]' """
    # argument t must me present in the function head, but it can be ignored in the body
    z1, z2  = z # unpacking the state vector (array) into its two components
    z1_dot = z2
    z2_dot = -(2*delta*z2 + omega_2*z1)
    return [z1_dot, z2_dot]

tt = np.arange(0, 100, .01) # independent variable (time)
z0 = [10, 0]   # initial state for z1 and z2 (=y, and y_dot)
res = solve_ivp(rhs, (tt[0], tt[-1]), z0, t_eval=tt) # calling the integration algorithm
zz = res.y # array with the time-development of the state
           # (rows: components; columns: time steps)

from matplotlib import pyplot as plt
plt.plot(tt, zz[0, :]) # plot z1 over t
plt.show()
