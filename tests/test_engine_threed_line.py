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

    def test_has_point(self):
        """Test method 'has_point'."""
        line = Line(Point(0, 0, 0), Vector(10, 0, 0))

        assert_that(line.has_point(Point(-1, 0, 0)), equal_to(True))
        assert_that(line.has_point(Point(0, 0, 0)), equal_to(True))
        assert_that(line.has_point(Point(5, 0, 0)), equal_to(True))
        assert_that(line.has_point(Point(10, 0, 0)), equal_to(True))
        assert_that(line.has_point(Point(11, 0, 0)), equal_to(True))

        assert_that(line.has_point(Point(5, 1, 0)), equal_to(False))
        assert_that(line.has_point(Point(5, -1, 0)), equal_to(False))

        assert_that(calling(line.has_point).with_args(1234),
                    raises(TypeError, "Given parameter is not a point"))

    def test_point(self):
        """Test method 'point'."""
        line = Line(Point(0, 0, 0), Vector(10, 0, 0))

        assert_that(line.point(0), equal_to(Point(0, 0, 0)))
        assert_that(line.point(0.5), equal_to(Point(5, 0, 0)))
        assert_that(line.point(1), equal_to(Point(10, 0, 0)))

        assert_that(calling(line.point).with_args("hello"),
                    raises(TypeError, "Given parameter is not an int or a float"))

    def test_from_points(self):
        """Testing static function 'from_points'."""
        assert_that(Line.from_points(Point(1, 2, 3), Point(4, 5, 6)),
                    equal_to(Line(Point(1, 2, 3), Vector(3, 3, 3))))

        assert_that(calling(Line.from_points).with_args("hello", "hello"),
                    raises(TypeError, "Not all given parameter are points"))

    def test_intersection_succeeds(self):
        """Testing method 'intersection'"""
        # lines on xy plane
        line_a = Line.from_points(Point(0, 0, 0), Point(10, 0, 0))
        line_b = Line.from_points(Point(5, -4, 0), Point(5, +4, 0))
        assert_that(line_a.intersection(line_b), equal_to(Point(5, 0, 0)))

        # lines on yz plane
        line_a = Line.from_points(Point(0, 0, 0), Point(0, 0, 10))
        line_b = Line.from_points(Point(0, -4, 5), Point(0, +4, 5))
        assert_that(line_a.intersection(line_b), equal_to(Point(0, 0, 5)))

        # lines on xz plane
        line_a = Line.from_points(Point(0, 0, 0), Point(0, 0, 10))
        line_b = Line.from_points(Point(-4, 0, 5), Point(+4, 0, 5))
        assert_that(line_a.intersection(line_b), equal_to(Point(0, 0, 5)))

    def test_intersection_fails(self):
        """Testing method 'intersection'"""
        # parallel line does not intersect
        line_a = Line.from_points(Point(0, 0, 0), Point(10, 0, 0))
        line_b = Line.from_points(Point(0, 1, 0), Point(10, 1, 0))
        assert_that(line_a.intersection(line_b), equal_to(None))

        assert_that(calling(Line.intersection).with_args(None, "hello"),
                    raises(TypeError, "Given parameter is not a line"))
