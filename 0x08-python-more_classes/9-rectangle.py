#!/usr/bin/python3
"""Module with an empty class"""


class Rectangle:
    """This is a class that defines a square
       Class attribute: number_of_instances
                        print_symbol
       Instance attributes: width (int)
                            height (int)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialises instance attribute
            Args: width - Width of rectangle
                  height - Height of rectangle"""
        if isinstance(width, int):
            if (width >= 0):
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if (height >= 0):
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """String representation of object"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height - 1):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        rectangle += str(self.print_symbol) * self.__width
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle to be
            able to recreate a new instance
        """
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """Prints meesage upon instance deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rectangle with bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if(rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new class instance
           Attribute, width == height == size"""
        return cls(size, size)
