class Sphere():
    """A class modeling a spherical objects"""

    def __init__(self, radius, midpoint=(0, 0, 0)):
        """
        Initialization method. Automatically executed when an object is created.
        Corresponds (approximately) to the 'constructor' in other programming
        languages.
        """

        # set attributes:
        self.radius = radius
        self.midpoint = midpoint

    def calc_volume(self):
        r = self.radius
        return (4/3)*np.pi*(r**3)
