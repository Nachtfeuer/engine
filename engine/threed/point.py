"""Mathmatical 3d point."""
from engine.threed.vector import Vector


class Point:
    """
    Mathmatically 3d point

    >>> Point()
    Point(x=0, y=0, z=0)
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        Args:
            x (float): 3d x coordinates (default: 0.0)
            y (float): 3d y coordinates (default: 0.0)
            z (float): 3d z coordinates (default: 0.0)
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Point(x=%(x)g, y=%(y)g, z=%(z)g)" % self.__dict__

    def __sub__(self, other):
        """
        Args:
            other(Point): another point to use for subtraction.

        Returns:
            Vector: difference of two points.
        """
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        raise TypeError("You cannot subtract a value of type %s from a point" % type(other))

    def __add__(self, other):
        """
        Get translated point.

        Args:
            other(vector): a vector to add its coordinates to the point.

        Returns:
            Point: translated point
        """
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)

        raise TypeError("You can not add a value of type %s to a point" % type(other))

    def __eq__(self, other):
        """
        Args:
            other(Point): another point to use for comparison.

        Returns:
            bool: True when both points are equal otherwise false
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z

        return False

    @staticmethod
    def from_vector(vector):
        """
        Args:
            vector(Vector): a vector to use to create a point from it.

        Returns:
            Point: a point

        Raises:
            TypeError: when given parameter is not a vector
        """
        if isinstance(vector, Vector):
            return Point(vector.x, vector.y, vector.z)

        raise TypeError("You cannot create a point from a value of type %s" % (type(vector)))
