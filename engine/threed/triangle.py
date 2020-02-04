"""Module triangle."""
from __future__ import annotations
from typing import List

from engine.threed.point import Point
from engine.threed.plane import Plane


class Triangle:
    """
    A Triangle is the smalles plane with three points.

    >>> Triangle(Point(1, 2, 3), Point(4, 5, 6),Point(7, 8, 9))
    Triangle(Point(x=1, y=2, z=3), Point(x=4, y=5, z=6), Point(x=7, y=8, z=9))
    """

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        """
        Initializing triangle with three points.

        Args:
            point_a(Point): first point of triangle.
            point_b(Point): second point of triangle.
            point_c(Point): third point of triangle.
        """
        if all(isinstance(entry, Point) for entry in [point_a, point_b, point_c]):
            self.__point_a = point_a
            self.__point_b = point_b
            self.__point_c = point_c
        else:
            raise TypeError("Not all parameters are of type %s" % type(Point))

    def points(self) -> List[Point]:
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

    def has_point(self, point: Point) -> bool:
        """
        Check whether given point is inside the triangle.

        Args:
            point(Point): point to check.

        Returns:
            bool: True when point is inside the triangle.
        """
        plane = Plane(self.__point_a,
                      self.__point_b - self.__point_a,
                      self.__point_c - self.__point_a)

        factor_a, factor_b = plane.calculate_point_factors(point)
        if factor_a is not None and factor_b is not None:
            print(factor_a, factor_b)
            return (0.0 <= factor_a <= 1.0 and 0.0 <= factor_b <= 1.0 and
                    (factor_a + factor_b) <= 1.0)

        return False
