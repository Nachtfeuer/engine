"""Testing of class Triangle."""
# pylint: disable=no-self-use
from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises

from engine.threed.point import Point
from engine.threed.triangle import Triangle


class TestTriangle(TestCase):
    """Testing of class Triangle."""

    def test_init_constructor(self):
        """Testing of init constructor."""
        point1, point2, point3 = Point(0, 0, 0), Point(1, 0, 0), Point(0, 1, 0)
        triangle = Triangle(point1, point2, point3)

        assert_that(len(triangle.points()), equal_to(3))
        assert_that(triangle.points()[0], equal_to(point1))
        assert_that(triangle.points()[1], equal_to(point2))
        assert_that(triangle.points()[2], equal_to(point3))

        message = "Not all parameters are of type %s" % type(Point)
        assert_that(calling(Triangle.__init__).with_args(None, 1, 2, 3),
                    raises(TypeError, message))
        assert_that(calling(Triangle.__init__).with_args(None, point1, 2, 3),
                    raises(TypeError, message))
        assert_that(calling(Triangle.__init__).with_args(None, point1, point2, 3),
                    raises(TypeError, message))

    def test_repr(self):
        """Testing of __repr__ method."""
        point1, point2, point3 = Point(0, 0, 0), Point(1, 0, 0), Point(0, 1, 0)
        triangle = Triangle(point1, point2, point3)

        expected_str = "Triangle(%s, %s, %s)" % (point1, point2, point3)
        assert_that(str(triangle), equal_to(expected_str))

#    def test_has_point(self):
#        """Testing of 'has_point' method."""
#        triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
#        assert_that(triangle.has_point(Point(2, 1, 0)), True)
