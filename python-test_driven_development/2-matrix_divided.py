#!/usr/bin/python3
"""This module defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number."""

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)

    row_size = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
