"""Testing of class Point."""
# pylint: disable=no-self-use
from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises, is_not
from engine.threed.vector import Vector
from engine.threed.point import Point


class TestPoint(TestCase):
    """Testing of class Point."""

    def test_default(self):
        """Testing of Default constructor."""
        point = Point()
        assert_that(point.x, equal_to(0.0))
        assert_that(point.y, equal_to(0.0))
        assert_that(point.z, equal_to(0.0))

    def test_sub(self):
        """Testing difference of two points."""
        assert_that(Point(1, 9, 11) - Point(4, 5, 6), equal_to(Vector(-3, 4, 5)))

        message = "You cannot subtract a value of type %s from a point" % type(0)
        assert_that(calling(Point(1, 2, 3).__sub__).with_args(1234),
                    raises(TypeError, message))

    def test_equal(self):
        """Testing two points to be equal."""
        assert_that(Point(1, 2, 3), equal_to(Point(1, 2, 3)))
        assert_that(Point(1, 2, 3), is_not(equal_to(Point(4, 5, 6))))
        assert_that(Point(1, 2, 3), is_not(equal_to(123)))

    def test_from_vector(self):
        """Testing of from_vector static function."""
        point = Point.from_vector(Vector(1, 2, 3))
        assert_that(isinstance(point, Point), equal_to(True))
        assert_that(point.x, equal_to(1.0))
        assert_that(point.y, equal_to(2.0))
        assert_that(point.z, equal_to(3.0))

        message = "You cannot create a point from a value of type %s" % (type(0))
        assert_that(calling(Point.from_vector).with_args(1234),
                    raises(TypeError, message))
