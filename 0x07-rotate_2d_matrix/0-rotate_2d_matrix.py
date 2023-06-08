#!/usr/bin/python3
"""matrix
"""


def transpose_matrix(matrix, n):
    """summary
    Args:
            matrix (_type_): description
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """summary
    Args:
            matrix (_type_): description
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):     
    n = len(matrix)
    transpose_matrix(matrix, n) 
    reverse_matrix(matrix)
    return matrix
