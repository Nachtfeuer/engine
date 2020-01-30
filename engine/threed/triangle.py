"""Module triangle."""
from engine.threed.point import Point


class Triangle:
    """
    A Triangle is the smalles plane with three points.

    >>> Triangle(Point(1, 2, 3), Point(4, 5, 6),Point(7, 8, 9))
    Triangle(Point(x=1, y=2, z=3), Point(x=4, y=5, z=6), Point(x=7, y=8, z=9))
    """

    def __init__(self, point_a, point_b, point_c):
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

    def points(self):
        """
        Returns:
            list<Point>: provides the three points.
        """
        return [self.__point_a, self.__point_b, self.__point_c]

    def __repr__(self):
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Triangle(%s, %s, %s)" % (self.__point_a, self.__point_b, self.__point_c)
