"""Subset sum problem via DP."""
from typing import List, Set


def subset_sum(nums: List[int], target: int) -> bool:
    """Determine if a subset sums to target.

    Example:
        >>> subset_sum([3, 34, 4, 12, 5, 2], 9)
        True
    """
    possible = {0}
    for n in nums:
        new_possible = set()
        for s in possible:
            new_possible.add(s + n)
        possible |= new_possible
        if target in possible:
            return True
    return target in possible
