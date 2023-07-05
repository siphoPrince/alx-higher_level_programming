#!/usr/bin/python3
import sys
"""defines a sove queen class"""


def solve_nqueens(N):
    """refers to nqueens"""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - col == i - row or \
                board[i] - col == row - i:
                return False
        return True

    def solve_util(board, row):
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_util(board, row + 1)

    board = [-1] * N
    solve_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
