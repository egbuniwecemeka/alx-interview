#!/usr/bin/python3
"""A python script that determines the least coins needed for a given total"""

from typing import List

def count(coins: List[int], n: int, total: int) -> int:
    """Returns fewest number of coins needed to meet the total"""
    # Base case 1: If total is 0. THere's only a single way to do this
    # i.e. by not chosing any coins
    if total == 0:
        print(0)
        return 0
    
    # Base case 2: If total is negative or no coins are left to consider
    # i.e n === coins.length
    if total < 0 or n == 0:
        print(-1)
        return -1
    
    # Recurrence relation
    return count(coins, total - coins[n - 1]) + count(coins, n - 1, total)

def makeChange(coins, total):
    """Returns fewest number of coins needed to meet the total"""
    return count(coins, len(coins), total)

if __name__ == "__main__":
    coins = [1, 2, 5, 4]
    total = 10
    makeChange(coins, total)
