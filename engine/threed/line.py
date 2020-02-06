"""Mathmatical 3d line."""
from __future__ import annotations
from typing import Optional

from engine.threed.base.point import AbstractPoint
from engine.threed.base.line import AbstractLine
from engine.tools.options import Options


class Line(AbstractLine):
    """Mathmatical 3d line."""

    def length(self) -> float:
        """
        Returns:
            float: length of line
        """
        return self.direction.length()

    def __repr__(self) -> str:
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Line(position=%(position)s, direction=%(direction)s)" % self.__dict__

    def __eq__(self, other: object) -> bool:
        """
        Args:
            other(Line): another line to use for comparison.

        Returns:
            bool: True when both lines are equal otherwise false
        """
        if isinstance(other, AbstractLine):
            return self.position == other.position and self.direction == other.direction

        return False

    def angle(self, other: AbstractLine) -> float:
        """
        Args:
            other(Line): another line to use for calculation of angle.

        Returns:
            float: angle between two lines.

        Raises:
            TypeError: when given parameter is not a line.
        """
        if isinstance(other, AbstractLine):
            return self.direction.angle(other.direction)

        raise TypeError("You cannot calculate an angle " +
                        "between a line and type %s" % type(other))

    def distance(self, obj: AbstractPoint) -> float:
        """
        Args:
            object(Point): distance to a point.

        Returns:
            float: distance to the point

        Raises:
            TypeError: when given parameter is not a point.
        """
        if isinstance(obj, AbstractPoint):
            point = obj
            vector_a = point - self.position
            vector_b = vector_a.projection(self.direction)
            return (vector_a - vector_b).length()

        raise TypeError("You can not calculate distance " +
                        "between a line and type %s" % type(obj))

    def has_point(self, point: AbstractPoint) -> bool:
        """
        Verifies that point is on the line.

        Args:
            point(Point): point to verify

        Returns:
            bool: True when point is on the line otherwise false

        Raises:
            TypeError: when given parameter is not a point
        """
        if isinstance(point, AbstractPoint):
            return self.distance(point) <= Options.PRECISION

        raise TypeError("Given parameter is not a point")

    def point(self, factor: float) -> AbstractPoint:
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
    def from_points(point_a: AbstractPoint, point_b: AbstractPoint) -> Line:
        """
        Create a line from two points.

        Args:
            point_a(AbstractPoint) - start point of line
            point_b(AbstractPoint) - end point of line

        Returns:
            Line: line with position (point) and direction (vector)

        Raises:
            TypeError: when not all parameters are points
        """
        if isinstance(point_a, AbstractPoint) and isinstance(point_b, AbstractPoint):
            return Line(point_a, point_b - point_a)

        raise TypeError("Not all given parameter are points")

    def intersection(self, other: AbstractLine) -> Optional[AbstractPoint]:
        """
        Calculate intersection between two lines.

        Args:
            other(AbstractLine): another line to find intersection point.

        Returns:
            Point: found intersection point or None if not found.

        Raises:
            TypeError: when given parameter is not a line.

        Note:
            The method does not check whether a found point lies inbetween
            the start point and end point of the line.
        """
        if isinstance(other, AbstractLine):
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
