"""Testing of class Vector."""
# pylint: disable=no-self-use
from unittest import TestCase
from hamcrest import assert_that, equal_to, less_than_or_equal_to, calling, raises, is_not

from engine.threed.vector import Vector
from engine.tools.conversions import to_degree
from engine.tools.options import Options


class TestVector(TestCase):
    """Testing of class Vector."""

    def test_default(self):
        """Testing of Default constructor."""
        vector = Vector()
        assert_that(vector.x, equal_to(0.0))
        assert_that(vector.y, equal_to(0.0))
        assert_that(vector.z, equal_to(0.0))

    def test_length(self):
        """Testing calculation of length vector."""
        vector = Vector(2, 3, 6)
        assert_that(abs(vector.length() - 7.0), less_than_or_equal_to(Options.PRECISION))

    def test_equal(self):
        """Testing two vectors to be equal."""
        assert_that(Vector(1, 2, 3), equal_to(Vector(1, 2, 3)))
        assert_that(Vector(1, 2, 3), is_not(equal_to(Vector(4, 5, 6))))
        assert_that(Vector(1, 2, 3), is_not(equal_to(123)))

    def test_sum(self):
        """Testing sum of two vectors."""
        assert_that(Vector(1, 2, 3) + Vector(4, 5, 6), equal_to(Vector(5, 7, 9)))

        message = "You cannot add a value of type %s to a vector" % type(0)
        assert_that(calling(Vector(1, 2, 3).__add__).with_args(1234),
                    raises(TypeError, message))

    def test_sub(self):
        """Testing difference of two vectors."""
        assert_that(Vector(1, 9, 11) - Vector(4, 5, 6), equal_to(Vector(-3, 4, 5)))

        message = "You cannot subtract a value of type %s from a vector" % type(0)
        assert_that(calling(Vector(1, 2, 3).__sub__).with_args(1234),
                    raises(TypeError, message))

    def test_negation(self):
        """Testing of method __neg__."""
        assert_that(-Vector(1, 2, 3), equal_to(Vector(-1, -2, -3)))

    def test_dot_product(self):
        """Testing dot product of two vectors."""
        assert_that(Vector(1, 2, 3).dot_product(Vector(4, 5, 6)), equal_to(32))

        message = "You cannot calculate a dot product between a vector and type %s" % type(0)
        assert_that(calling(Vector(1, 2, 3).dot_product).with_args(1234),
                    raises(TypeError, message))

    def test_cross_product(self):
        """Testing cross product of two vectors."""
        assert_that(Vector(2, 3, 4).cross_product(Vector(5, 6, 7)), equal_to(Vector(-3, 6, -3)))

        message = "You cannot calculate a cross product between a vector and type %s" % type(0)
        assert_that(calling(Vector(1, 2, 3).cross_product).with_args(1234),
                    raises(TypeError, message))

    def test_angle(self):
        """Testing angle between two vectors."""
        angle = to_degree(Vector(9, 2, 7).angle(Vector(4, 8, 10)))
        assert_that(abs(angle - 38.2), less_than_or_equal_to(1e-1))

        message = "Vector length cannot be 0 for calculating angle"
        assert_that(calling(Vector(0, 0, 0).angle).with_args(Vector(1, 2, 3)),
                    raises(ValueError, message))
        assert_that(calling(Vector(1, 2, 3).angle).with_args(Vector(0, 0, 0)),
                    raises(ValueError, message))

        message = "You cannot calculate an angle between a vector and type %s" % type(0)
        assert_that(calling(Vector(1, 2, 3).angle).with_args(1234),
                    raises(TypeError, message))

    def test_from_sequence(self):
        """Testing from_sequence static function."""
        assert_that(Vector.from_sequence([1, 2, 3]), equal_to(Vector(1, 2, 3)))

        message = r"Sequence \[1, 2\] cannot be converted into a vector"
        assert_that(calling(Vector.from_sequence).with_args([1, 2]),
                    raises(TypeError, message))
        message = r"could not convert string to float: 'hello'"
        assert_that(calling(Vector.from_sequence).with_args([1, 2, "hello"]),
                    raises(ValueError, message))

    def test_to_list(self):
        """Testing to_list method."""
        assert_that(Vector(1, 2.5, 3).to_list(), equal_to([1, 2.5, 3]))

    def test_to_tuple(self):
        """Testing to_tuple method."""
        assert_that(Vector(1, 2.5, 3).to_tuple(), equal_to((1, 2.5, 3)))

    def test_normalized(self):
        """Testing normalized method."""
        assert_that(Vector(2, 2, 2).normalized().length(), equal_to(1.0))

    def test_scaled(self):
        """Testing scaled method."""
        assert_that(Vector(1, 2, 3).scaled(2.0), equal_to(Vector(2.0, 4.0, 6.0)))

    def test_mul(self):
        """Testing multiplication."""
        assert_that(Vector(1, 2, 3) * 2.0, equal_to(Vector(2.0, 4.0, 6.0)))

        message = "You cannot multiply a value of type %s with a vector" % type("hello")
        assert_that(calling(Vector(1, 2, 3).__mul__).with_args("hello"),
                    raises(TypeError, message))

    def test_projection(self):
        """Test method 'projection'."""
        assert_that(Vector(1, 1, 0).projection(Vector(2, 0, 0)),
                    equal_to(Vector(1, 0, 0)))

        message = "You can not calculate a projection of a vector on a type %s" % type("hello")
        assert_that(calling(Vector(1, 2, 3).projection).with_args("hello"),
                    raises(TypeError, message))
