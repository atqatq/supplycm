"""Longest Increasing Subsequence (O(n log n))."""
from typing import List
import bisect


def longest_increasing_subsequence(seq: List) -> int:
    """Length of LIS.

    Example:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    if not seq:
        return 0
    tails = []
    for x in seq:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
