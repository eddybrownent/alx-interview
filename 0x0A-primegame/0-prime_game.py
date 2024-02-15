#!/usr/bin/python3
"""
Script to determine who the winner of each game is
"""


def is_prime(num):
    """
    function to check is a number is prime

    Args:
        num: the number to check

    Returns:
        bool: True if number is prime else False
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def optimal_move(n):
    """
    determines optimal move for current player

    Args:
        n: current number in the game

    Returns:
        int: prime number to remove & its multiples, or 0 if no prime
    """
    for i in range(2, n + 1):
        if is_prime(i) and n % i == 0:
            return i
    return 0


def isWinner(x, nums):
    """
    determines the winner of the prime game

    Args:
        x: number of rounds
        nums: an array of n for each round

    Returns:
    str or None: Name of the player that won, or None
    """
    player_maria = 0
    player_ben = 0

    if x < 1 or not nums:
        return None

    for n in nums:
        x = sum(1 for i in range(2, n + 1) if is_prime(i))

        if x % 2 == 0:
            player_ben += 1
        else:
            player_maria += 1

    if player_maria < player_ben:
        return "Ben"
    elif player_ben < player_maria:
        return "Maria"
    else:
        return None
