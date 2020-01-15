#!/usr/bin/python3
"""Module for a class Rectangle that defines a rectangle by: (based on
2-rectangle.py)
"""


class Rectangle:
    """A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Contructor of class Rectangle

        Args:
            width (int): The Rectangle class width
            height (int): The Rectangle class height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Method to recover the rectangle class width

        Returns:
            The private atribute width
        """
        self.__width

    @width.setter
    def width(self, value):
        """Method to set the rectangle class width

        Args:
            value (int): The value for the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to recover the rectangle class height

        Returns:
            The private atribute height
        """
        self.__height

    @height.setter
    def height(self, value):
        """Method to set the rectangle class height

        Args:
            value (int): The value for the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method: def area(self): that returns the rectangle
        area

        Returns:
            area = width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method: def perimeter(self): that returns the
        rectangle perimeter: 

        Returns:
            perimeter = 2 * (width + height)
        """
        if self.__width == 0 or  self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Magic method to return a string representation of the object

        Returns:
            A string that represents the object
        """
        line = ["#" * self.__width] * self.__height
        return "\n".join(line)
