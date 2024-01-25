#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Takes 2D matrix and rotate it 90 degrees clockwise

    Args:
        matrix: the 2D matrix to rotate

    Return:
        matrix: the rotated 2D matrix
    """

    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]

    return matrix
