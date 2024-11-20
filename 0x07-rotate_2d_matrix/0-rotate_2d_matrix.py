#!/bin/usr/env python3
"""Rotate a 2D Matrix in a anti-clockwise direction"""

# Naive approach - O(n^2) Time and O(n^2) Space
# This includes moving row1/first row to first column in reverse order and so on.
# In the matrix above a (3*3) where n=3
# Example matrix[0][0] will become matrix[2][0]
# Example matrix[2][2] should be matrix[0][2]

def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90degrees anti-clockwise"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    print(matrix)

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
             ]
    
    anti_clockwise = rotate_2d_matrix(matrix)
    