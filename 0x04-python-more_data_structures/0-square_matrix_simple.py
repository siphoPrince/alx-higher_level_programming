#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Matrix = matrix.copy()

    for loop in range(len(matrix)):
        Matrix[loop] = list(map(lambda x: x**2, matrix[loop]))

    return (Matrix)
