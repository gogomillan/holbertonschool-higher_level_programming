#!/usr/bin/python3
"""
Documentation for function that prints a text with 2 new lines after each of
these characters: ., ? and :

Example:
    $ python3
    >>> print_square = __import__('4-print_square').print_square
    >>> print_square(4)
    ####
    ####
    ####
    ####
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): the text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    space = False
    for c in text:
        if c == '.' or c == '?' or c == ':':
            print(c + '\n')
            space = False
        elif c == ' ' and space is False:
            space = False
        else:
            print(c, end="")
            space = True
