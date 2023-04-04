#!/usr/bin/python3
""" 2-matrix_divided: matrix_divided() """


def matrix_divided(matrix, div):
    """ 
    Function to divide all elements of a square matrix
    arg1: the matrix (matrix)
    arg2: the divisor (div)
    """
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if div is None:
        div = 1
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for element in matrix:
        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for unit in element:
            if type(unit) not in [int]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix)
    a = 0
    while (a < row_len):
        b = 0
        while (b < len(matrix[0])):
            matrix[a][b] = (matrix[a][b]) / div
            b += 1
        a += 1

