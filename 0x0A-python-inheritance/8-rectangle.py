#!/usr/bin/python3
""" Module rectangle"""


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """init files """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
