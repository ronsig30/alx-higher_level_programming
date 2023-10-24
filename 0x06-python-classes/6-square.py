#!/usr/bin/python3
"""Define a class of a square."""


class Square:
    """Representing square."""

    def __init__(self, size=0, position=(0, 0)):
        """A new_square is initialized.
        Args:
            size int: new square size.
            position (int, int): New square position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Current size of the square to be set."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Current position of a square is set"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Current area of a square is returned"""
        return (self.__size * self.__size)

    def my_print(self):
        """The square with the # char to be printed"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
