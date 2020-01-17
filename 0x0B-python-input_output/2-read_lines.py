#!/usr/bin/python3
"""
Module for the function read_lines(filename="", nb_lines=0) that reads n lines
of a text file (UTF8) and prints it to stdout.
"""


def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file
        nb_lines (int): The number of lines to print
    """
    cnt = 0
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            cnt += 1
            if nb_lines <= 0 or cnt <= nb_lines:
                print(line, end='')
