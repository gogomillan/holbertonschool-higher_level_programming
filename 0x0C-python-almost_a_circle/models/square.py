#!/usr/bin/python3
"""
Module for the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inheritance from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square.

        Args:
            *args (variable size): New attribute values.
            **kwargs (dict variable size): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the print() and str() representation of a Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
