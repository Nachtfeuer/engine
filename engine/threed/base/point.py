"""Modul point for abstract base class."""
# pylint: disable=cyclic-import
from __future__ import annotations
from typing import Union
import abc

from engine.threed.base.vector import AbstractVector


class AbstractPoint(abc.ABC):
    """Abstract base class for point."""

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
    def __add__(self, other: AbstractVector) -> AbstractPoint:
        """
        Get translated point.

        Args:
            other(AbstractVector): a vector to add its coordinates to the point.

        Returns:
            AbstractPoint: translated point
        """

    @abc.abstractmethod
    def __sub__(self, other: AbstractPoint) -> AbstractVector:
        """
        Args:
            other(Point): another point to use for subtraction.

        Returns:
            Vector: difference of two points.
        """
