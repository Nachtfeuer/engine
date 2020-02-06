"""Mathmatical 3d point."""
from __future__ import annotations

from engine.threed.base.point import AbstractPoint
from engine.threed.base.vector import AbstractVector

from engine.threed.vector import Vector


class Point(AbstractPoint):
    """
    Mathmatically 3d point.

    >>> Point()
    Point(x=0, y=0, z=0)
    """

    def __repr__(self) -> str:
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Point(x=%(x)g, y=%(y)g, z=%(z)g)" % self.__dict__

    def __sub__(self, other: AbstractPoint) -> AbstractVector:
        """
        Args:
            other(AbstractPoint): another point to use for subtraction.

        Returns:
            AbstractVector: difference of two points.
        """
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        raise TypeError("You cannot subtract a value of type %s from a point" % type(other))

    def __add__(self, other: AbstractVector) -> AbstractPoint:
        """
        Get translated point.

        Args:
            other(AbstractVector): a vector to add its coordinates to the point.

        Returns:
            AbstractPoint: translated point
        """
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)

        raise TypeError("You can not add a value of type %s to a point" % type(other))

    def __eq__(self, other: object) -> bool:
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
    def from_vector(vector: AbstractVector) -> AbstractPoint:
        """
        Args:
            vector(AbstractVector): a vector to use to create a point from it.

        Returns:
            AbstractPoint: a point

        Raises:
            TypeError: when given parameter is not a vector
        """
        if isinstance(vector, AbstractVector):
            return Point(vector.x, vector.y, vector.z)

        raise TypeError("You cannot create a point from a value of type %s" % (type(vector)))

    @staticmethod
    def origin() -> Point:
        """
        Returns:
            Point: the Point at origin.
        """
        return Point(0, 0, 0)
