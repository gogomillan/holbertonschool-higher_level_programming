#!/usr/bin/python3
"""
Documentation for function that divides all elements of a matrix.

Example:
    $ python3
    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided
    >>> matrix = [ [1, 2, 3], [4, 5, 6] ]
    >>> print(matrix_divided(matrix, 3))
    >>> print(matrix)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    [[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix (list): the square matrix
        div (int or float): the number that divide

    Returns:
        new matrix
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    if type(matrix) == tuple or type(matrix) == set:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    l = len(matrix[0])
    for row in matrix:
        if type(row) == tuple or type(row) == set:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != l:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    new = list(map(lambda row: list(map(lambda col: round(col / div, 2),
                                        row)), matrix))
    return new
