

# In this exercise the order of the given code snippets is arbitrary
# For each task you select the appropriate the block(s), uncomment and
# make your adaptions at `(...)`

# Use the ability of Spyder (or another IDE), to move blocks
# with multiple lines and to blockwise (un)comment!


#import numpy as ...
#from scipy.integrate import odeint
#import matplotlib.pyplot as plt

# optional debugging tool
#from ipydex import IPS


# ###############################################################

# np.loadtxt(...)

# ###############################################################

#for k in range(1, ...):
#    fname = f"data{k}.txt"
#    print(fname)
#    try:
#        x = np.loadtxt(...)
#    except ValueError as ve:
#        print("Error:", ve)
#    else:
#        # Task 3:
#        rhs = create_rhs_from_1darr(x)
#        rhs_list.append(rhs)

# ###############################################################

#def rhs_factory(A):
#   """
#   factory function, to "produce" a `solve_ivp`-compatible
#   rhs function based on a matrix `A`.
#   """
#
#    # ensure that A is a square matrix
#    assert ...
#
#
#    # define the new function (this is the 'product' of the factory)
#    def rhs(..., ...):
#       # ODE: derivative of the state is Matrix A times state vector
#       ...
#       return x_dot
#
#
#    # add the state dimension as additional attribute to the function object
#    rhs.state_dimension = ...
#
#    # return the procuct of the fatory (the created rhs function)
#    return rhs

# ###############################################################

#def create_rhs_from_1darr(arr):
#    n = arr.shape[0]
#    n2 = int(np.sqrt(n))
#    arr2 = arr.reshape(n2, -1)
#
#    return rhs_factory(arr2)



# ###############################################################

# implement equation x_dot = A*x:

#def rhs(time, state):
#    x_dot = np.dot(A, state)
#
#    return x_dot


# ###############################################################

#rhs_list = []

# ###############################################################

# apply the `simulate` function (3 options).
# option a): classic by ordinary for-loop

#for rhs in rhs_list:
#    simulate(...)


# option b): in functional programming style with `map`
# `map(...)` creates an iterator object
# `list(...)` iterates over such an iterator object and thus causes the execution of the function
#list(map(...))


# ###############################################################

#plt.show()

# ###############################################################

# Task 9
#rhs_list = filter(lambda ...)

# ###############################################################

#tt = np.linspace(0, 5, int(1e3))

#def simulate(rhs):
#    """
#    Perform the simulation for a given rhs function object
#
#    :param rhs:     `solve_ivp`-compatible function object
#
#    :return:     None
#    """
#
#    np.random.seed(75)  # initialize random generator -> reproducibility
#    xx0 = np.random.rand(rhs.state_dimension)
#
#    # run the simulation
#    # (tt is global variable, (tt[0], tt[-1]) is a 2-tuple with first and last time instant)
#    res = solve_ivp(rhs, (tt[0], tt[-1]), xx0, t_eval=tt)
#
#
#    # Extract time evolution of the first state component
#    x1 = res.y[0, :]
#
#    plt.plot(tt, x1)

