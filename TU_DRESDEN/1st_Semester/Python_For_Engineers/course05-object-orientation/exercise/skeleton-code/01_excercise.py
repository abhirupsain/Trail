import numpy as np

from ipydex import IPS, activate_ips_on_exception
activate_ips_on_exception()


# Task 05.1.1
class GeometricObject:

    def __init__(self, middlepoint, XXX):
        self.middlepoint = XX

        self.check_attributes()

    # this method is for convenience you can ignore it
    def __repr__(self):
        return str(list(self.__dict__.items()))

    def check_attributes(self):
        assert isinstance(self.middlepoint, np.ndarray)
        assert self.middlepoint.shape == XXX

    def calc_volume(self):
        msg = "unavailable for this abstract base class"
        raise NotImplementedError(msg)

    def XXX():
        pass

        # ...


exit() # move this line further down or delete it

class Ellipsoid(XXX):
    pass

# ...


# Task 05.1.2
x1 = XXX(np.array([0., 0., 0.]), "black", 2.5, 273)
# ...

# Task 05.1.3 for Cuboid instance x3

assert x3.calc_volume() == XXX


XXX.move(np.array([1, -5, -0.75]))

# check for new position
assert np.all(XXX.middlepoint == XXX)

# Task 05.1.3 for Cuboid instance x3

assert x4.calc_volume() == 4/3*np.pi*x4.r1**3

print(x4.calc_volume(), x4.calc_mass())
x4.move(np.array([300, 20, 1]))
x4.move(np.array([0.3, 0.22, 0.111]))

# check for new position (more robust method)
assert np.allclose(XXX.middlepoint, XXX)


# Task 05.1.4

# create empty list
XXX = []
for i in XXX(10):
    XXX.append(XXX)


# Task 05.1.5

my_cube = XXX(...)
my_sphere = XXX(...)

print(my_cube.calc_distance(XXX))
