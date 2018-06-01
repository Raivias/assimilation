class Vector:
    """
    Class to use of pose, speed, and accelertation. Generally anything that has three directional components
    """
    def __init__(self, a, b, c):
        """
        The three parts of the set
        :param a: x, i, alpha
        :param b: y, j, beta
        :param c: z, k, gamma
        """
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return Vector(a, b, c)

    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        c = self.c - other.c
        return Vector(a, b, c)

    def __mul__(self, other):
        if other is Vector:
            return self.cross_mul(other)

    def cross_mul(self, other):
        """
        Cross multiply
        :param other: Another Vector
        :return: Cross multiple of two matices
        """
        a = (self.b * other.c) - (self.c * other.b)
        b = (self.c * other.a) - (self.a * other.c)
        c = (self.a * other.b) - (self.b * other.a)
        return Vector(a, b, c)

    def scalar_mul(self, other):
        pass
