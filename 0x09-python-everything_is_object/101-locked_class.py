#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from creating new attributes in the Locked      Class except for the declared attributes called 'first_name
    '"""

    __slots__ = ["first_name"]
