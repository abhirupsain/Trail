import sys
import numpy as np
from numpy import r_, pi
from matplotlib import pyplot as plt  # used for the plotting at the end


# Move the following line further down as you are advancing.
# Background: actively exiting the program here prevents errors,
# due to usage of undefined names like `XXX`.


sys.exit() # Ends the program here. Otherwise: error messages




# Task 1:

# import the function solve_ivp from the package scipy.integrate
from scipy.XXX import XXX

# import two functions for calculating the accelerations
# (look inside the file `equations_of_motion.py`!)
from equations_of_motion import xdd_fnc #, XXX


# Task 2:

def rhs(XXX, XXX):
    # This function calculates the time derivative z_dot from the state z
    # the 1st argument (the time t) is not needed here

    x, phi, xd, phid = z # unpacking (see overview slides in course01)
    F = 0

    xdd = xdd_fnc(XXX, XXX, ...)
    phidd = XXX


    # Return the derivative of the state vector
    z_dot = r_[xd, phid, XXX, XXX]
    return z_dot


tt = np.linspace(0, 10, 1001)


# Task 3:

zz0 = np.array([XXX,  pi*0.5, XXX, XXX])


# Task 4:

# do the numerical integration
res = solve_ivp(XXX, (tt[0], tt[-1]), XXX, t_eval=tt, rtol=1e-5)

# res: result container
# res.y: result array with shape (4, 1001)
# rows -> state components, columns -> time steps.


# Task 5:

# Unpacking of individual state components.
# Arrays are always unpacked along the 1st axis (rows).
x, phi, xd, phid = XXX

# visualization (more on this in course04):
plt.plot(tt, x)
plt.plot(XYZ)
plt.show()
