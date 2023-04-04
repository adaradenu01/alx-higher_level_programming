#!/usr/bin/python3
"""Module name: 3-say_my_name
   Method: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints text
       args: first_name, last_name
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
