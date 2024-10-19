import sys
import numpy as np
from numpy import r_, pi
from matplotlib import pyplot as plt # used for the plotting at the end


# Task 1:

# import the function solve_ivp from the package scipy.integrate
from scipy.integrate import solve_ivp

# import two functions for calculating the accelerations
# (look inside the file `equations_of_motion.py`!)
from equations_of_motion import xdd_fnc, phidd_fnc


# Task 2:

def rhs(t, z):
    # This function calculates the time derivative z_dot from the state z
    # the 1st argument (the time t) is not needed here

    x, phi, xd, phid = z # unpacking (see overview slides in course01)
    F = 0

    xdd = xdd_fnc(x, phi, xd, phid, F)
    phidd = phidd_fnc(x, phi, xd, phid, F)

    # Return the derivative of the state vector
    z_dot = r_[xd, phid, xdd, phidd]
    return z_dot


tt = np.linspace(0, 10, 1001)


# Task 3:

zz0 = np.array([0,  pi*0.5, 0, 0])


# Task 4:

# do the numerical integration
res = solve_ivp(rhs, (tt[0], tt[-1]), zz0, t_eval=tt, rtol=1e-5)

# res: result container
# res.y: result array with shape (4, 1001)
# rows -> state components, columns -> time steps.

# Task 5:

# Unpacking of individual state components.
# Arrays are always unpacked along the 1st axis (rows).
x, phi, xd, phid = res.y


# visualization (more on this in course04):
plt.plot(tt, x)
plt.plot(tt, phi)
plt.show()


## The following code is not part of the exercise03.1 but conveniently stored here
## by the supervisor. It is used to generate "pseudo-measurement data"
## for exercise03.2.
## The block will not be executed, but can be quickly converted to "active code"
## by replacing `0` with `1` in the if-statement.

if 0:
    # binary format:
    np.save('measurement-data.npy', res.y)
    # text fomat (human readable, but needs more memory):
    np.savetxt('measurement-data.txt', res.y)

    print ("Files written.")
