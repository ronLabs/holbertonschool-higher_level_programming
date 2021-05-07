#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix.copy()
    for i in range(len(matrix_cpy)):
        matrix_cpy[i] = list(map(lambda a: a ** 2, matrix_cpy[i]))
    return (matrix_cpy)
