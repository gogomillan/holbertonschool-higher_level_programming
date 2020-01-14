#!/usr/bin/python3
"""Module for multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies  2 matrices by using the module NumPy:

    Args:
        m_a (list int or float): Matrix a
        m_b (list int or float): Matrix b
    """
    import numpy as np

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a is None or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if m_b is None or len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    length = len(m_a[0])
    for row in m_a:
        if row is None or len(row) == 0:
            raise ValueError("m_a can't be empty")
        if len(row) != length:
            raise TypeError("each row of m_a must be of the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_a should contain only integers or floats")
    length = len(m_b[0])
    for row in m_b:
        if row is None or len(row) == 0:
            raise ValueError("m_b can't be empty")
        if len(row) != length:
            raise TypeError("each row of m_b must be of the same size")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    a_a = np.array(m_a)
    a_b = np.array(m_b)
    a_c = np.matmul(a_a, a_b)

    return a_c
