#!/usr/bin/python3
"""Module of a Square"""


class Square:
    """Defining a Square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero(0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of Square.

        Returns:
            The size to be squared.
        """
        return self.__size ** 2
