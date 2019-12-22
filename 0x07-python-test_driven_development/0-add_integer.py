#!/usr/bin/python3
"""
Documentation for simple add integer function

Example:
    $ python3
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> print(add_integer(1, 2))
    3
"""


def add_integer(a, b=98):
    """
    Adds two integers together

    Args:
        a (int): first value to add
        b (int, default=98): second value to add

    Returns:
        the sum of a and b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
