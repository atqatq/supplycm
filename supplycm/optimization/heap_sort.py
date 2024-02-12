"""Heap sort."""
from typing import List


def heap_sort(arr: List) -> List:
    """Sort using binary heap.

    Example:
        >>> heap_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    import heapq
    h = list(arr)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(arr))]
