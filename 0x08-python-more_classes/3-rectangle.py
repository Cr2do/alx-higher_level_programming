#!/usr/bin/python3
"""
A simple module Rectangle
"""


class Rectangle:
    """
        Rectangle classe
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("#", end="")
                print("\n", end="")
        return ""

    def print(Rectangle):
        if Rectangle.height == 0 or Rectangle.width == 0:
            return ""
        else:
            for i in range(Rectangle.height):
                for j in range(Rectangle.width):
                    print("#", end="")
                print("\n", end="")
        return ""