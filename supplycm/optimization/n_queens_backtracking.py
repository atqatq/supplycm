"""N-Queens problem via backtracking."""
from typing import List, Optional


def n_queens_backtracking(n: int) -> Optional[List[int]]:
    """Find one solution to N-Queens.

    Returns list of column positions (index = row) or None.

    Example:
        >>> sol = n_queens_backtracking(4)
        >>> sol is not None
        True
    """
    def is_safe(positions, row, col):
        for r, c in enumerate(positions):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    def solve(positions, row):
        if row == n:
            return positions
        for col in range(n):
            if is_safe(positions, row, col):
                result = solve(positions + [col], row + 1)
                if result is not None:
                    return result
        return None
    return solve([], 0)
