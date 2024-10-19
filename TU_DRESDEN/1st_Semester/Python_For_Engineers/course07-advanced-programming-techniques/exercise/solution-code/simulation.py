
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from data_tools import create_rhs_from_1darr

def simulate(rhs):
    """
    Perform the simulation for a given rhs function object

    :param rhs:     `solve_ivp`-compatible function object

    :return:     None
    """

    np.random.seed(75)  # initialize random generator -> reproducibility
    xx0 = np.random.rand(rhs.state_dimension)

    # run the simulation
    # (tt is global variable, (tt[0], tt[-1]) is a 2-tuple with first and last time instant)
    res = solve_ivp(rhs, (tt[0], tt[-1]), xx0, t_eval=tt)

    # Extract time evolution of the first state component
    x1 = res.y[0, :]

    plt.plot(tt, x1)


# create a list for the function objects
rhs_list = []

for k in range(1, 5):
    fname = f"data{k}.txt"
    print(fname)
    try:
        x = np.loadtxt(fname)
    except ValueError as ve:
        print("Error:", ve)
    else:
        rhs = create_rhs_from_1darr(x)
        rhs_list.append(rhs)

tt = np.linspace(0, 5, int(1e3))


# two different variants to restrict the simulation to systems with
# state dimension smaller than 3 (see task 9)

if 0:  # switch filtering on/off completely
    if 0:  # distinguish between `filter`-func and list comprehension
        rhs_list = filter(lambda q: q.state_dimension < 3, rhs_list)
    else:
        # task 11 (part 1)
        rhs_list = [q for q in rhs_list if q.state_dimension < 3]


# Apply the `simulate` function from above.
# `map(...)` creates an iterator
# `list(...)` evaluates the iterator and thereby causes the actual execution
# the application of the `simulate` function:

res = list(map(simulate, rhs_list))


# task 11 (part 2)
res = [simulate(rhs_func) for rhs_func in rhs_list]

plt.show()
