#!/usr/bin/python3


import sys


def print_board(board):
    """
    Prints the board
    :param board: 2D list representing the board
    """
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n, row_mask, ld_mask, rd_mask):
    """
    Checks if it is safe to place a queen at a specific position on the board
    :param board: 2D list representing the board
    :param row: row to place queen
    :param col: column to place queen
    :param n: size of the board
    :param row_mask: bitmask indicating which rows have already been used
    :param ld_mask: bitmask indicating which left diagonals have already been used
    :param rd_mask: bitmask indicating which right diagonals have already been used
    :return: True if it is safe, False if not
    """
    # Check the row mask to see if this row has already been used
    if row_mask & (1 << row):
        return False

    # Check the left diagonal mask to see if this diagonal has already been used
    if ld_mask & (1 << (row + col)):
        return False

    # Check the right diagonal mask to see if this diagonal has already been used
    if rd_mask & (1 << (n - 1 - row + col)):
        return False

    return True


def solve_n_queens(board, col, n, row_mask, ld_mask, rd_mask):
    """
    Solves the N queens problem using backtracking and bit manipulation
    :param board: 2D list representing the board
    :param col: column to start in
    :param n: size of the board
    :param row_mask: bitmask indicating which rows have already been used
    :param ld_mask: bitmask indicating which left diagonals have already been used
    :param rd_mask: bitmask indicating which right diagonals have already been used
    """
    # Base case: if all queens are placed, print the board
    if col == n:
        print_board(board)
        print()
        return

    # Compute the valid positions for the current column
    valid_positions = ((1 << n) - 1) & ~(row_mask | ld_mask | rd_mask)

    # Recur for each valid position
    while valid_positions:
        # Get the least significant bit in the valid positions
        position = valid_positions & -valid_positions

        # Clear the least significant bit in the valid positions
        valid_positions &= valid_positions - 1

        # Compute the row and place the queen
        row = bin(position - 1).count("1")
        board[row][col] = "Q"

        # Update the masks
        row_mask |= 1 << row
        ld_mask |= 1 << (row + col)
        rd_mask |= 1 << (n - 1 - row + col)

        # Recur for the next column
        solve_n_queens(board, col + 1, n, row_mask, ld_mask, rd_mask)

        # Remove the queen and update the masks
        board[row][col] = "."
        row_mask &= ~(1 << row)
        ld_mask &= ~(1 << (row + col))
        rd_mask &= ~(1 << (n - 1 - row + col))


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board and masks
    board = [["." for _ in range(n)] for _ in range(n)]
    row_mask = 0
    ld_mask = 0
    rd_mask = 0

    # Solve the N queens problem
    solve_n_queens(board, 0, n, row_mask, ld_mask, rd_mask)
