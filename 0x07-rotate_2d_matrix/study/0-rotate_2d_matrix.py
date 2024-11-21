#!/usr/bin/env python3

# Method 1:Naive approach - O(n^2) Time and O(n^2) Space
# This includes moving row1/first row to first column in
# reverse order and so on.
# In the matrix above a (3*3) where n=3
# Example matrix[0][0] will become matrix[2][0]
# Example matrix[2][2] should be matrix[0][2]

def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix"""
    n = len(matrix)

    # Initialize the result to zeros
    res = [[0] * n for _ in range(n)]

    # Flip the matrix in counterclockwise direction
    for i in range(n):
        for j in range(n):
            res[n-j-1][i] = matrix[i][j]

    # Copy into original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]


# Method 2: Expected approach - O(n^2) Time and O(1) Space
# To solve the question without any extra space, rotate the array in form of cycles. For example, a 4 X 4 matrix will have 2 cycles. The first cycle is formed by its 1st row, last column, last row, and 1st column. The second cycle is formed by the 2nd row, second-last column, second-last row, and 2nd column. The idea is for each square cycle, to swap the elements involved with the corresponding cell in the matrix in an anticlockwise direction i.e. from top to left, left to bottom, bottom to right, and from right to top one at a time using nothing but a temporary variable to achieve this

# In the example, 4*4 matrix will have n/2 boundaries
# Step by step movement of the outer boundary, elements will be moved in a boundary of 4, starting from the top most outer right element
# Follow the below steps to solve the problem

def expected_2d_rotate(mat):
    """Expected approach 2D matrix rotation"""
    
    # there are n/2 squares or cycles in a matrix of side n. Run a loop to traverse the matrix a cycle at a time.
    n = len(mat)

    # Tranverse the matrix a cycle at a time
    for i in range(n//2):
        for j in range(i, n - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]
              ]
    
    rotate_2d_matrix(matrix)
    expected_2d_rotate(matrix)

    for row in matrix:
        print(" ".join(map(str, row)))
