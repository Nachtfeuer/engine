"""Mathmatical 3d line."""
from engine.threed.point import Point
from engine.threed.vector import Vector


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
