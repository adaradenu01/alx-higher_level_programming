#!/usr/bin/python3
"""Module name: 4-print_square"""


def print_square(size):
    """Prints a square with character '#' 
       argument parameter : size (unit length of square)
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
