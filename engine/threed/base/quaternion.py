"""Module quaternion for abstract base class."""
from __future__ import annotations
from typing import Union
import abc


class AbstractQuaternion(abc.ABC):
    """Abstract base class for quaternion."""

    def __init__(self,
                 w: Union[int, float] = 0.0,
                 x: Union[int, float] = 0.0,
                 y: Union[int, float] = 0.0,
                 z: Union[int, float] = 0.0):
        """
        Args:
            w (int or float): rotation angle (default: 0.0)
            x (int or float): 3d x coordinates of roation axis (default: 0.0)
            y (int or float): 3d y coordinates of roation axis (default: 0.0)
            z (int or float): 3d z coordinates of roation axis (default: 0.0)
        """
        self.w = float(w)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @abc.abstractmethod
    def norm(self) -> float:
        """
        Returns:
            float: norm of quaternion
        """

    @abc.abstractmethod
    def length(self) -> float:
        """
        Returns:
            float: length (magnitude) of quaternion
        """

    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Args:
            other(AbstractQuaternion): another quaternion to use for comparison.

        Returns:
            bool: True when both quatenrions are equal otherwise false
        """

    @abc.abstractmethod
    def __add__(self, other: AbstractQuaternion) -> AbstractQuaternion:
        """
        Args:
            other(AbstractQuaternion): another quaternion to use for summation.

        Returns:
            AbstractQuaternion: sum of two quaternion.
        """

    @abc.abstractmethod
    def __sub__(self, other: AbstractQuaternion) -> AbstractQuaternion:
        """
        Args:
            other(AbstractQuaternion): another quaternion to use for subtraction.

        Returns:
            AbstractQuaternion: difference of two quaternion.
        """

    @abc.abstractmethod
    def conjugate(self) -> AbstractQuaternion:
        """
        Returns:
            AbstractVector: conjugae current quaternion.
        """

    @abc.abstractmethod
    def scaled(self, factor: Union[int, float]) -> AbstractQuaternion:
        """
        Provide quaternion scaled by given factor.

        Args:
            factor(int or float): factor to multiply each field with.

        Returns:
            AbstractQuaternion: each field multiplicated by given factor.
        """

    @abc.abstractmethod
    def inverse(self) -> AbstractQuaternion:
        """
        Provide inverse quaternion.

        Returns:
            AbstractQuaternion: inverse quaternion.
        """

    @abc.abstractmethod
    def __mul__(self, other: AbstractQuaternion) -> AbstractQuaternion:
        """
        Args:
            other(Quaternion): another quaternion

        Returns:
            Quaternion: as a product of two quaternion (also known as Hamilton product).
        """
