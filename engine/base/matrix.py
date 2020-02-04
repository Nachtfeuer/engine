"""Module matrix."""
from __future__ import annotations
from typing import Tuple, List, Generator, Any


class Matrix:
    """Managing operations for a matrix."""
    def __init__(self, initial_rows: int = 2, initial_cols: int = 2):
        """Initialize a matrix with given number of rows and columns."""
        self.__data = []
        self.__shape = (initial_rows, initial_cols)

        for _ in range(initial_rows):
            row = []
            for _ in range(initial_cols):
                row.append(0.0)
            self.__data.append(row)

    def __repr__(self) -> str:
        """
        Returns:
            str: internal representation of the matrix data.
        """
        return "Matrix(%s)" % self.__data

    def shape(self) -> Tuple[int, int]:
        """
        Dimension of the matrix

        Returns:
            tuple: with two ints representing number of rows and columns of the matrix
        """
        return self.__shape

    def rows(self) -> Generator[Any, Any, Any]:
        """
        Returns:
            generator(yield): Provide a copy of the rows.
        """
        for row in self.__data:
            yield row[:]

    def columns(self) -> Generator[Any, Any, Any]:
        """
        Returns:
            generator(yield): Provide a copy of the columns.
        """
        for idx in range(len(self.__data[0])):
            yield [row[idx] for row in self.__data]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        """
        Args:
            index (tuple): it contains first the row then the column as tuple
            value(float): value is a float
        """
        if not isinstance(index, tuple):
            raise TypeError("Index is equired to be a tuple")
        if not len(index) == 2 or not all(isinstance(entry, int) for entry in index):
            raise TypeError("Index is equired to be a tuple with two ints")
        if not isinstance(value, (float, int)):
            raise TypeError("Value is expected to be a float or an int")

        row, column = index
        self.__data[row][column] = value

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        """
        Args:
            index (tuple): it contains first the row then the column as tuple

        Returns
            float or int: value at given index
        """
        if not isinstance(index, tuple):
            raise TypeError("Index is equired to be a tuple")
        if not len(index) == 2 or not all(isinstance(entry, int) for entry in index):
            raise TypeError("Index is equired to be a tuple with two ints")

        row, column = index
        return self.__data[row][column]

    @staticmethod
    def from_sequence(sequence: List[Any]) -> Matrix:
        """
        Args:
            sequence: the matrix (list of lists, list of tuples, tuple of tuples, ...)

        Returns:
            Matrix: the matrix representation
        """
        if not isinstance(sequence, (list, tuple)):
            raise TypeError("Not a list or tuple of rows")
        if not all(isinstance(entry, (list, tuple)) for entry in sequence):
            raise TypeError("Not all rows are lists or tuples")
        if len(sequence) == 0 or len(sequence[0]) == 0:
            raise ValueError("Either rows, columns or both are 0 entries")

        matrix = Matrix(len(sequence), len(sequence[0]))
        for row_idx, row in enumerate(sequence):
            for col_idx, value in enumerate(row):
                matrix[row_idx, col_idx] = value

        return matrix

    def __mul__(self, other: Matrix) -> Matrix:
        """
        Multiplication between two matrices.

        Args:
            other(Matrix): another matrix instance.

        Returns:
            Matrix: result of multiplication of two matrices
        """
        if isinstance(other, Matrix):
            matrix = Matrix(self.shape()[0], other.shape()[1])
            for column_idx, column in enumerate(other.columns()):
                for row_idx, row in enumerate(self.rows()):
                    matrix[row_idx, column_idx] = \
                        sum(row_val * col_val for row_val, col_val in zip(row, column))
            return matrix

        raise TypeError("You cannot multiply a value of type %s with a matrix" % type(other))
