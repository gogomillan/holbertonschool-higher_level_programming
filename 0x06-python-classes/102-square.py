#!/usr/bin/python3
class Square:
    """ This is a class to define a square.
    """
    def __init__(self, size=0):
        """ This is constructor method.

        Args:
            size: size of the square.
        """
        self.size = size

    @property
    def size(self):
        """ This is the getter method.

        Returns:
            __size: size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ This is the setter method.

        Args:
            size: size of the square.
        """
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ This method return the area of the square.

        Returns:
            self.__size * self.__size: The are of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """ Equal comparision method to a Square.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Different comparison method to a Square.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """ Less than comparison method to a Square.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """ Less than or equal comparison method to a Square.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Greater than comparison method to a Square.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Greater than or equal comparison method to a Square.
        """
        return self.area() >= other.area()
