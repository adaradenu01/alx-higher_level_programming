#!/usr/bin/python3
"""Module : 2-is_same_class, Method : is_same_class"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
