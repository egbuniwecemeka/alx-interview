#!/usr/bin/python3
"""Rotate a 2D Matrix in a anti-clockwise direction"""

# Naive approach - O(n^2) Time and O(n^2) Space
# This includes moving row1/first row to first column in
# reverse order and so on.
# In the matrix above a (3*3) where n=3
# Example matrix[0][0] will become matrix[2][0]
# Example matrix[2][2] should be matrix[0][2]


def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90degrees anti-clockwise"""
    n = len(matrix)

    # Initialize the result matrix with zeros
    res = [[0] * n for _ in range(n)]

    # Flip matrix counterclockwise with nested loops
    for i in range(n):
        for j in range(n):
            res[n-j-1][i] = matrix[i][j]

    # Update the original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]

