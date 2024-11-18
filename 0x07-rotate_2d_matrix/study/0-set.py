#!/usr/bin/env python3
"""Sets"""

word = set('abracadabra')
word1 = set('aladin')
print(word)

fruits = {'apple', 'orange', 'apple', 'carrot', 'mango', 'apple'}
print(fruits)   #  show that duplicates have been removed

membership = 'orange' in fruits
print(membership)

alpha_diff = word - word1
alpha_or = word | word1
alpha_and = word & word1
alpha_neg = word ^ word1
print(alpha_diff)
print(alpha_or)
print(alpha_and)
print(alpha_neg)

# Comprehensions can also be used on sets
a = {x for x in word if x not in 'abc'}
print(a)