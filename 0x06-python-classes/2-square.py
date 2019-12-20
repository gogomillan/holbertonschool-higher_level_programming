#!/usr/bin/python3
class Square:
    """ This is a class to define a square.
    """
    def __init__(self, size=0):
        """ This is constructr method.

        Args:
            size: size of the square.
        """
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
