#!/usr/bin/python3
"""
N-Queens Problem Solver

Usage: nqueens N
"""
import sys


def check_valid(board, row, col, n):
    """
    checks if placing a queen at a certain
    position is valid on the board
    """
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def printer(board):
    """
    Prints the solution for current board
    """
    print("[", end="")
    for i, col in enumerate(board):
        if i != 0:
            print(", ", end="")
        print("[{}, {}]".format(i, col), end="")
    print("]")


def nqueens_sol(board, row, n):
    """
    finds and prints all solutions to N-queens problem
    """
    if row == n:
        printer(board)
        print()
        return

    for col in range(n):
        if check_valid(board, row, col, n):
            board[row] = col
            nqueens_sol(board, row + 1, n)


def main():
    """
    Main entry point to the program
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens_sol(board, 0, N)


if __name__ == "__main__":
    main()
