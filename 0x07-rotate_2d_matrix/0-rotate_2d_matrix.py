#!/usr/bin/python3
"""Rotate a 2D Matrix in a anti-clockwise direction"""




def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90degrees anti-clockwise"""

    # there are n/2 squares or cycles in a matrix of side n. Run a loop to traverse the matrix a cycle at a time.
    n = len(matrix)

    # Tranverse the matrix a cycle at a time
    for i in range(n//2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = temp
