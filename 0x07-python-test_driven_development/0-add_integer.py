#!/usr/bin/python3
"""This Module carrys a function that adds 2 integers"""


def add_integer(a, b=98):
    """ A func to add two numbers
        args: only type 'int' or 'float'
        Return: sum of the two numbers
    """
    if type(a) in [float]:
        a = int(a)
    if type(b) in [float]:
        b = int(b)
    if type(a) not in [int]:
        raise TypeError("a must be an integer")
    if type(b) not in [int]:
        raise TypeError("b must be an integer")
    return a+b
