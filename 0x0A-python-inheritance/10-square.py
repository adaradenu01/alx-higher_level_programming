#!/usr/bin/python3
"""
    9-rectangle: subclass Rectangle from BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Subclass of Subclass 'Rectangle'
        Attributes: Width and Height(Private instance attributes)
        Method: area() and integer_validator()
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size**2)

    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle", self.__size, self.__size))
