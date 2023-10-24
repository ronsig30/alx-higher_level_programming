#!/usr/bin/python3
"""MagicClass matching exactly with bytecode provided"""

import math


class MagicClass:
    """To represent a circle"""

    def __init__(self, radius=0):
        """MagicClass is initialized.
        Arg:
            radius (int or float): radius of new magicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area of MagicClass is returned."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference of Magicclass is returned."""
        return (2 * math.pi * self.__radius)
