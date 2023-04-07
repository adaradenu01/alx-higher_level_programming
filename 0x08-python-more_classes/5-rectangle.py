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

    def area(self):
        """Returns area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """String representation of object"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height - 1):
            rectangle += '#' * self.__width + "\n"
        rectangle += '#' * self.__width
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle to be
            able to recreate a new instance
        """
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """Prints meesage upon instance deletion"""
        print("Bye rectangle...")
