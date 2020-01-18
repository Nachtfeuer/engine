"""Testing of class Line."""
# pylint: disable=no-self-use
from unittest import TestCase
from hamcrest import assert_that, equal_to, is_not, calling, raises, less_than_or_equal_to

from engine.threed.vector import Vector
from engine.threed.point import Point
from engine.threed.line import Line
from engine.tools.conversions import to_degree
from engine.tools.options import Options


class TestLine(TestCase):
    """Testing of class Line."""

    def test_init_constructor(self):
        """Testing of init constructor."""
        line = Line(Point(1, 2, 3), Vector(4, 5, 6))
        assert_that(line.position, equal_to(Point(1, 2, 3)))
        assert_that(line.direction, equal_to(Vector(4, 5, 6)))

        message = "One or all types for line parameters are wrong"
        assert_that(calling(Line.__init__).with_args(None, 1, 2),
                    raises(TypeError, message))
        assert_that(calling(Line.__init__).with_args(None, Point(1, 2, 3), 2),
                    raises(TypeError, message))
        assert_that(calling(Line.__init__).with_args(None, 1, Vector(4, 5, 6)),
                    raises(TypeError, message))

    def test_length(self):
        """Testing length of line."""
        line = Line(Point(1, 2, 3), Vector(4, 5, 6))
        assert_that(line.length(), equal_to(Vector(4, 5, 6).length()))

    def test_equal(self):
        """Testing of __eq__ method."""
        line_a = Line(Point(1, 2, 3), Vector(4, 5, 6))
        line_b = Line(Point(1, 2, 3), Vector(4, 5, 6))
        line_c = Line(Point(4, 5, 6), Vector(4, 5, 6))
        line_d = Line(Point(1, 2, 3), Vector(7, 8, 9))

        assert_that(line_a, equal_to(line_b))
        assert_that(line_a, is_not(equal_to(line_c)))
        assert_that(line_a, is_not(equal_to(line_d)))
        assert_that(line_a, is_not(equal_to(1234567890)))

    def test_angle(self):
        """Testing angle method."""
        line_a = Line(Point(1, 2, 3), Vector(2, 4, 6))
        line_b = Line(Point(4, 5, 6), Vector(3, 5, 9))

        expected_angle = to_degree(Vector(2, 4, 6).angle(Vector(3, 5, 9)))
        given_angle = to_degree(line_a.angle(line_b))
        assert_that(abs(given_angle - expected_angle),
                    less_than_or_equal_to(Options.PRECISION), "was %g" % given_angle)

        message = "You cannot calculate an angle between a line and type %s" % type(0)
        assert_that(calling(line_a.angle).with_args(1234),
                    raises(TypeError, message))

    def test_distance(self):
        """Test method 'distance'."""
        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        point = Point(0, 1, 0)
        distance = line.distance(point)
        assert_that(abs(distance - 1.0),
                    less_than_or_equal_to(Options.PRECISION), "but was %g" % distance)

        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        point = Point(0.5, 1, 0)
        distance = line.distance(point)
        assert_that(abs(distance - 1.0),
                    less_than_or_equal_to(Options.PRECISION), "but was %g" % distance)

        message = "You can not calculate distance between a line and type %s" % type(0)
        assert_that(calling(line.distance).with_args(1234),
                    raises(TypeError, message))
