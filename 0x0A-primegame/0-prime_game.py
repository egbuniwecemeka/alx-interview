#!/usr/bin/env python3
"""A script that selects the winner of a game of prime numbers"""

def isWinner(x, nums):
    """
    Determine the winner of a game of prime numbers

    Args:
        x (int): Number of rounds.
        nums (list): List of integers
    
    Returns:
        str or None: Name of the winner ('Maria' or 'Ben' or None if tied)
    """
    if x < 1 or not nums:
        return None
    
    # Find the maxium number in nums for prime sieve
    max_num = max(nums)

    # Generate a list of primes using Sieve of Eratosthenes
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[1]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False
    
    # Precompute the number of primes up to each number
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine winners for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 0: # Ben wins if the count is even
            ben_wins += 1
        else: # Maria wins if the count is odd
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
