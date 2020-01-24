"""Testing of class Matrix."""
# pylint: disable=no-self-use
import math
from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises, less_than_or_equal_to
from engine.base.matrix import Matrix
from engine.threed.vector import Vector
from engine.tools.options import Options
from engine.tools.conversions import to_radian


class TestMatrix(TestCase):
    """Testing of class Matrix."""

    def test_default(self):
        """Test default constructor."""
        matrix = Matrix()
        assert_that(len(list(matrix.rows())), equal_to(2))
        assert_that(len(list(matrix.columns())), equal_to(2))
        assert_that(list(matrix.rows()), equal_to([[0, 0], [0, 0]]))
        assert_that(list(matrix.columns()), equal_to([[0, 0], [0, 0]]))
        assert_that(matrix.shape(), equal_to((2, 2)))

    def test_setitem(self):
        """Test changing a value in the matrix."""
        matrix = Matrix()
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4
        assert_that(list(matrix.rows()), equal_to([[1, 2], [3, 4]]))
        assert_that(list(matrix.columns()), equal_to([[1, 3], [2, 4]]))

        assert_that(calling(matrix.__setitem__).with_args(1, 5),
                    raises(TypeError, "Index is equired to be a tuple"))
        assert_that(calling(matrix.__setitem__).with_args((1, 2, 3), 5),
                    raises(TypeError, "Index is equired to be a tuple with two ints"))
        assert_that(calling(matrix.__setitem__).with_args((1.0, 2.0), 5),
                    raises(TypeError, "Index is equired to be a tuple with two ints"))
        assert_that(calling(matrix.__setitem__).with_args((1, 1), "hello"),
                    raises(TypeError, "Value is expected to be a float or an int"))

    def test_getitem(self):
        """Test retrieving a value in the matrix."""
        matrix = Matrix.from_sequence([[1, 2], [3, 4]])

        assert_that(matrix[0, 0], equal_to(1))
        assert_that(matrix[0, 1], equal_to(2))
        assert_that(matrix[1, 0], equal_to(3))
        assert_that(matrix[1, 1], equal_to(4))

        assert_that(calling(matrix.__getitem__).with_args(1),
                    raises(TypeError, "Index is equired to be a tuple"))
        assert_that(calling(matrix.__getitem__).with_args((1.0, 2.0)),
                    raises(TypeError, "Index is equired to be a tuple with two ints"))

    def test_from_sequence(self):
        """Testing of from_sequence static function."""
        matrix = Matrix.from_sequence([[1, 2, 3], [4, 5, 6]])
        assert_that(list(matrix.rows()), equal_to([[1, 2, 3], [4, 5, 6]]))

        message = "Not a list or tuple of rows"
        assert_that(calling(Matrix.from_sequence).with_args(1234),
                    raises(TypeError, message))
        message = "Not all rows are lists or tuples"
        assert_that(calling(Matrix.from_sequence).with_args([1, 2, 3, 4]),
                    raises(TypeError, message))
        message = "Either rows, columns or both are 0 entries"
        assert_that(calling(Matrix.from_sequence).with_args([]),
                    raises(ValueError, message))

    def test_mul(self):
        """Testing of __mul__ method."""
        matrix_a = Matrix.from_sequence([[1, 2, 3], [4, 5, 6]])
        matrix_b = Matrix.from_sequence([[7, 8], [9, 10], [11, 12]])
        matrix_c = matrix_a * matrix_b

        assert_that(matrix_c.shape(), equal_to((2, 2)))
        assert_that(list(matrix_c.rows()), equal_to([[58, 64], [139, 154]]))

        message = "You cannot multiply a value of type %s with a matrix" % type(0)
        assert_that(calling(matrix_a.__mul__).with_args(1234),
                    raises(TypeError, message))

    def test_translation(self):
        """Testing translation via matrix multiplication."""
        # representation of the vector or point (ignore fourth value, is always 1)
        matrix_a = Matrix.from_sequence([[1, 1, 1, 1]])
        # representation of the translation matrix
        matrix_b = Matrix.from_sequence(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 2, 3, 1]])

        # translating
        matrix_c = matrix_a * matrix_b
        # result vector or point (ignore fourth value is always 1)
        assert_that(list(matrix_c.columns()), equal_to([[2], [3], [4], [1]]))

    def test_scale(self):
        """Testing scaling via matrix multiplication."""
        # representation of the vector or point (ignore fourth value, is always 1)
        matrix_a = Matrix.from_sequence([[1, 2, 3, 1]])
        # representation of the scale matrix
        matrix_b = Matrix.from_sequence(
            [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 1]])

        # scaling
        matrix_c = matrix_a * matrix_b
        # result vector or point (ignore fourth value is always 1)
        assert_that(list(matrix_c.columns()), equal_to([[2], [4], [6], [1]]))

    def test_rotation_z(self):
        """Testing rotation around z axis via matrix multiplication."""
        # representation of the vector or point (ignore fourth value, is always 1)
        vector = Vector(1, 1, 0).normalized()
        matrix_a = Matrix.from_sequence([[vector.x, vector.y, vector.z]])

        # representation of the rotation matrix along y axis
        angle = to_radian(-90.0)
        matrix_b = Matrix.from_sequence(
            [[math.cos(angle), -math.sin(angle), 0.0],
             [math.sin(angle), math.cos(angle), 0.0],
             [0.0, 0.0, 1.0]])

        # rotating around z axis
        matrix_final = matrix_a * matrix_b

        assert_that(abs(matrix_final[0, 0] - -vector.x), less_than_or_equal_to(Options.PRECISION),
                    "x value was %g instead of %s" % (matrix_final[0, 0], -vector.x))
        assert_that(abs(matrix_final[0, 1] - vector.y), less_than_or_equal_to(Options.PRECISION),
                    "y value was %g instead of %s" % (matrix_final[0, 1], vector.y))
        assert_that(abs(matrix_final[0, 2] - vector.z), less_than_or_equal_to(Options.PRECISION),
                    "z value was %g instead of %s" % (matrix_final[0, 2], vector.z))

    def test_rotation_y(self):
        """Testing rotation around y axis via matrix multiplication."""
        # representation of the vector or point (ignore fourth value, is always 1)
        vector = Vector(1, 1, 0).normalized()
        matrix_a = Matrix.from_sequence([[vector.x, vector.y, vector.z]])

        # representation of the rotation matrix along y axis
        angle = to_radian(90.0)
        matrix_b = Matrix.from_sequence(
            [[math.cos(angle), 0.0, math.sin(angle)],
             [0.0, 1.0, 0.0],
             [-math.sin(angle), 0.0, math.cos(angle)]])

        # rotating around z axis
        matrix_final = matrix_a * matrix_b

        assert_that(abs(matrix_final[0, 0] - vector.z), less_than_or_equal_to(Options.PRECISION),
                    "x value was %g instead of %s" % (matrix_final[0, 0], vector.z))
        assert_that(abs(matrix_final[0, 1] - vector.y), less_than_or_equal_to(Options.PRECISION),
                    "y value was %g instead of %s" % (matrix_final[0, 1], vector.y))
        assert_that(abs(matrix_final[0, 2] - vector.x), less_than_or_equal_to(Options.PRECISION),
                    "z value was %g instead of %s" % (matrix_final[0, 2], vector.x))

    def test_rotation_x(self):
        """Testing rotation around x axis via matrix multiplication."""
        # representation of the vector or point (ignore fourth value, is always 1)
        vector = Vector(1, 1, 0).normalized()
        matrix_a = Matrix.from_sequence([[vector.x, vector.y, vector.z]])

        # representation of the rotation matrix along y axis
        angle = to_radian(-90.0)
        matrix_b = Matrix.from_sequence(
            [[1.0, 0.0, 0.0],
             [0.0, math.cos(angle), -math.sin(angle)],
             [0.0, math.sin(angle), math.cos(angle)]])

        # rotating around z axis
        matrix_final = matrix_a * matrix_b

        assert_that(abs(matrix_final[0, 0] - vector.x), less_than_or_equal_to(Options.PRECISION),
                    "x value was %g instead of %s" % (matrix_final[0, 0], vector.z))
        assert_that(abs(matrix_final[0, 1] - vector.z), less_than_or_equal_to(Options.PRECISION),
                    "y value was %g instead of %s" % (matrix_final[0, 1], vector.z))
        assert_that(abs(matrix_final[0, 2] - vector.y), less_than_or_equal_to(Options.PRECISION),
                    "z value was %g instead of %s" % (matrix_final[0, 2], vector.y))

    def test_repr(self):
        """Test __repr__ method."""
        matrix = Matrix.from_sequence([[1, 2, 3], [4, 5, 6]])
        expected_string = "Matrix([[1, 2, 3], [4, 5, 6]])"
        assert_that(str(matrix), equal_to(expected_string))
