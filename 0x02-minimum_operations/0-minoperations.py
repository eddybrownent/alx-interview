#!/usr/bin/python3
"""
method that calculates fewest num of operations needed
to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Calculates fewest number of operations

    :param n: target number of H chars
    :return: minimum num operations to achieve n H chars , 0 if impossible
    """
    if n <= 1:
        return 0

    operas = 0
    div = 2

    while n > 1:
        while n % div == 0:
            n //= div
            operas += div

        div += 1

    return operas
