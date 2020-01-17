#!/usr/bin/python3
"""
Module for the function number_of_lines(filename="") that returns the number of
lines of a text file.
"""


def number_of_lines(filename=""):
    """
    Function that returns the number of lines of a text file

    Args:
        filename (str): The name of the file

    Returns:
        The number of lines of the file
    """
    cnt = 0
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            cnt += 1
    return cnt
