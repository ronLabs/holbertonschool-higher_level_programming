#!/usr/bin/python3
"""
Return a new matrix Divided by div value
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(col, int) or isinstance(col, float))
                    for col in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    j = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return j
