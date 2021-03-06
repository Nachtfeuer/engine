"""Testing of eval functions."""
# pylint: disable=no-self-use,too-few-public-methods
from __future__ import annotations
from typing import Union

from unittest import TestCase
from hamcrest import assert_that, equal_to, calling, raises

from engine.eval.variable import Variable
from engine.eval.functions import Square, SumOfDigits, SquareRoot, Increment, Decrement


class BadVariable(Variable):
    """Variable used the wrong way."""
    def __init__(self):
        """Initializing"""
        super(BadVariable, self).__init__(None)

    def get(self, lazy: bool = False) -> Union[int, Variable]:
        """As it shouldn't be"""
        return self


class TestFunctions(TestCase):
    """Testing of eval functions."""

    def test_square(self):
        """Testing square function."""
        fun = Square(Variable(32))
        assert_that(fun.get(), equal_to(1024))
        assert_that(str(fun), "Square(Variable(32))")

        # testing bad usage (just once because of abstract function)
        fun = Square(BadVariable())
        message = "Variable value should be of type 'int'"
        assert_that(calling(fun.get), raises(TypeError, message))

    def test_sum_of_digits(self):
        """Testing sum of digits function."""
        fun = SumOfDigits(Variable(123456789))
        assert_that(fun.get(), equal_to(45))
        assert_that(str(fun), "SumOfDigits(Variable(123456789))")
        # handling of negative numbers
        fun = SumOfDigits(Variable(-123456789))
        assert_that(fun.get(), equal_to(45))

    def test_integer_square_root(self):
        """Testing integer square root function."""
        fun = SquareRoot(Variable(1025))
        assert_that(fun.get(), equal_to(32))
        assert_that(str(fun), "SquareRoot(Variable(1025))")

    def test_increment(self):
        """Testing increment function."""
        fun = Increment(Variable(10))
        assert_that(fun.get(), equal_to(11))
        assert_that(str(fun), "Increment(Variable(10))")

    def test_decrement(self):
        """Testing decrement function."""
        fun = Decrement(Variable(10))
        assert_that(fun.get(), equal_to(9))
        assert_that(str(fun), "Decrement(Variable(10))")
