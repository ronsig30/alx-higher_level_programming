#!/usr/bin/python3
"""Module of a square"""


class Square:
    """Defining a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a square.

        Raise:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of a square.

        Return:
            The size to be squared
        """
        return self.__size ** 2
