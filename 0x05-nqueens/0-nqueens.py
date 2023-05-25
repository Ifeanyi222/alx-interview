#!/usr/bin/python3
"""N queens"""


import sys


def generate_solutions(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for i in range(column):
            if is_safe(queen, i, array):
                safe_position.append(array + [i])
    return safe_position


def is_safe(k, i, array):
    if i in array:
        return (False)
    else:
        return all(abs(array[column] - i) != k - column
                   for column in range(k))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    solutions = generate_solutions(n, n)
    for array in solutions:
        clean = []
        for k, i in enumerate(array):
            clean.append([k, i])
        print(clean)


if __name__ == '__main__':
    n_queens()
