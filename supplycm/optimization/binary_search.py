"""Binary search."""
from typing import List


def binary_search(arr: List, target) -> int:
    """Return index of target or -1.

    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
