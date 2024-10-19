"""
Module with auxilliary functions

"""

import numpy as np



def create_rhs_from_1darr(arr):
    n = arr.shape[0]
    n2 = int(np.sqrt(n))
    arr2 = arr.reshape(n2, -1)

    return rhs_factory(arr2)


def rhs_factory(A):
    """
    factory function, to "produce" a `solve_ivp`-compatible
    rhs function based on a matrix `A`.
    """

    n, m = A.shape
    # ensure that A is a square matrix
    assert n == m

    # define the new function (this is the 'product' of the factory)
    def rhs(time, state):
        # ODE: derivative of the state is Matrix A times state vector
        x_dot = np.dot(A, state)  # alternative: A@state

        return x_dot

    # add the state dimension as additional attribute to the function object
    rhs.state_dimension = n


    # return the procuct of the fatory (the created rhs function)
    return rhs
