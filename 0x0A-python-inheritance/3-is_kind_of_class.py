#!/usr/bin/python3
"""Module : 3-is_kind_of_class, Method : is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
