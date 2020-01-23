"""Testing of Module conversions."""
# pylint: disable=no-self-use
import math
from unittest import TestCase
from hamcrest import assert_that, less_than_or_equal_to
from engine.tools.conversions import to_degree
from engine.tools.options import Options


class TestConversions(TestCase):
    """Testing of module conversions."""

    def test_to_degree(self):
        """Testing of to_degree function."""
        assert_that(abs(to_degree(math.pi) - 180.0),
                    less_than_or_equal_to(Options.PRECISION), "180 degrees")
        assert_that(abs(to_degree(math.pi / 6.0) - 30.0),
                    less_than_or_equal_to(Options.PRECISION), "30 degrees")
        assert_that(abs(to_degree(1) - 57.295779),
                    less_than_or_equal_to(Options.PRECISION), "about 57 degrees")
