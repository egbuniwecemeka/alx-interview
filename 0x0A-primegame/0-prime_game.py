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
    def isprime(n: int) -> bool:
        """Checks if a nmber is prime or even"""
        if n <= 0:
            print('Input a positive integer')
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in nums if isprime(num)]
    

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 9]
    res = isPrime(array)
    print(f'Result: {res}')