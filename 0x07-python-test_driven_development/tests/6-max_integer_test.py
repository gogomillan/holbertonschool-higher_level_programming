==============================
How to use 100-matrix_mul.py
==============================

The function multiplies 2 matrices:

    >>> matrix_mul = __import__("100-matrix_mul").matrix_mul
    >>> print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    [[7, 10], [15, 22]]

Documentation
=============

    >>> module_doc = __import__("100-matrix_mul").__doc__
    >>> print(len(module_doc) > 0)
    True

    >>> func_doc = __import__("100-matrix_mul").matrix_mul.__doc__
    >>> print(len(func_doc) > 0)
    True

Basic multiplication
==============

If the factors are right
::
    >>> print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    [[7, 10], [15, 22]]

    >>> print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
    [[13, 16]]

    >>> matrix_divided(matrix, float('inf'))
    [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

Negative numbers
::
    >>> matrix_divided(matrix, -1)
    [[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0]]

Mixed Integers and Floats
::
    >>> matrix = [[1, 2.2, 3], [4, 5.5, 6]]

    >>> matrix_divided(matrix, 3)
    [[0.33, 0.73, 1.0], [1.33, 1.83, 2.0]]

Error Handling
==============

Exceptions control

    >>> matrix = [[1, 2, 3], [4, 5, 6]]

Dividing by zero
::
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

Divisor is not an integer or float
::
    >>> matrix_divided(matrix, "Hello")
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

    >>> matrix_divided(matrix, (1, 2, 3))
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

Some rows is not the same size
::
    >>> matrix = [[1, 2, 3], [4, 5]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

    >>> matrix = [[1], [4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

Matrix is not a list of lists of integers or floats
::
    >>> matrix = [[1, 2, "Hello"], [4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[1, 2, 3], ["Holberton", 5, 6]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[1, 2, (1, 2, 3)], [4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[1, 2, [1, 2, 3]], ["Holbies", 5, 6]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = ((1, 2, 3), (4, 5, 6))

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [(1, 2, 3), [4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = []

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = None

    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Missing Arguments
::
    >>> matrix_divided(matrix)
    Traceback (most recent call last):
    ...
    TypeError: matrix_divided() missing 1 required positional argument: 'div'

    >>> matrix_divided()
    Traceback (most recent call last):
    ...
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
