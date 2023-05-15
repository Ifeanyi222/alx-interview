#!/usr/bin/python3
"""0. Minimum Operations """


def minOperations(n):

    if n <= 1:
        return 0
    j = 2
    count = 0
    while j <= n:
        if n % j == 0:
            count += j
            n = n / j
        else:
            j += 1
    return count
