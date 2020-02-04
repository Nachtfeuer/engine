"""Mathmatical 3d plane."""
from __future__ import annotations
from typing import Union, Any, Optional

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

    def __init__(self, position: Point, direction_a: Vector, direction_b: Vector):
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

    def __repr__(self) -> str:
        """
        Returns:
            str: readable representation of the values of this class.
        """
        text = "Plane(position=%(position)s, " % self.__dict__
        text += "direction_a=%(direction_a)s, direction_b=%(direction_b)s)" % self.__dict__
        return text

    def __eq__(self, other: object) -> bool:
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

    def point(self, factor_a: Union[int, float], factor_b: Union[int, float]) -> Point:
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

    def intersection(self, other: Any) -> Optional[Point]:
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

    def has_point(self, point: Point, exact_match: bool = True) -> bool:
        """
        Args:
            point(Point): point to check to be on the plane.
            exact_match(bool): when true (default) both factors have to be in range(0.0..1.0)

        Returns:
            bool: True when point is on the plane.
        """
        if isinstance(point, Point):
            # p1      = p2 + a * v1 + b * v2   | -p2
            # p1 - p2 =      a * v1 + b * v2
            # 1) -b * v2
            #     (p1 - p2) - b * v2 = a * v1      | x v2
            #     (p1 - p2) x v2     = a * v1 x v2
            # 2) -a * v1
            #     (p1 - p2) - a * v1 = b * v2      | x v1
            #     (p1 - p2) x v1     = b * v2 x v1
            vector_a = (point - self.position).cross_product(self.direction_b)
            vector_b = self.direction_a.cross_product(self.direction_b)

            factor_a = Plane.factor_check(vector_a, vector_b)
            if factor_a is not None:
                vector_c = (point - self.position).cross_product(self.direction_a)
                vector_d = self.direction_b.cross_product(self.direction_a)

                factor_b = Plane.factor_check(vector_c, vector_d)
                if factor_b is not None:
                    return not exact_match or \
                        (0.0 <= factor_a <= 1.0 and 0.0 <= factor_b <= 1.0)

            return False
        raise TypeError("Given parameter is not a point")

    @staticmethod
    def factor_check(vector_a: Vector, vector_b: Vector) -> Optional[float]:
        """
        Args:
            vector_a(Vector): first vector
            vector_b(Vector): second vector to use for division

        Returns:
            tuple(float, bool): factor and True when the factor is valid
        """
        factor = None

        if abs(vector_b.x) > Options.PRECISION:
            factor = vector_a.x / vector_b.x
        elif not vector_a.x == vector_b.x:
            return None

        if abs(vector_b.y) > Options.PRECISION:
            factor = vector_a.y / vector_b.y
        elif not vector_a.y == vector_b.y:
            return None

        if abs(vector_b.z) > Options.PRECISION:
            factor = vector_a.z / vector_b.z
        elif not vector_b.z == vector_a.z:
            return None

        return factor
