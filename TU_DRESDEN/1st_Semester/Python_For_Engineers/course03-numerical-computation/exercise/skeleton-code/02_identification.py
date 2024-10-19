
# Move the following line further down as you are advancing.
# Background: actively exiting the program here prevents errors,
# due to usage of undefined names like `XXX`.


sys.exit() # Ends the program here. Otherwise: error messages







import sys
import numpy as np


# Task 1:

# import the function solve_ivp from the package scipy.integrate


# import two functions for calculating the accelerations
# (look inside the file `equations_of_motion.py`!)
from equations_of_motion import xdd_fnc, XXX


# load pseudo measurement data in binary format
zz_res_target = np.load(XXX)

# -> this is a 2d array with shape = (4, 1001), i.e. 4 rows, 1001 cols.
# meaning of rows: x, phi, xd, phid
# meaning of cols: time instant


## alternatively: load data in text format:
# zz_res_target = np.loadtxt(XXX)


# Task 2:

def min_target(p):
    """
    This function is called repeatedly by the optimization algorithm.
    On every call it performs an simlation and calculates the difference
    to the measurement data.

    :param  p:  sequence of two parameter values (m2, l)

    :returns:   err – non-negative real valued error measure
                (how "wrong the simulation result is")
    """

    m2, l = XXX # unpacking the parameter vector

    # Task 3:

    # Define a function INSIDE another function.
    # works and is often useful!
    # The inner function has reading access on the namespace
    # of the outer function (as with global variables).

    # The outer function can not access the namespace of the inner function.

    def rhs(t, z):
        """
        Righthand side of the equations of motion
        (Note: this depends on m2 and l from the surrounding namespace).
        """
        x, phi, xd, phid = XXX # unpacking
        F = 0

        # m2 and l come from the namespace one level higher
        # (you might want to look again into `eqations_of_motion.py`
        # to check the signature of these functions:)
        xdd = xdd_fnc(XXXXXXXX, m2, l)
        phidd = phidd_fnc(XXXXXXXXX,  XXX, XXX)

        # return derivative of the state vector
        return XXX

    # end of the inner function definition of rhs


    # Task 4:

    # For performance reasons, it would be better to define these two variables
    # outside of min_target, but for didactic reasons it is simpler to define
    # them here:

    # array with evaluation times (should be consistent with the measured data)
    tt = np.linspace(0, 10, XXX)

    # select a consistent initial state (4 values) for the simulation
    # from the measurement data (-> choose the first column)
    zz0 = XXX

    # do the simulation (get result container)
    sim_res = solve_ivp(XXX, (XXXX, XX), YYY, t_eval=tt, rtol=1e-5)

    # select the state vector (which we call "z" but scipy calls "y")
    zz_res = XXX.y

    # Task 5:

    # Calculate the difference of the x-positions (first line in each case)
    # then square (...**2),
    # then add up (applying np.sum)
    err = np.sum( (XXX[YYY, ZZZ] - XXX[YYY, ZZZ])**XXX )

    # Status message and output (to assess progress of optimization)
    print("simulation ready. p =", p, " equation error:", err)

    return err # return scalar (real valued) error measure

# end of the outer function definition (min_target)


# Task 6:

p0 = np.array([.5, .7]) # Startschätzung für m2 und l

# import the function minimize from the module scipy.optimize
from XXX.XXX import XXX

# do the optimization (call the algorithm, which internally repeatedly calls min_target)
min_res = minimize(XXX, XXX, method="Nelder-Mead")

print("\n", "minimization result (data structure):", min_res, "\n")
print("estimated paremeters (m2, l):", min_res.x, "\n")
