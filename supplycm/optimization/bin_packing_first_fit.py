"""First-fit bin packing heuristic."""
from typing import List


def bin_packing_first_fit(items: List[float], bin_capacity: float) -> List[List[float]]:
    """Place each item in first bin that fits.

    Example:
        >>> bins = bin_packing_first_fit([2, 5, 4, 7, 1, 3, 8], 10)
        >>> sum(sum(b) for b in bins) == 30
        True
    """
    bins = []
    for item in items:
        placed = False
        for b in bins:
            if sum(b) + item <= bin_capacity:
                b.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    return bins
