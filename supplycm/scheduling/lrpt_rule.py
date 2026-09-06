"""Longest Remaining Processing Time rule."""
from typing import List


def lrpt_rule(remaining_times: List[float]) -> int:
    """Return index of job with longest remaining time.

    Example:
        >>> lrpt_rule([3, 5, 2])
        1
    """
    if not remaining_times:
        return -1
    return max(range(len(remaining_times)), key=lambda i: remaining_times[i])
