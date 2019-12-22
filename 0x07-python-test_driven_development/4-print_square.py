#!/usr/bin/python3
"""
Documentation for function that prints a square with the character #.

Example:
    $ python3
    >>> print_square = __import__('4-print_square').print_square
    >>> print_square(4)
    ####
    ####
    ####
    ####
"""


def print_square(size):
    """
    Function that prints a square with the character #.

    Args:
        size (integer, float): the size of the square
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
