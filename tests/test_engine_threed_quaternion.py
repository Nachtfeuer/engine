"""Testing of class Quaternion."""
# pylint: disable=no-self-use
import math
from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises, is_not

from engine.threed.quaternion import Quaternion
from engine.threed.vector import Vector
from engine.tools.conversions import to_radian


class QuaternionTest(TestCase):
    """Testing of class Quaternion."""

    def test_repr(self):
        """Testing of method __repr__."""
        quaternion = Quaternion(2, 4, 5, 6)
        assert_that(str(quaternion), equal_to("Quaternion(w=2, x=4, y=5, z=6)"))

    def test_length(self):
        """Testing method 'length'."""
        quaternion = Quaternion(2, 4, 5, 6)
        assert_that(quaternion.length(), equal_to(9.0))

    def test_equal(self):
        """Testing of method __eq__."""
        quaternion1 = Quaternion(1, 2, 3, 4)
        quaternion2 = Quaternion(1, 2, 3, 4)
        quaternion3 = Quaternion(5, 6, 7, 8)

        assert_that(quaternion1, equal_to(quaternion2))
        assert_that(quaternion1, is_not(equal_to(quaternion3)))
        assert_that(quaternion1, is_not(equal_to(1234)))

    def test_add(self):
        """Testing of method __add__."""
        assert_that(Quaternion(1, 2, 3, 4) + Quaternion(5, 6, 7, 8),
                    equal_to(Quaternion(6, 8, 10, 12)))

        assert_that(calling(Quaternion(0, 0, 0, 0).__add__).with_args("hello"),
                    raises(TypeError, "Given parameter is not a quaternion"))

    def test_sub(self):
        """Testing of method __sub__."""
        assert_that(Quaternion(4, 3, 2, 1) - Quaternion(5, 6, 7, 8),
                    equal_to(Quaternion(-1, -3, -5, -7)))

        assert_that(calling(Quaternion(0, 0, 0, 0).__sub__).with_args("hello"),
                    raises(TypeError, "Given parameter is not a quaternion"))

    def test_conjugate(self):
        """Testing of method 'conjugate'."""
        assert_that(Quaternion(1, 2, 3, 4).conjugate(), equal_to(Quaternion(1, -2, -3, -4)))

    def test_scaled(self):
        """Testing of method 'scaled'."""
        assert_that(Quaternion(1, 2, 3, 4).scaled(2), equal_to(Quaternion(2, 4, 6, 8)))

    def test_inverse(self):
        """Testing of method 'inverse'."""
        assert_that(Quaternion(1, 0, 1, 0).inverse(), equal_to(Quaternion(0.5, 0, -0.5, 0)))

    def test_mult(self):
        """Testing of method '__mul__'."""
        quaternion1 = Quaternion(1.0, 0.0, 1.0, 0.0)
        quaternion2 = Quaternion(1.0, 0.5, 0.5, 0.75)
        assert_that(quaternion1 * quaternion2, equal_to(Quaternion(0.5, 1.25, 1.5, 0.25)))

        assert_that(calling(Quaternion(0, 0, 0, 0).__mul__).with_args("hello"),
                    raises(TypeError, "Given parameter is not a quaternion"))

    def test_rotate_x(self):
        """Testing rotation around x axis."""
        w = to_radian(90)
        quaternion = Quaternion(math.cos(w/2.0), math.sin(w/2.0), 0, 0)
        vector = Vector(0.0, 2.0, 0.0)
        vector_rotated = quaternion * Quaternion.from_vector(vector) * quaternion.inverse()
        assert_that(vector_rotated, equal_to(Quaternion(0, 0, 0, 2.0)))

    def test_rotate_y(self):
        """Testing rotation around y axis."""
        w = to_radian(-90)
        quaternion = Quaternion(math.cos(w/2.0), 0, math.sin(w/2.0), 0)
        vector = Vector(2.0, 0.0, 0.0)
        vector_rotated = quaternion * Quaternion.from_vector(vector) * quaternion.inverse()
        assert_that(vector_rotated, equal_to(Quaternion(0, 0, 0, 2.0)))

    def test_rotate_z(self):
        """Testing rotation around z axis."""
        w = to_radian(90)
        quaternion = Quaternion(math.cos(w/2.0), 0, 0, math.sin(w/2.0))
        vector = Vector(0.0, 2.0, 0.0)
        vector_rotated = quaternion * Quaternion.from_vector(vector) * quaternion.inverse()
        assert_that(vector_rotated, equal_to(Quaternion(0, -2, 0, 0)))


def test_quaternion_mul_perf(benchmark):
    """Testing performance of Quaternion.__mul__ method."""
    benchmark(Quaternion(1.0, 0.0, 1.0, 0.0).__mul__, Quaternion(1.0, 0.5, 0.5, 0.75))
