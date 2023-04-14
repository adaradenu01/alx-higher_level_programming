#!/usr/bin/python3
"""Module name : 8-base_geometry, Subclass : Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inherits from 'BaseGeometry'"""
    def __init__(self, width, height):
        """initialises width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__heigth = height
