#!/usr/bin/env python3
"""A script """
from typing import List

def isPrime(nums: List[int]) -> List[int]:
    """ Returns a list of prime numbers from a list of integers
        Args:
            nums - A list of integers
        Returns:
            A list of prime numbers
    """
    return [num for num in nums]
    

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 9]
    res = isPrime(array)
    print(f'Result: {res}')