"""Mathmatical 3d vector."""
from __future__ import annotations
import math
from typing import List, Tuple, Union, Any
from engine.tools.options import Options
from engine.threed.base.vector import AbstractVector


class Vector(AbstractVector):
    """
    Mathmatically 3d vector

    >>> Vector()
    Vector(x=0, y=0, z=0)
    >>> abs(Vector(2, 3, 6).length() - 7.0) < 1e-6
    True
    """

    def length(self) -> float:
        """
        Returns:
            float: length of vector
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self) -> str:
        """
        Returns:
            str: readable representation of the values of this class.
        """
        return "Vector(x=%(x)g, y=%(y)g, z=%(z)g)" % self.__dict__

    def __eq__(self, other: object) -> bool:
        """
        Args:
            other(Vector): another vector to use for comparison.

        Returns:
            bool: True when both vectors are equal otherwise false
        """
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z

        return False

    def __add__(self, other: AbstractVector) -> AbstractVector:
        """
        Args:
            other(AbstractVector): another vector to use for summation.

        Returns:
            AbstractVector: sum of two vectors.
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        raise TypeError("You cannot add a value of type %s to a vector" % type(other))

    def __neg__(self) -> AbstractVector:
        """
        Returns:
            Vector: negation of current vector.
        """
        return Vector(-self.x, -self.y, -self.z)

    def __sub__(self, other: AbstractVector) -> AbstractVector:
        """
        Args:
            other(AbstractVector): another vector to use for subtraction.

        Returns:
            AbstractVector: difference of two vectors.
        """
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        raise TypeError("You cannot subtract a value of type %s from a vector" % type(other))

    def __mul__(self, other: Union[int, float]) -> AbstractVector:
        """
        Multiply a vector by a factor.

        Args:
            other(int or float): a factor

        Returns:
            AbstractVector: multiplicated by a factor.
        """
        if isinstance(other, (int, float)):
            return self.scaled(other)

        raise TypeError("You cannot multiply a value of type %s with a vector" % type(other))

    def __getitem__(self, index: int) -> float:
        """
        Args:
            index(int): 0 = x, 1 = y, 2 = z

        Returns:
            float: coordinate at given index.
        """
        if isinstance(index, int):
            if 0 <= index < 3:
                return [self.x, self.y, self.z][index]
            raise ValueError("Index out of range (0, 1 or 2 expected)")
        raise TypeError("Index is not an int")

    def dot_product(self, other: AbstractVector) -> float:
        """
        Args:
            other(Vector): another vector to use for calculation of dot product.

        Returns:
            float: dot product of two vectors.
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

        raise TypeError("You cannot calculate a dot product " +
                        "between a vector and type %s" % type(other))

    def is_perpendicular(self, other: AbstractVector) -> bool:
        """
        Checking two vectors to be perpendicular to each other.

        Args:
            other(AbstractVector): another Vector to check this property with

        Returns:
            bool: when both vectors are perpendicular to each other.
        """
        return abs(self.dot_product(other)) < Options.PRECISION

    def cross_product(self, other: AbstractVector) -> AbstractVector:
        """
        Args:
            other(AbstractVector): another vector to use for calculation of cross product.

        Returns:
            AbstractVector: dot product of two vectors.
        """
        if isinstance(other, AbstractVector):
            return Vector(self.y * other.z - self.z * other.y,
                          self.z * other.x - self.x * other.z,
                          self.x * other.y - self.y * other.x)

        raise TypeError("You cannot calculate a cross product " +
                        "between a vector and type %s" % type(other))

    def angle(self, other: AbstractVector) -> float:
        """
        Args:
            other(AbstractVector): another vector to use for calculation of angle.

        Returns:
            float: angle between two vectors.
        """
        if isinstance(other, Vector):
            len1 = self.length()
            if len1 == 0.0:
                raise ValueError("Vector length cannot be 0 for calculating angle")

            len2 = other.length()
            if len2 == 0.0:
                raise ValueError("Vector length cannot be 0 for calculating angle")

            return math.acos(self.dot_product(other) / (len1 * len2))

        raise TypeError("You cannot calculate an angle " +
                        "between a vector and type %s" % type(other))

    def to_list(self) -> List[float]:
        """
        Returns:
            list: a list with three floats representing x, y and z (in that order).
        """
        return [self.x, self.y, self.z]

    def to_tuple(self) -> Tuple[float, float, float]:
        """
        Returns:
            tuple: a tuple with three floats representing x, y and z (in that order).
        """
        return (self.x, self.y, self.z)

    @staticmethod
    def from_sequence(sequence: Any) -> Vector:
        """
        Args:
            sequence (list or tuple): a sequence of ints or floats representing x, y and z.

        Returns:
            Vector: with x, y and z taken from sequence.

        Raises:
            TypeError: if given parameter doesn't match requirements.
        """
        if isinstance(sequence, (list, tuple)) and len(sequence) == 3:
            x, y, z = sequence
            return Vector(x, y, z)

        raise TypeError("Sequence %s cannot be converted into a vector" % str(sequence))

    def normalized(self) -> AbstractVector:
        """
        Provided normalized vector (lenght is then 1.0).

        Returns:
            AbstractVector: normalized
        """
        return self.scaled(1.0 / self.length())

    def scaled(self, factor: Union[int, float]) -> AbstractVector:
        """
        Provide vector scaled by given factor.

        Args:
            factor(int or float): factor to multiply each coordinate with.

        Returns:
            AbstractVector: each coordinated multiplicated by given factor.
        """
        return Vector(self.x * factor, self.y * factor, self.z * factor)

    def projection(self, other: AbstractVector) -> AbstractVector:
        """
        Calculate projection "vector on vector".

        Args:
            other(Vector): the vector to do projection on

        Returns:
            Vector: Calculated projection.
        """
        if isinstance(other, Vector):
            return other.scaled(self.dot_product(other) / other.dot_product(other))

        raise TypeError("You can not calculate a projection " +
                        "of a vector on a type %s" % type(other))
