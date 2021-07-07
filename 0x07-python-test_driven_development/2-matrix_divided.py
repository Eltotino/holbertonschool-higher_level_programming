#!/usr/bin/python3
"""Matrix divide module"""


def matrix_divided(matrix, div):
    """
    Divides all elements of 'matrix' by 'div'
    Args:
        matrix : list of list for integer or float
        div : int or float as div
    Raises:
        TypeError: if list not a list of list of int or float
        TypeError: if each row of the matrix don't have same size
        TypeErroe: if div not a number
        ZeroDivisionError: if div is a 0
    Returns:
        (list[list]): a matrix with same size of the given matrix
    """
    if not isinstance(matrix, list) or \
            not all(type(row) is list for row in matrix) or \
            not all(all(type(e) in (int, float) for e in row)
                    for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        return
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
        return
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return
    return [[round(i/div, 2) for i in row] for row in matrix]
