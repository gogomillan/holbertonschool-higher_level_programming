#!/usr/bin/python3
class Square:
    """ This is a class to define a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ This is constructor method.

        Args:
            size: size of the square.
            position: postion for the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ This is the getter method.

        Returns:
            __position: position of the square.
        """
        return self.__position

    @position.setter
    def position(self, position):
        """ This is the setter method.

        Args:
            size: size of the square.
        """
        if not type(position) is tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not type(position[0]) is int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not type(position[1]) is int:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        """ This method return the area of the square.

        Returns:
            self.__size * self.__size: The are of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """ This method prints in stdout the square with the character #.
        """
        for i in range(self.__size):
            if self.__position[1] == 0:
                print(" " * self.__position[0], end='')
            print("#" * self.__size)
        if self.__size == 0:
            print()
