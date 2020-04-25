"""Module functions."""
from __future__ import annotations
import math
import abc
from engine.eval.variable import Variable


class Function(abc.ABC):
    """Base for functions."""

    def __init__(self, variable: Variable):
        """Initialize function instance."""
        self.__variable = variable

    def __repr__(self) -> str:
        """We do not mention the function itself."""
        return str(self.__variable)

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

    def __call__(self) -> int:
        """Execution calculation (same as get)."""
        return self.get()

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
        return sum(map(int, str(abs(value))))


class SquareRoot(Function):
    """Calculate integer square root of variable value."""

    def __repr__(self) -> str:
        """String representation of the Square function."""
        return "Square(%s)" % super().__repr__()

    def calculate(self, value: int) -> int:
        """Calculate the integer square root of given value."""
        return int(math.sqrt(value))


class Increment(Function):
    """Calculate +1 of variable value."""

    def __repr__(self) -> str:
        """String representation of the increment function."""
        return "Increment(%s)" % super().__repr__()

    def calculate(self, value: int) -> int:
        """Calculate the increment of given value."""
        return value + 1


class Decrement(Function):
    """Calculate -1 of variable value."""

    def __repr__(self) -> str:
        """String representation of the decrement function."""
        return "Decrement(%s)" % super().__repr__()

    def calculate(self, value: int) -> int:
        """Calculate the decrement of given value."""
        return value - 1
