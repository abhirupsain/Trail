from numpy import sin, cos



# fixed parameter values:
m1 = 0.8
g = 9.81


def xdd_fnc(x, phi, xd, phid, F, m2=0.3, l=0.5):
    """
    Returns the acceleration of the card (depending on the state vector and the force)

    :param x:    cart position (in m)
    :param phi:  pendulum angle (in rad)
    :param xd:   cart velocity (in m/s)
    :param phid: angular velocity of the pendulum angle (in rad/s)
    :param F:    force applied to the cart (in N)
    :param m2:   mass of the pendulum (in kg)
    :param l:    length of the pendulum rod (in m)

    :returns:    acceleration of x

    """

    res = (F + g*m2*sin(2*phi)/2 + l*m2*phid**2*sin(phi))/(m1 + m2*sin(phi)**2)
    return res


def phidd_fnc(x, phi, xd, phid, F, m2=0.3, l=0.5):
    """
    Returns the angulare acceleration of the pendulum (depending on the state vector and the force)

    :param x:    cart position (in m)
    :param phi:  pendulum angle (in rad)
    :param xd:   cart velocity (in m/s)
    :param phid: angular velocity of the pendulum angle (in rad/s)
    :param F:    force applied to the cart (in N)
    :param m2:   mass of the pendulum (in kg)
    :param l:    length of the pendulum rod (in m)

    :returns:    acceleration of phi
    """

    res = -(F*cos(phi) + g*m1*sin(phi) + g*m2*sin(phi) + l*m2*phid**2*sin(2*phi)/2)/(l*(m1 + m2*sin(phi)**2))
    return res
