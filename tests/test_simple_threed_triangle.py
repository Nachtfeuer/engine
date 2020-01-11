"""Testing of class Triangle."""
# pylint: disable=no-self-use
from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises

from engine.threed.vector import Vector
from engine.threed.point import Point
from engine.threed.triangle import Triangle


class TestTriangle(TestCase):
    """Testing of class Triangle."""

    def test_init_constructor(self):
        """Testing of init constructor."""
        point1, point2, point3 = Point(0, 0, 0), Point(1, 0, 0), Point(0, 1, 0)
        vector1, vector2, vector3 = point2-point1, point3-point2, point1-point3
        triangle = Triangle(vector1, vector2, vector3)

        assert_that(len(triangle.vectors()), equal_to(3))
        assert_that(triangle.vectors()[0], equal_to(vector1))
        assert_that(triangle.vectors()[1], equal_to(vector2))
        assert_that(triangle.vectors()[2], equal_to(vector3))

        message = "Not all parameters are of type %s" % type(Vector)
        assert_that(calling(Triangle.__init__).with_args(None, 1, 2, 3),
                    raises(TypeError, message))
        assert_that(calling(Triangle.__init__).with_args(None, vector1, 2, 3),
                    raises(TypeError, message))
        assert_that(calling(Triangle.__init__).with_args(None, vector1, vector2, 3),
                    raises(TypeError, message))

        message = "Given vectors do not represent a closed triangle"
        assert_that(calling(Triangle.__init__).with_args(
            None, Vector(1, 1, 1), Vector(1, 1, 1), Vector(1, 1, 1)),
                    raises(ValueError, message))

    def test_repr(self):
        """Testing of __repr__ method."""
        point1, point2, point3 = Point(0, 0, 0), Point(1, 0, 0), Point(0, 1, 0)
        vector1, vector2, vector3 = point2-point1, point3-point2, point1-point3
        triangle = Triangle(vector1, vector2, vector3)

        expected_str = "Triangle(%s, %s, %s)" % (vector1, vector2, vector3)
        assert_that(str(triangle), equal_to(expected_str))

    def test_is_valid(self):
        """Testing of is_valid static function."""
        point1, point2, point3 = Point(0, 0, 0), Point(1, 0, 0), Point(0, 1, 0)
        vector1, vector2, vector3 = point2-point1, point3-point2, point1-point3
        assert_that(Triangle.is_valid(vector1, vector2, vector3), equal_to(True))
