#!/usr/bin/python3
"""
Pascal's Triangle Algorithm
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n-th number of rows
    Returns: A list of lists representing Pascal's triangle
    """
    triangle = [[1]]

    for i in range(n - 1):
        # create a temp row with 0s at beginning & end
        temp = [0] + triangle[-1] + [0]
        row = []
        # get values for new row (summing adjacent elements in temp row)
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle
