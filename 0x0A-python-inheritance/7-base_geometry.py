#!/usr/bin/python3
"""Module name : 7-base_geometry, class : BaseGeometry"""


class BaseGeometry:
    """Class with a public instance method:
       'area()' and 'integer_validator()'"""
    def area(self):
        """Raises exception with message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """checks if value is a positive integer"""
        if not type(value) is int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
