"""Module plane for base class."""
import abc
from typing import Any, Optional, Union, Tuple
from engine.threed.base.point import AbstractPoint
from engine.threed.base.vector import AbstractVector


class AbstractPlane(abc.ABC):
    """Abstract base class for plane."""

    def __init__(self,
                 position: AbstractPoint,
                 direction_a: AbstractVector,
                 direction_b: AbstractVector):
        """
        Initialize plane with position and two directions.

        Args:
            position(AbstractPoint): start of plane
            direction_a(AbstractVector): first direction of plane.
            direction_b(AbstractVector): second direction of plane.

        Raises:
            TypeError: when position is not a point or directions are not a vector
        """
        if isinstance(position, AbstractPoint) and \
            isinstance(direction_a, AbstractVector) and \
                isinstance(direction_b, AbstractVector):
            self.position = position
            self.direction_a = direction_a
            self.direction_b = direction_b
        else:
            raise TypeError("One or all types for plane parameters are wrong")

    @abc.abstractmethod
    def normal(self) -> AbstractVector:
        """
        Returns:
            AbstractVector: plane normal.
        """

    @abc.abstractmethod
    def intersection(self, other: Any) -> Optional[AbstractPoint]:
        """
        Calculate intersection between given plane and a line.

        Args:
            other(Line): line to find intersection point.

        Returns:
            Point: found intersection point or None if not found.

        Raises:
            TypeError: when given parameter is not a line.

        Note:
            The method does not check whether a found point lies inbetween
            the start point and end point of the line or inside the limits
            defined for the plane.
        """

    @abc.abstractmethod
    def point(self, factor_a: Union[int, float], factor_b: Union[int, float]) -> AbstractPoint:
        """
        Provide point on plane by two factors (0=start point, 1=end point).

        Args:
            factor_a(float or int): the factor to control which point (0=start point, 1=end point).
            factor_b(float or int): the factor to control which point (0=start point, 1=end point).

        Raises:
            TypeError: when given parameter is not an int or a float
        """

    @abc.abstractmethod
    def has_point(self, point: AbstractPoint, exact_match: bool = True) -> bool:
        """
        Args:
            point(AbstractPoint): point to check to be on the plane.
            exact_match(bool): when true (default) both factors have to be in range(0.0..1.0)

        Returns:
            bool: True when point is on the plane.

        Raises:
            TypeError: if given Parameter is not a point
        """

    @abc.abstractmethod
    def calculate_point_factors(
            self, point: AbstractPoint) -> Tuple[Optional[float], Optional[float]]:
        """
        Args:
            point(Point): point to check to be on the plane.
            exact_match(bool): when true (default) both factors have to be in range(0.0..1.0)

        Returns:
            Tuple[float, float]: tuple of two float factors or None's
                                 if no intersection is possible.

        Raises:
            TypeError: if given Parameter is not a point
        """

    @abc.abstractmethod
    def projection_point(self, point: AbstractPoint) -> AbstractPoint:
        """
        Projection of point on given plane.

        Args:
            plane(AbstractPlane): plane to use for point -> plane projection.

        Returns:
            AbstractPoint: projection point onto given plane.
        """
