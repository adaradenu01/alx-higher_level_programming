#!/usr/bin/python3
"""Module with an empty class"""


class Rectangle:
    """This is a class that defines a square
        Attributes: width (int)
                    height (int)"""
    def __init__(self, width=0, height=0):
        """Initialises instance attribute
            Args: width - Width of rectangle
                  height - Height of rectangle"""
        if isinstance(width, int):
            if (width >= 0):
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if (height >= 0):
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Retrieves width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value
