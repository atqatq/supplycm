"""Fractional knapsack (greedy)."""
from typing import List, Tuple


def fractional_knapsack(weights: List[float], values: List[float], capacity: float) -> Tuple[float, List[float]]:
    """Greedy: take items by value/weight ratio.

    Example:
        >>> val, amounts = fractional_knapsack([2, 3, 4], [3, 4, 5], 5)
        >>> val == 7.0
        True
    """
    n = len(weights)
    ratios = sorted(range(n), key=lambda i: -values[i] / weights[i] if weights[i] > 0 else 0)
    total_value = 0.0
    amounts = [0.0] * n
    remaining = capacity
    for i in ratios:
        if weights[i] <= remaining:
            amounts[i] = 1.0
            total_value += values[i]
            remaining -= weights[i]
        else:
            frac = remaining / weights[i]
            amounts[i] = frac
            total_value += values[i] * frac
            remaining = 0
            break
    return total_value, amounts
