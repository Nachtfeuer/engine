"""Testing of eval functions."""
# pylint: disable=no-self-use,too-few-public-methods
from unittest import TestCase
from hamcrest import assert_that, equal_to

from engine.eval.variable import Variable


class TestVariable(TestCase):
    """Testing of eval functions."""

    def test_default(self):
        """Testing default use."""
        some_var = Variable(32)
        assert_that(some_var.get(), equal_to(32))
        assert_that(str(some_var), equal_to("Variable(32)"))

    def test_nested_variables(self):
        """Testing nested variables use."""
        some_var = Variable(Variable(32))
        assert_that(some_var.get(), equal_to(32))
        assert_that(str(some_var), equal_to("Variable(Variable(32))"))
