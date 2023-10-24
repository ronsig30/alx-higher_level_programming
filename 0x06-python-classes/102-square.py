#!/usr/bin/python3
"""Module of a square"""


class Square:
    """defining a square"""

    def __init__(self, size=0):
        """constructor.
        Args:
            size: side length of a square.
        """
        self.size = size

    @property
    def size(self):
        """property of the length of a square.
        Raises:
            TypeError: if size is not integer
            ValueError: If size is less than zero.
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
        """area of the square.
        Returns:
            size aquared.
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
