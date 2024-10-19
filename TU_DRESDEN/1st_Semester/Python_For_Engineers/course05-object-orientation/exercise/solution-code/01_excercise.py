import numpy as np

from ipydex import IPS, activate_ips_on_exception
activate_ips_on_exception()


# Task 05.1.1
class GeometricObject:

    def __init__(self, middlepoint, color, density, temperature):
        self.middlepoint = middlepoint
        self.color = color
        self.density = density
        self.temperature = temperature  # in K

        self.check_attributes()

    def __repr__(self):
        return str(list(self.__dict__.items()))

    def check_attributes(self):
        assert isinstance(self.middlepoint, np.ndarray)
        assert self.middlepoint.shape == (3,)
        assert isinstance(self.color, str)
        assert isinstance(self.density, (float, int))
        assert isinstance(self.temperature, (float, int))

    def calc_volume(self):
        msg = "unavailable for this abstract base class"
        raise NotImplementedError(msg)

    def calc_mass(self):
        return self.calc_volume()*self.density

    def move(self, target_direction):
        assert isinstance(target_direction, np.ndarray)
        assert target_direction.shape == self.middlepoint.shape
        self.middlepoint += target_direction

    # Task 05.1.5 (only this method)
    def calc_distance(self, other):
        assert isinstance(other, GeometricObject)
        return np.sqrt(np.sum((self.middlepoint - other.middlepoint)**2))


class Ellipsoid(GeometricObject):

    def __init__(self, r1, r2, r3, middlepoint, color="white", density=1, temperature=300):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

        # call the "constructor" of the base class
        GeometricObject.__init__(self, middlepoint, color, density, temperature)

    def calc_volume(self):
        return 4/3*np.pi*self.r1*self.r2*self.r3


class Cuboid(GeometricObject):

    def __init__(self, a, b, c, middlepoint, color="white", density=1, temperature=300):
        self.a = a
        self.b = b
        self.c = c

        # call the "constructor" of the base class
        GeometricObject.__init__(self, middlepoint, color, density, temperature)


    def calc_volume(self):
        return self.a*self.b*self.c


class Sphere(Ellipsoid):
    def __init__(self, radius, middlepoint, color="white", density=1, temperature=300):

        # call the "constructor" of the base class (Ellipsoid)
        Ellipsoid.__init__(self, radius, radius, radius, middlepoint, color, density, temperature)


class Cube(Cuboid):
    def __init__(self, a, middlepoint, color="white", density=1, temperature=300):

        # call the "constructor" of the base class (Ellipsoid)
        Cuboid.__init__(self, a, a, a, middlepoint, color, density, temperature)


# Task 05.1.2
x1 = GeometricObject(np.array([0., 0., 0.]), "black", 2.5, 273)
x2 = Ellipsoid(3, 2, 1, np.array([0., 0., 0.]))
x3 = Cuboid(2, 3, 4, np.array([0., 0., 0.]))
x4 = Sphere(2, np.array([0., 0., 0.]))
x5 = Cube(2.5, np.array([0., 0., 0.]))


# Task 05.1.3 for Cuboid instance x3

assert x3.calc_volume() == 24.0


print(x3.calc_volume(), x3.calc_mass())
x3.move(np.array([1, -5, -0.75]))
x3.move(np.array([-3, 7, 0.5]))

# check for new position
assert np.all(x3.middlepoint == np.array([-2, 2, -0.25]))

# Task 05.1.3 for Sphere instance x3

assert x4.calc_volume() == 4/3*np.pi*x4.r1**3

print(x4.calc_volume(), x4.calc_mass())
x4.move(np.array([300, 20, 1]))
x4.move(np.array([0.3, 0.22, 0.111]))

# check for new position (more robust method)
assert np.allclose(x4.middlepoint, np.array([300.3, 20.22, 1.111]))


# Task 05.1.4

# create empty list
cubes = []
for i in range(10):
    cubes.append(Cube(a=10, middlepoint=np.random.random(3)))


# Task 05.1.5

my_cube = Cube(1, np.array([3, 0, 0]))
my_sphere = Sphere(1, np.array([0, 4, 0]))

print(my_cube.calc_distance(my_sphere))
