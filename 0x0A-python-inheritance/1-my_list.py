#!/usr/bin/python3
"""Module name: 1-my_list, subclass: MyList"""


class MyList(list):
    """Subclass inheriting from class 'list'
        Method: print_sorted"""

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
