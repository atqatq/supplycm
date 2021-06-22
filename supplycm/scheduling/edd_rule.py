"""Earliest Due Date dispatching rule."""
from typing import List


def edd_rule(due_dates: List[float]) -> List[int]:
    """Order jobs by earliest due date.

    Example:
        >>> edd_rule([10, 5, 8, 2])
        [3, 1, 2, 0]
    """
    return sorted(range(len(due_dates)), key=lambda i: due_dates[i])
