"""Module quaternion for mathmatical quaternion."""
from __future__ import annotations
from typing import Union
import math
from engine.threed.base.quaternion import AbstractQuaternion
from engine.threed.base.vector import AbstractVector


class Quaternion(AbstractQuaternion):
    """Mathmatical quaternion."""

    def __repr__(self) -> str:
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Quaternion(w=%(w)g, x=%(x)g, y=%(y)g, z=%(z)g)" % self.__dict__

    def norm(self) -> float:
        """
        Returns:
            float: norm of quaternion
        """
        return self.w**2 + self.x**2 + self.y**2 + self.z**2

    def length(self) -> float:
        """
        Returns:
            float: length (magnitude) of quaternion
        """
        return math.sqrt(self.norm())

    def __eq__(self, other: object) -> bool:
        """
        Args:
            other(AbstractQuaternion): another quaternion to use for comparison.

        Returns:
            bool: True when both quatenrions are equal otherwise false
        """
        if isinstance(other, AbstractQuaternion):
            return self.w == other.w and \
                   self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __add__(self, other: AbstractQuaternion) -> AbstractQuaternion:
        """
        Args:
            other(AbstractQuaternion): another quaternion to use for summation.

        Returns:
            AbstractQuaternion: sum of two quaternion.
        """
        if isinstance(other, AbstractQuaternion):
            return Quaternion(self.w + other.w,
                              self.x + other.x, self.y + other.y, self.z + other.z)

        raise TypeError("Given parameter is not a quaternion")

    def __sub__(self, other: AbstractQuaternion) -> AbstractQuaternion:
        """
        Args:
            other(AbstractQuaternion): another quaternion to use for subtraction.

        Returns:
            AbstractQuaternion: difference of two quaternion.
        """
        if isinstance(other, AbstractQuaternion):
            return Quaternion(self.w - other.w,
                              self.x - other.x, self.y - other.y, self.z - other.z)

        raise TypeError("Given parameter is not a quaternion")

    def conjugate(self) -> AbstractQuaternion:
        """
        Returns:
            Vector: conjugate of current vector.
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def scaled(self, factor: Union[int, float]) -> AbstractQuaternion:
        """
        Provide quaternion scaled by given factor.

        Args:
            factor(int or float): factor to multiply each field with.

        Returns:
            AbstractQuaternion: each field multiplicated by given factor.
        """
        return Quaternion(self.w * factor, self.x * factor, self.y * factor, self.z * factor)

    def inverse(self) -> AbstractQuaternion:
        """
        Provide inverse quaternion.

        Returns:
            AbstractQuaternion: inverse quaternion.
        """
        return self.conjugate().scaled(1.0 / self.norm())

    def __mul__(self, other: AbstractQuaternion) -> AbstractQuaternion:
        """
        Args:
            other(Quaternion): another quaternion

        Returns:
            Quaternion: as a product of two quaternion (also known as Hamilton product).
        """
        if isinstance(other, Quaternion):
            return Quaternion(
                self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z,
                self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y,
                self.w * other.y + self.y * other.w + self.z * other.x - self.x * other.z,
                self.w * other.z + self.z * other.w + self.x * other.y - self.y * other.x
            )

        raise TypeError("Given parameter is not a quaternion")

    @staticmethod
    def from_vector(vector: AbstractVector) -> AbstractQuaternion:
        """
        Convert a vector into quaternion.

        Args:
            vector(AbstractVector): vector to convert into a quaternion.

        Returns:
            AbstractQuaternion: converted vector.
        """
        return Quaternion(0, vector.x, vector.y, vector.z)
