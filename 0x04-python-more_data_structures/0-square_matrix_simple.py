#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    word function that computes 
    the square of a matrix
    """

    newm = []

    for j in matrix:
        result = list(map(lambda x: x**2, j))
        newm.append(result)
    return newm
