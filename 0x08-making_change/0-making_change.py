#!/usr/bin/python3
"""
This Module determines the fewest num of
coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins to make up the target amount

    Parameters:
              coins: List of coin denominations.
              target_amount: The desired total amount to make up

    Returns:
          int: minimum num of coins to make up the target amount.
               else Returns -1 if it's not possible
    """
    if total == 0:
        return 0

    coins.sort()
    num_coin_types = len(coins)

    min_coins_table = [float('inf')] * (total + 1)
    min_coins_table[0] = 0

    for i in range(1, num_coin_types + 1):
        for j in range(coins[i - 1], total + 1):
            min_coins_table[j] = min(
                    min_coins_table[j],
                    1 + min_coins_table[j - coins[i - 1]])

    result = min_coins_table[total]

    return result if result != float('inf') else -1
