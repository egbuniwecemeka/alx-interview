#!/usr/bin/python3
"""A python script that determines the least coins needed for a given total"""

def makeChange(coins: int, total: int) -> int:
    """Returns fewest number of coins needed to meet the total"""
    n = len(coins)
    # Base case 1: If total is 0. THere's only a single way to do this
    # i.e. by not chosing any coins
    if total == 0:
        return 0
    
    # Base case 2: If total is negative or no coins are left to consider
    # i.e n === coins.length
    if total < 0 or n == 0:
        return -1
    
    print(f'n: ${n}')



if __name__ == "__main__":
    coins = [1,2,5]
    makeChange(coins, 10)
