"""Mathmatical 3d plane."""
from engine.threed.point import Point
from engine.threed.vector import Vector
from engine.threed.line import Line
from engine.tools.options import Options


class Plane:
    """
    Mathmatical 3d plane.

    >>> plane = Plane(Point(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9))
    >>> str(plane).replace("x=", "").replace("y=", "").replace("z=", "")
    'Plane(position=Point(1, 2, 3), direction_a=Vector(4, 5, 6), direction_b=Vector(7, 8, 9))'
    """

    def __init__(self, position, direction_a, direction_b):
        """
        Initialize plane with position and two directions.

        Args:
            position(Point): start of plane
            direction_a(Vector): first direction of plane.
            direction_b(Vector): second direction of plane.

        Raises:
            TypeError: when position is not a point or directions are not a vector
        """
        if isinstance(position, Point) and \
            isinstance(direction_a, Vector) and \
                isinstance(direction_b, Vector):
            self.position = position
            self.direction_a = direction_a
            self.direction_b = direction_b
        else:
            raise TypeError("One or all types for plane parameters are wrong")

    def __repr__(self):
        """
        Returns:
            str: readable representation of the values of this class.
        """
        text = "Plane(position=%(position)s, " % self.__dict__
        text += "direction_a=%(direction_a)s, direction_b=%(direction_b)s)" % self.__dict__
        return text

    def __eq__(self, other):
        """
        Args:
            other(Plane): another plane to use for comparison.

        Returns:
            bool: True when both planes are equal otherwise false
        """
        if isinstance(other, Plane):
            return self.position == other.position and \
               self.direction_a == other.direction_a and \
               self.direction_b == other.direction_b

        return False

    def point(self, factor_a, factor_b):
        """
        Provide point on plane by two factors (0=start point, 1=end point).

        Args:
            factor_a(float or int): the factor to control which point (0=start point, 1=end point).
            factor_b(float or int): the factor to control which point (0=start point, 1=end point).

        Raises:
            TypeError: when given parameter is not an int or a float
        """
        if isinstance(factor_a, (int, float)) and isinstance(factor_b, (int, float)):
            return self.position \
                + self.direction_a.scaled(factor_a) \
                + self.direction_b.scaled(factor_b)

        raise TypeError("Not all parameter are either an int or a float")

    def intersection(self, other):
        """
        Calculate intersection between given plane and a line.

        Args:
            other(Line): line to find intersection point.

        Returns:
            Point: found intersection point or None if not found.

        Raises:
            TypeError: when given parameter is not a line.

        Note:
            The method does not check whether a found point lies inbetween
            the start point and end point of the line or inside the limits
            defined for the plane.
        """
        if isinstance(other, Line):
            line = other
            # p1 + a * v1               = p2 + b * v2 + c * v3           | - p1
            #      a * v1               = (p2 - p1) + b * v2 + c * v3    | x v3
            # a * (v1 x v3)             = (p2 - p1) x v3 + b * (v2 x v3) | x (v2 x v3)
            # a * (v1 x v3) x (v2 x v3) = ((p2 - p1) x v3)) x (v2 x v3)
            vector_a = line.direction.cross_product(self.direction_b) \
                .cross_product(self.direction_a.cross_product(self.direction_b))
            vector_b = (self.position - line.position).cross_product(self.direction_b) \
                .cross_product(self.direction_a.cross_product(self.direction_b))

            if abs(vector_a.x) > Options.PRECISION:
                return line.point(vector_b.x / vector_a.x)
            if abs(vector_a.y) > Options.PRECISION:
                return line.point(vector_b.y / vector_a.y)
            if abs(vector_a.z) > Options.PRECISION:
                return line.point(vector_b.z / vector_a.z)

            # no intersection
            return None

        raise TypeError("Given parameter is not a line")
