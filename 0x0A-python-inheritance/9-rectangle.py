#!/usr/bin/python3
"""Module name : 9-base_geometry, Subclass : Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inherits from 'BaseGeometry'"""
    def __init__(self, width, height):
        """initialises width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns string representation of object"""
        return ("[{}] {}/{}".format(type(self).__name__, self.__width,
                self.__height))
