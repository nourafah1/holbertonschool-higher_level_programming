#!/usr/bin/python3
"""Solves the N queens problem."""

import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed safely."""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve(n, row=0, queens=[]):
    """Find and print all N queens solutions."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            solve(n, row + 1, queens + [[row, col]])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solve(n)
