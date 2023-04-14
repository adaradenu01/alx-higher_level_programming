#!/usr/bin/python3
"""Module : 4-inherits_from, Method : inherits_from"""


def inherits_from(obj, a_class):
    """Checks if an object is inherited from a specified class"""
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
