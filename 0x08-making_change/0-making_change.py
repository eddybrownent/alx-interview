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

    min_coins_table = [[float('inf')] * (total + 1)
                       for _ in range(num_coin_types + 1)]

    for i in range(num_coin_types + 1):
        min_coins_table[i][0] = 0

    for i in range(1, num_coin_types + 1):
        for j in range(1, total + 1):
            current_coin_value = coins[i - 1]
            if current_coin_value > j:
                min_coins_table[i][j] = min_coins_table[i - 1][j]
            else:
                min_coins_table[i][j] = min(
                        min_coins_table[i - 1][j],
                        1 + min_coins_table[i][j - current_coin_value]
                        )

    result = min_coins_table[num_coin_types][total]

    return result if result != float('inf') else -1
