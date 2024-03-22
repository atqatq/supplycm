"""Best-fit bin packing."""
from typing import List


def bin_packing_best_fit(items: List[float], bin_capacity: float) -> List[List[float]]:
    """Place each item in bin with least remaining space that fits.

    Example:
        >>> bins = bin_packing_best_fit([2, 5, 4, 7, 1, 3, 8], 10)
        >>> sum(sum(b) for b in bins) == 30
        True
    """
    bins = []
    for item in items:
        best_idx = -1
        best_remaining = float('inf')
        for i, b in enumerate(bins):
            remaining = bin_capacity - sum(b)
            if remaining >= item and remaining - item < best_remaining:
                best_remaining = remaining - item
                best_idx = i
        if best_idx >= 0:
            bins[best_idx].append(item)
        else:
            bins.append([item])
    return bins
