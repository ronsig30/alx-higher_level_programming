#!/usr/bin/python3
"""Module of a Square"""


class Square:
    """Defining a square."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: length of a square.
        """
        self.size = size

    @property
    def size(size):
        """Property for the length of a square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero(0).
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

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Outputs the square."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if is self.size - 1 and i != j else "")
        print()
