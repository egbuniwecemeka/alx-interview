#!/usr/bin/env python3
""""""
from typing import List

def isPrime(array: List[int]):
    if array <= 0:
        return 'Negative'
    for i in range(2, int(array**2) + 1):
        # If num is even (multiple of 2)
        if num % 2 == 0:
            return 'Even'
    return array
    

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 9]
    res = isPrime(array)
    print(f'Result: {res}')