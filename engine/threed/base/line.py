"""Modul line for abstract base class."""
from __future__ import annotations
from typing import Optional
import abc

from engine.threed.base.point import AbstractPoint
from engine.threed.base.vector import AbstractVector


class AbstractLine(abc.ABC):
    """Abstract base class for line."""

    def __init__(self, position: AbstractPoint, direction: AbstractVector):
        """
        Initialize line with position and direction.

        Args:
            position(AbstractPoint): start of line
            direction(AbstractVector): direction of line.

        Raises:
            TypeError: when position is not a point or direction is not a vector
        """
        if isinstance(position, AbstractPoint) and isinstance(direction, AbstractVector):
            self.position = position
            self.direction = direction
        else:
            raise TypeError("One or all types for line parameters are wrong")

    @abc.abstractmethod
    def length(self) -> float:
        """
        Returns:
            float: length of line
        """

    @abc.abstractmethod
    def angle(self, other: AbstractLine) -> float:
        """
        Args:
            other(Line): another line to use for calculation of angle.

        Returns:
            float: angle between two lines.

        Raises:
            TypeError: when given parameter is not a line.
        """

    @abc.abstractmethod
    def distance(self, obj: AbstractPoint) -> float:
        """
        Args:
            object(Point): distance to a point.

        Returns:
            float: distance to the point

        Raises:
            TypeError: when given parameter is not a point.
        """

    @abc.abstractmethod
    def has_point(self, point: AbstractPoint) -> bool:
        """
        Verifies that point is on the line.

        Args:
            point(Point): point to verify

        Returns:
            bool: True when point is on the line otherwise false

        Raises:
            TypeError: when given parameter is not a point
        """

    @abc.abstractmethod
    def point(self, factor: float) -> AbstractPoint:
        """
        Provide point on line by factor (0=start point, 1=end point).

        Args:
            factor(float or int): the factor to control which point (0=start point, 1=end point).

        Raises:
            TypeError: when given parameter is not an int or a float
        """

    @abc.abstractmethod
    def intersection(self, other: AbstractLine) -> Optional[AbstractPoint]:
        """
        Calculate intersection between two lines.

        Args:
            other(AbstractLine): another line to find intersection point.

        Returns:
            Point: found intersection point or None if not found.

        Raises:
            TypeError: when given parameter is not a line.

        Note:
            The method does not check whether a found point lies inbetween
            the start point and end point of the line.
        """
