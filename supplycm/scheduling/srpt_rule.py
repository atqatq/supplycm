"""Shortest Remaining Processing Time rule."""
from typing import List


def srpt_rule(remaining_times: List[float]) -> int:
    """Return index of job with shortest remaining time.

    Example:
        >>> srpt_rule([3, 5, 2])
        2
    """
    if not remaining_times:
        return -1
    return min(range(len(remaining_times)), key=lambda i: remaining_times[i])
