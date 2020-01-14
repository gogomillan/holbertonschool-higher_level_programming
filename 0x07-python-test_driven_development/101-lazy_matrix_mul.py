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

    return np.matmul(m_a, m_b)
