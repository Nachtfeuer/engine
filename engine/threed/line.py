"""Mathmatical 3d line."""
from engine.threed.point import Point
from engine.threed.vector import Vector
from engine.tools.options import Options


class Line:
    """
    Mathmatical 3d line.

    >>> line = Line(Point(1, 1, 1), Vector(2, 2, 2))
    >>> line
    Line(position=Point(x=1, y=1, z=1), direction=Vector(x=2, y=2, z=2))
    """

    def __init__(self, position, direction):
        """
        Initialize line with position and direction.

        Args:
            position(Point): start of line
            direction(Vector): direction of line.

        Raises:
            TypeError: when position is not a point or direction is not a vector
        """
        if isinstance(position, Point) and isinstance(direction, Vector):
            self.position = position
            self.direction = direction
        else:
            raise TypeError("One or all types for line parameters are wrong")

    def length(self):
        """
        Returns:
            float: length of line
        """
        return self.direction.length()

    def __repr__(self):
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Line(position=%(position)s, direction=%(direction)s)" % self.__dict__

    def __eq__(self, other):
        """
        Args:
            other(Line): another line to use for comparison.

        Returns:
            bool: True when both lines are equal otherwise false
        """
        if isinstance(other, Line):
            return self.position == other.position and self.direction == other.direction

        return False

    def angle(self, other):
        """
        Args:
            other(Line): another line to use for calculation of angle.

        Returns:
            Vector: angle between two lines.

        Raises:
            TypeError: when given parameter is not a line.
        """
        if isinstance(other, Line):
            return self.direction.angle(other.direction)

        raise TypeError("You cannot calculate an angle " +
                        "between a line and type %s" % type(other))

    def distance(self, obj):
        """
        Args:
            object(Point): distance to a point.

        Returns:
            float: distance to the point

        Raises:
            TypeError: when given parameter is not a point.
        """
        if isinstance(obj, Point):
            point = obj
            vector_a = point - self.position
            vector_b = vector_a.projection(self.direction)
            return (vector_a - vector_b).length()

        raise TypeError("You can not calculate distance " +
                        "between a line and type %s" % type(obj))

    def has_point(self, point):
        """
        Verifies that point is on the line.

        Args:
            point(Point): point to verify

        Returns:
            bool: True when point is on the line otherwise false

        Raises:
            TypeError: when given parameter is not a point
        """
        if isinstance(point, Point):
            return self.distance(point) <= Options.PRECISION

        raise TypeError("Given parameter is not a point")

    def point(self, factor):
        """
        Provide point on line by factor (0=start point, 1=end point).

        Args:
            factor(float or int): the factor to control which point (0=start point, 1=end point).

        Raises:
            TypeError: when given parameter is not an int or a float
        """
        if isinstance(factor, (int, float)):
            return self.position + self.direction.scaled(factor)

        raise TypeError("Given parameter is not an int or a float")

    @staticmethod
    def from_points(point_a, point_b):
        """
        Create a linne from two points.

        Args:
            point_a(Point) - start point of line
            point_b(Point) - end point of line

        Returns:
            Line: line with position (point) and direction (vector)

        Raises:
            TypeError: when not all parameters are points
        """
        if isinstance(point_a, Point) and isinstance(point_b, Point):
            return Line(point_a, point_b - point_a)

        raise TypeError("Not all given parameter are points")

    def intersection(self, other):
        """
        Calculate intersection between two lines.

        Args:
            other(Line): another line to find intersection point.

        Returns:
            Point: found intersection point or None if not found.

        Raises:
            TypeError: when given parameter is not a line.

        Note:
            The method does not check whether a found point lies inbetween
            the start point and end point of the line.
        """
        if isinstance(other, Line):
            # p1 + a * v1 = p2 + b * v2         | - p1
            #      a * v1 = (p2 - p1) + b * v2  | x v2
            # a * v1 x v2 = (p2 - p1) x v2
            vector_a = self.direction.cross_product(other.direction)
            vector_b = (other.position - self.position).cross_product(other.direction)

            if abs(vector_a.x) > Options.PRECISION:
                return self.point(vector_b.x / vector_a.x)
            if abs(vector_a.y) > Options.PRECISION:
                return self.point(vector_b.y / vector_a.y)
            if abs(vector_a.z) > Options.PRECISION:
                return self.point(vector_b.z / vector_a.z)

            return None

        raise TypeError("Given parameter is not a line")
