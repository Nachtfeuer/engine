"""Modul vector for abstract base class."""
from __future__ import annotations
from typing import Union, List, Tuple
import abc


class AbstractVector(abc.ABC):
    """Abstract base class for vector."""

    def __init__(self,
                 x: Union[int, float] = 0.0,
                 y: Union[int, float] = 0.0,
                 z: Union[int, float] = 0.0):
        """
        Args:
            x (float): 3d x coordinates (default: 0.0)
            y (float): 3d y coordinates (default: 0.0)
            z (float): 3d z coordinates (default: 0.0)
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @abc.abstractmethod
    def length(self) -> float:
        """
        Returns:
            float: length of vector
        """

    @abc.abstractmethod
    def dot_product(self, other: AbstractVector) -> float:
        """
        Args:
            other(AbstractVector): another vector to use for calculation of dot product.

        Returns:
            float: dot product of two vectors.
        """

    @abc.abstractmethod
    def is_perpendicular(self, other: AbstractVector) -> bool:
        """
        Checking two vectors to be perpendicular to each other.

        Args:
            other(AbstractVector): another Vector to check this property with

        Returns:
            bool: when both vectors are perpendicular to each other.
        """

    @abc.abstractmethod
    def cross_product(self, other: AbstractVector) -> AbstractVector:
        """
        Args:
            other(AbstractVector): another vector to use for calculation of cross product.

        Returns:
            AbstractVector: dot product of two vectors.
        """

    @abc.abstractmethod
    def angle(self, other: AbstractVector) -> float:
        """
        Args:
            other(AbstractVector): another vector to use for calculation of angle.

        Returns:
            float: angle between two vectors.
        """

    @abc.abstractmethod
    def to_list(self) -> List[float]:
        """
        Returns:
            list: a list with three floats representing x, y and z (in that order).
        """

    @abc.abstractmethod
    def to_tuple(self) -> Tuple[float, float, float]:
        """
        Returns:
            tuple: a tuple with three floats representing x, y and z (in that order).
        """

    @abc.abstractmethod
    def normalized(self) -> AbstractVector:
        """
        Provided normalized vector (lenght is then 1.0).

        Returns:
            AbstractVector: normalized
        """

    @abc.abstractmethod
    def scaled(self, factor: Union[int, float]) -> AbstractVector:
        """
        Provide vector scaled by given factor.

        Args:
            factor(int or float): factor to multiply each coordinate with.

        Returns:
            AbstractVector: each coordinated multiplicated by given factor.
        """

    @abc.abstractmethod
    def projection(self, other: AbstractVector) -> AbstractVector:
        """
        Calculate projection "vector on vector".

        Args:
            other(Vector): the vector to do projection on

        Returns:
            Vector: Calculated projection.
        """

    @abc.abstractmethod
    def __add__(self, other: AbstractVector) -> AbstractVector:
        """
        Args:
            other(AbstractVector): another vector to use for summation.

        Returns:
            AbstractVector: sum of two vectors.
        """

    @abc.abstractmethod
    def __sub__(self, other: AbstractVector) -> AbstractVector:
        """
        Args:
            other(AbstractVector): another vector to use for subtraction.

        Returns:
            AbstractVector: difference of two vectors.
        """
