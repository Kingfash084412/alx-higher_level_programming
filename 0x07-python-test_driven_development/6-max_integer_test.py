#!/usr/bin/python3


"""
This is an example of the matrix_divided function.
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    This function divides a matrix by an integer or float and returns a new
    matrix divided by that number
    """

    if (matrix == [] or matrix[0] == []):
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (
                type(matrix[i][j]) is not int and
                type(matrix[i][j]) is not float
            ):
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')

    x = len(matrix[0])

    for i in range(1, len(matrix)):
        if len(matrix[i]) != x:
            raise TypeError('Each row of the matrix must have the same size')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    newmat = matrix[:]

    newmat = [
        [float(round(newmat[i][j]/div, 2)) for j in range(len(newmat[i]))]
        for i in range(len(newmat))]

    return newmat 
