#!/usr/bin/env python3
"""A simple script on List Comprehensions"""

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)  # Should print the output of the squares for num 0-9

# Similarly
squares1 = list(map(lambda i: i**2, range(10)))
print(squares1)

# Similarly
squares2 = [i**2 for i in range(10)]
print(squares2)

# create a list of 2-tuples like (number, square)
list1 = [5, 10, 15, 20]
list2 = [25, 30, 35, 40]
squares3 = [(x, y**2) for x in list1 for y in list2 if x != y]
print(squares3)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for i in vec for num in i]
print(flat_list)
