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
    def width(width):
        return self.__width

    @property
    def height(height):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        else:
            raise TypeError("width must be an integer")
            if (value < 0):
                raise TypeError("width must be >= 0")

    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        else:
            raise TypeError("height must be an integer")
            if (value < 0):
                raise TypeError("height must be >= 0")
