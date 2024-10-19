from numpy import sin, cos, pi, array, eye
from scipy.integrate import ode

l = 0.5


def rhs(t, y, m1, m2):
    """
    Calculation of the time derivative of the state of our system.
    Assumption: constant pendulum length.
    """

    # unpacking the components of the state vector
    x, phi, xd, phid = y

    F = 0
    g = 9.81

    xdd = (F + g * m2 * sin(2 * phi) / 2 + l * m2 * phid ** 2 * sin(phi)) / (
        m1 + m2 * sin(phi) ** 2
    )
    phidd = -(g * (m1 + m2) * sin(phi) + (F + l * m2 * phid ** 2 * sin(phi)) * cos(phi)) / (
        l * (m1 + m2 * sin(phi) ** 2)
    )

    return [xd, phid, xdd, phidd]
