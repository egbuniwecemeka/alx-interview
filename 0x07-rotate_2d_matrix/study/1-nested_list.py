#!/usr/bin/env python3
"""Nested list"""

# transpose rows and columns of the following 3*4 matrix

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
mat_res = [[row[i] for row in matrix] for i in range(4)]
print(mat_res)

# Similarly
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)


transposed_val = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# del statement - removes an item from a list using its index instead of value
del transposed[1]