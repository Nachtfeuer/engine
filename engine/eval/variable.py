"""Module variable."""
from __future__ import annotations
from typing import Union


class Variable:
    """Variable keeping a concrete value or variable reference."""

    def __init__(self, value: Union[int, Variable]):
        """
        Initialize the variable with a value or variable reference.
        """
        self.__value = value

    def __repr__(self) -> str:
        """String representation of the variable."""
        return "Variable(%s)" % self.__value

    def get(self, lazy: bool = False) -> Union[int, Variable]:
        """
        Usually retrieving the value.

        Args:
            lazy(bool): when true then just provide the value or the variable
                        reference (do not call get on the reference)
        Returns:
            Union[int, Variable]: value or variable (depends)
        """
        if isinstance(self.__value, Variable) and not lazy:
            return self.__value.get()
        return self.__value
