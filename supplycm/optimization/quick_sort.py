"""Quick sort."""
from typing import List


def quick_sort(arr: List) -> List:
    """Quick sort with middle pivot.

    Example:
        >>> quick_sort([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
    """
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
