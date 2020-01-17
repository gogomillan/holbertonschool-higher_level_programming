#!/usr/bin/python3
"""
Module for the function: pascal_triangle(n)
"""


def pascal_triangle(n):

    """
    function that returns a list of lists of integers representing the Pascals
    triangle of size n

    Args:
        n (int): How many lists

    Returns:
        List of lists with the integer values according to the Pascal Triangle.
    """
    tri = list()
    if n <= 0:
        return tri
    tri.append([1])
    if n == 1:
        return tri
    for i in range(1, n):
        tri.append(list())
        tri[i].append(1)
        for j in range(1, i):
            tri[i].append(tri[i-1][j-1] + tri[i-1][j])
        tri[i].append(1)
    return tri
