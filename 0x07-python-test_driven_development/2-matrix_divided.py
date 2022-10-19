#!/usr/bin/python3
"""
Function(s):
    matrix_divided: Divides the contents of a matrix by div.
"""


def matrix_divided(matrix, div):
    """
    Recieves two values, checks if div is a number, and matrix only contains
    number, then casts them as ints. Then all the the elements of the matrix
    are divide by div, and a new matrix containing the result, rounded to
    two decimal places, is returned.
    Args:
        matrix: Matrix of values.
        div: Number to divide each item in matrix by.
    Returns:
        list: New matrix, each element divided by zero.
    Raises:
        TypeError: In the event of either variable
            not being or containing an int or float.
        ZeroDivisionError: In the event of an attempted division by zero.
    Notes:
        Instead of round, I came up with this math: int(t/div*100)/100)
    """
    matrixError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matrixError)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    length = len(matrix[0])
    for i in matrix:
        hold = []
        if not isinstance(i, list):
            raise TypeError(matrixError)
        if length != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for t in i:
            if not isinstance(t, int) and not isinstance(t, float):
                raise TypeError(matrixError)
            hold.append(round(t/div, 2))
        new_matrix.append(hold)
    return new_matrix

