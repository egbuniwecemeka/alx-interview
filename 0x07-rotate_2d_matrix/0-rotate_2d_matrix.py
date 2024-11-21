#!/usr/bin/python3
"""Rotate a 2D Matrix in a anti-clockwise direction"""




def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90degrees anti-clockwise"""
    n  = len(matrix)

    # Reverse the rows
    for row in matrix:
        row.reverse()
    
    # Transposing rows and colums
    for i in range(n):
        for j in range(n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
