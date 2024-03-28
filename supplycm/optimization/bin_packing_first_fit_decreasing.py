"""First-fit decreasing bin packing."""
from typing import List
from .bin_packing_first_fit import bin_packing_first_fit


def bin_packing_first_fit_decreasing(items: List[float], bin_capacity: float) -> List[List[float]]:
    """Sort items descending then first-fit.

    Example:
        >>> bins = bin_packing_first_fit_decreasing([2, 5, 4, 7, 1, 3, 8], 10)
        >>> sum(sum(b) for b in bins) == 30
        True
    """
    sorted_items = sorted(items, reverse=True)
    return bin_packing_first_fit(sorted_items, bin_capacity)
