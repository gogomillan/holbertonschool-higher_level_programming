#!/usr/bin/python3
"""
Module for class Base
"""


class Base:
    """
    Class Base
    """

    """ Private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor method

        Args:
            id (int): The id for the Base class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
