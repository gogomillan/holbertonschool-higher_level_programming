#!/usr/bin/python3
"""
Module for class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor method

        Args:
            width (int): The width for the Rectangle class
            height (int): The height for the Rectangle class
            x (int): The x for the Rectangle class
            y (int): The x for the Rectangle class
            id (int): The id for the Rectangle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Property method

        Returns:
            The __width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method

        Args:
            value (int): The value for __width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Property method

        Returns:
            The __height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method

        Args:
            value (int): The value for __height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Property method

        Returns:
            The __x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method

        Args:
            value (int): The value for __x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Property method

        Returns:
            The __y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method

        Args:
            value (int): The value for __y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        public method that returns the area value of the Rectangle instance.

        Returns:
            Rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        Method that prints in stdout the Rectangle with the character #
        """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        Method so that it returns [Rectangle] (<id>) <x>/<y> -
        <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
