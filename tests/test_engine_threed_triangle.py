"""Testing of class Triangle."""
# pylint: disable=no-self-use
from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises

from engine.threed.point import Point
from engine.threed.triangle import Triangle
from engine.threed.line import Line


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

    def test_has_point_should_succeed(self):
        """Testing of 'has_point' method should succeed."""
        triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
        assert_that(triangle.has_point(Point(0, 0, 0)), equal_to(True))
        assert_that(triangle.has_point(Point(2, 1, 0)), equal_to(True))
        assert_that(triangle.has_point(Point(3, 0, 0)), equal_to(True))
        assert_that(triangle.has_point(Point(3, 3, 0)), equal_to(True))

    def test_has_point_should_fail(self):
        """Testing of 'has_point' method should fail."""
        triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
        assert_that(triangle.has_point(Point(3.001, 0, 0)), equal_to(False))
        assert_that(triangle.has_point(Point(-0.001, 0, 0)), equal_to(False))
        assert_that(triangle.has_point(Point(3.001, 3.001, 0)), equal_to(False))
        assert_that(triangle.has_point(Point(2, 1, 0.001)), equal_to(False))

    def test_intersection_should_succeed(self):
        """Testing of 'intersection' method should succeed."""
        triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
        line = Line.from_points(Point(2, 1, -5), Point(2, 1, +5))
        assert_that(triangle.intersection(line), equal_to(Point(2, 1, 0)))

    def test_intersection_should_fail(self):
        """Testing of 'intersection' method should fail."""
        # line intersects plane of triangle but not in range defined by its vectors
        triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
        line = Line.from_points(Point(5, 1, -5), Point(5, 1, +5))
        assert_that(triangle.intersection(line), equal_to(None))

        # line parallel to triangle and also not on its plane
        triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
        line = Line.from_points(Point(0, 0, -5), Point(3, 0, -5))
        assert_that(triangle.intersection(line), equal_to(None))


def test_triangle_has_point_perf(benchmark):
    """Testing performance of triangle has_point method."""
    triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
    benchmark(triangle.has_point, Point(2, 1, 0))


def test_triangle_intersects_line_perf(benchmark):
    """Testing performance of triangle intersection method."""
    triangle = Triangle(Point(0, 0, 0), Point(3, 0, 0), Point(3, 3, 0))
    line = Line.from_points(Point(2, 1, -5), Point(2, 1, +5))
    benchmark(triangle.intersection, line)
