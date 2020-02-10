"""Module triangle."""
from __future__ import annotations
from typing import List, Optional

from engine.threed.base.point import AbstractPoint
from engine.threed.base.line import AbstractLine

from engine.threed.plane import Plane


class Triangle:
    """A Triangle is the smalles plane with three points."""

    def __init__(self, point_a: AbstractPoint, point_b: AbstractPoint, point_c: AbstractPoint):
        """
        Initializing triangle with three points.

        Args:
            point_a(AbstractPoint): first point of triangle.
            point_b(AbstractPoint): second point of triangle.
            point_c(AbstractPoint): third point of triangle.
        """
        if all(isinstance(entry, AbstractPoint) for entry in [point_a, point_b, point_c]):
            self.__point_a = point_a
            self.__point_b = point_b
            self.__point_c = point_c
        else:
            raise TypeError("Not all parameters are of type %s" % type(AbstractPoint))

    def points(self) -> List[AbstractPoint]:
        """
        Returns:
            list<Point>: provides the three points.
        """
        return [self.__point_a, self.__point_b, self.__point_c]

    def __repr__(self) -> str:
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Triangle(%s, %s, %s)" % (self.__point_a, self.__point_b, self.__point_c)

    def has_point(self, point: AbstractPoint) -> bool:
        """
        Check whether given point is inside the triangle.

        Args:
            point(AbstractPoint): point to check.

        Returns:
            bool: True when point is inside the triangle.
        """
        plane = Plane(self.__point_a,
                      self.__point_b - self.__point_a,
                      self.__point_c - self.__point_a)

        factor_a, factor_b = plane.calculate_point_factors(point)
        if factor_a is not None and factor_b is not None:
            return (0.0 <= factor_a <= 1.0 and 0.0 <= factor_b <= 1.0 and
                    (factor_a + factor_b) <= 1.0)

        return False

    def intersection(self, line: AbstractLine) -> Optional[AbstractPoint]:
        """
        Checking intersectionof triangle with a line.

        Args:
            line(Line): the line to find intersection point.

        Returns:
            Point: if intersection point has been found otherwise None.
        """
        plane = Plane(self.__point_a,
                      self.__point_b - self.__point_a,
                      self.__point_c - self.__point_a)

        point = plane.intersection(line)
        if point is not None:
            if self.has_point(point):
                return point
        return None
