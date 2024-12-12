#!/usr/bin/env python3
""""""
from typing import List

def isPrime(nums: List[int]):
    for num in nums:
        # Check if i is less than one
        if num <= 0:
            return 'Negative'
        # If num is even (multiple of 2)
        if num % 2 == 0:
            return 'Even'
        return num
    

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 9]
    res = isPrime(array)
    print(f'Result: {res}')