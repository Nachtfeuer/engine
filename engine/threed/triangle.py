"""Module triangle."""
from engine.threed.vector import Vector
from engine.threed.point import Point


class Triangle:
    """
    A Triangle is the smalles plane with three points
    (internally stored as vertices).
    """

    def __init__(self, vector_a, vector_b, vector_c):
        """
        Initializing triangle with three vertices.

        Args:
            vector_a(Vector): first vector of triangle.
            vector_b(Vector): second vector of triangle.
            vector_c(Vector): third vector of triangle.
        """
        if all(isinstance(entry, Vector) for entry in [vector_a, vector_b, vector_c]):
            if Triangle.is_valid(vector_a, vector_b, vector_c):
                self.__vector_a = vector_a
                self.__vector_b = vector_b
                self.__vector_c = vector_c
            else:
                raise ValueError("Given vectors do not represent a closed triangle")
        else:
            raise TypeError("Not all parameters are of type %s" % type(Vector))

    def vectors(self):
        """
        Returns:
            list<Vector>: provides the three vectors.
        """
        return [self.__vector_a, self.__vector_b, self.__vector_c]

    def __repr__(self):
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Triangle(%s, %s, %s)" % (self.__vector_a, self.__vector_b, self.__vector_c)

    @staticmethod
    def is_valid(vector_a, vector_b, vector_c):
        """
        Verifying that given vertices represent a closed triangle.

        Args:
            vector_a(Vector): first vector of triangle.
            vector_b(Vector): second vector of triangle.
            vector_c(Vector): third vector of triangle.

        Returns:
            bool: True when given vertices are representing a valid triangle.
        """
        return Point() == Point.from_vector(vector_a + vector_b + vector_c)

    @staticmethod
    def from_points(point_a, point_b, point_c):
        """
        Create a triangle from three points.

        Args:
            point_a(Point): first point of triangle.
            point_b(Point): second point of triangle.
            point_c(Point): third point of triangle.

        Returns:
            Triangle: a triangle created from points.

        Raises:
            ValueError: when not all vectors have a lenght > 0
            TypeError: when not all parameters are points
        """
        if all(isinstance(point, Point) for point in [point_a, point_b, point_c]):
            vector_a = point_b - point_a
            vector_b = point_c - point_b
            vector_c = point_a - point_c

            if all(vector.length() > 0.0 for vector in [vector_a, vector_b, vector_c]):
                return Triangle(vector_a, vector_b, vector_c)

            raise ValueError("Not all vectors have a length > 0.0")
        raise TypeError("Not all parameters are points")
