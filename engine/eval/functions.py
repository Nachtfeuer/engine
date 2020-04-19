"""Module functions."""
from __future__ import annotations
import abc
from engine.eval.variable import Variable


class Function(abc.ABC):
    """Base for functions."""

    def __init__(self, variable: Variable):
        """Initialize function instance."""
        self.__variable = variable

    def get(self) -> int:
        """
        Calculate the square.

        Returns:
            int: square of given variable value.
        """
        value = self.__variable.get()
        if isinstance(value, int):
            return self.calculate(value)

        raise TypeError("Variable value should be of type 'int'")

    @abc.abstractmethod
    def calculate(self, value: int) -> int:
        """Calculate the value."""


class Square(Function):
    """Calculate square of given variable value."""

    def __repr__(self) -> str:
        """String representation of the Square function."""
        return "Square(%s)" % super().__repr__()

    def calculate(self, value: int) -> int:
        """Calculate the square of given value."""
        return value ** 2


class SumOfDigits(Function):
    """Calculate sum of digits of variable value."""

    def __repr__(self) -> str:
        """String representation of the Square function."""
        return "SumOfDigits(%s)" % super().__repr__()

    def calculate(self, value: int) -> int:
        """Calculate the sum of the digits of given value."""
        return sum(map(int, str(value)))
