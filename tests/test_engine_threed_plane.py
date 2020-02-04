"""Testing of class Plane."""
# pylint: disable=no-self-use
from unittest import TestCase
from unittest.mock import patch
from hamcrest import assert_that, equal_to, is_not, calling, raises

from engine.threed.vector import Vector
from engine.threed.point import Point
from engine.threed.line import Line
from engine.threed.plane import Plane


class TestPlane(TestCase):
    """Testing of class Plane."""

    def test_init_constructor(self):
        """Testing of init constructor."""
        plane = Plane(Point(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9))
        assert_that(plane.position, equal_to(Point(1, 2, 3)))
        assert_that(plane.direction_a, equal_to(Vector(4, 5, 6)))
        assert_that(plane.direction_b, equal_to(Vector(7, 8, 9)))

        message = "One or all types for plane parameters are wrong"
        assert_that(calling(Plane.__init__).with_args(None, 1, 2, 3),
                    raises(TypeError, message))
        assert_that(calling(Plane.__init__).with_args(None, Point(1, 2, 3), 2, 3),
                    raises(TypeError, message))
        assert_that(calling(Plane.__init__).with_args(None, Point(1, 2, 3), Vector(4, 5, 6), 3),
                    raises(TypeError, message))

    def test_equal(self):
        """Testing of __eq__ method."""
        line_a = Plane(Point(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9))
        line_b = Plane(Point(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9))
        line_c = Plane(Point(4, 5, 6), Vector(7, 8, 9), Vector(10, 11, 12))

        assert_that(line_a, equal_to(line_b))
        assert_that(line_a, is_not(equal_to(line_c)))
        assert_that(line_a, is_not(equal_to(1234567890)))

    def test_point(self):
        """Testing of 'point' method."""
        plane = Plane(Point(1, 1, 0), Vector(0, 1, 0), Vector(1, 0, 0))
        assert_that(plane.point(0, 0), equal_to(Point(1, 1, 0)))
        assert_that(plane.point(1, 0), equal_to(Point(1, 2, 0)))
        assert_that(plane.point(0, 1), equal_to(Point(2, 1, 0)))
        assert_that(plane.point(1, 1), equal_to(Point(2, 2, 0)))

        message = "Not all parameter are either an int or a float"
        assert_that(calling(Plane.point).with_args(None, 1, "abc"), raises(TypeError, message))
        assert_that(calling(Plane.point).with_args(None, "abc", 1), raises(TypeError, message))

    def test_intersection_succeeds(self):
        """Testing of 'intersection' method."""
        # lines intersects xy plane
        plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 10, 0))
        line = Line(Point(5, 5, -5), Vector(0, 0, 10))
        assert_that(plane.intersection(line), equal_to(Point(5, 5, 0)))

        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(10, 0, 0))
        line = Line(Point(5, 5, -5), Vector(0, 0, 10))
        assert_that(plane.intersection(line), equal_to(Point(5, 5, 0)))

        # lines intersects xz plane
        plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 0, 10))
        line = Line(Point(5, 5, 5), Vector(0, -10, 0))
        assert_that(plane.intersection(line), equal_to(Point(5, 0, 5)))

        plane = Plane(Point(0, 0, 0), Vector(0, 0, 10), Vector(10, 0, 0))
        line = Line(Point(5, 5, 5), Vector(0, -10, 0))
        assert_that(plane.intersection(line), equal_to(Point(5, 0, 5)))

        # lines intersects yz plane
        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(0, 0, 10))
        line = Line(Point(-5, 5, 5), Vector(10, 0, 0))
        assert_that(plane.intersection(line), equal_to(Point(0, 5, 5)))

        plane = Plane(Point(0, 0, 0), Vector(0, 0, 10), Vector(0, 10, 0))
        line = Line(Point(-5, 5, 5), Vector(10, 0, 0))
        assert_that(plane.intersection(line), equal_to(Point(0, 5, 5)))

    def test_intersection_fails(self):
        """Testing method 'intersection'."""
        # parallel line does not intersect
        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(10, 0, 0))
        line = Line(Point(0, 0, 1), Vector(10, 0, 0))
        assert_that(plane.intersection(line), equal_to(None))

        assert_that(calling(Plane.intersection).with_args(None, "hello"),
                    raises(TypeError, "Given parameter is not a line"))

    def test_has_point_succeeds(self):
        """Testing method 'has_point' to succeed."""
        # xy plane
        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(10, 0, 0))
        assert_that(plane.has_point(Point(5, 5, 0)), equal_to(True))
        plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 10, 0))
        assert_that(plane.has_point(Point(5, 5, 0)), equal_to(True))
        # xz plane
        plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 0, 10))
        assert_that(plane.has_point(Point(5, 0, 5)), equal_to(True))
        plane = Plane(Point(0, 0, 0), Vector(0, 0, 10), Vector(10, 0, 0))
        assert_that(plane.has_point(Point(5, 0, 5)), equal_to(True))
        # yz plane
        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(0, 0, 10))
        assert_that(plane.has_point(Point(0, 5, 5)), equal_to(True))
        plane = Plane(Point(0, 0, 0), Vector(0, 0, 10), Vector(0, 10, 0))
        assert_that(plane.has_point(Point(0, 5, 5)), equal_to(True))

    def test_has_point_fails(self):
        """Testing method 'has_point' to fail."""
        # xy plane
        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(10, 0, 0))
        assert_that(plane.has_point(Point(5, 5, 5)), equal_to(False))
        plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 10, 0))
        assert_that(plane.has_point(Point(5, 5, 5)), equal_to(False))
        # xz plane
        plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 0, 10))
        assert_that(plane.has_point(Point(5, 1, 5)), equal_to(False))
        plane = Plane(Point(0, 0, 0), Vector(0, 0, 10), Vector(10, 0, 0))
        assert_that(plane.has_point(Point(5, 1, 5)), equal_to(False))
        # yz plane
        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(0, 0, 10))
        assert_that(plane.has_point(Point(1, 5, 5)), equal_to(False))
        plane = Plane(Point(0, 0, 0), Vector(0, 0, 10), Vector(0, 10, 0))
        assert_that(plane.has_point(Point(1, 5, 5)), equal_to(False))

        plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(0, 0, 10))
        with patch.object(Plane, "factor_check") as mocked_factor_check:
            mocked_factor_check.side_effect = [0.5, None]
            assert_that(plane.has_point(Point(1, 5, 5)), equal_to(False))

        assert_that(calling(plane.has_point).with_args(None, "hello"),
                    raises(TypeError, "Given parameter is not a point"))


def test_plane_intersect_line_perf(benchmark):
    """Testing performance of plane intersection method."""
    plane = Plane(Point(0, 0, 0), Vector(10, 0, 0), Vector(0, 10, 0))
    line = Line(Point(5, 5, -5), Vector(0, 0, 10))
    benchmark(plane.intersection, line)


def test_plane_has_point_perf(benchmark):
    """Testing performance of plane has_point method."""
    plane = Plane(Point(0, 0, 0), Vector(0, 10, 0), Vector(10, 0, 0))
    benchmark(plane.has_point, Point(5, 5, 0))
