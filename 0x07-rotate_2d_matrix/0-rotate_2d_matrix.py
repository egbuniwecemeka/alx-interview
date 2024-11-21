#!/usr/bin/python3
"""Rotate a 2D Matrix in a anti-clockwise direction"""


def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90degrees anti-clockwise"""

    matrix.reverse()

    n  = len(matrix)
    
    # Transposing rows and colums
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
