#!/usr/bin/env python3
""""""
from typing import List

def isPrime(nums: List[int]) -> List[int]:
    def isprime(n: int) -> bool:
        # Check if n is negative
        if n <= 0:
            return False
        
        for i in range(2, int(n**2) + 1):
            if n % i == 0:
                return False
            return True
    
    return [num for num in nums if isprime(num)]
    

if __name__ == "__main__":
    array = [1, 3, 4, 5, 7, 9]
    res = isPrime(array)
    print(f'Result: {res}')