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
        self.size = size
        self.position = position

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
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(i, int) for i in position) or
                not all(i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
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
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """ This method prints in stdout the square with the character #.
        """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            if i != self.__size - 1:
                print()
        return ""
