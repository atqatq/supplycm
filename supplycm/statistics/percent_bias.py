"""Percent bias (PBIAS)."""
from typing import List


def percent_bias(actual: List[float], forecast: List[float]) -> float:
    """PBIAS = sum(F-A) / sum(A) * 100.

    Example:
        >>> round(percent_bias([10, 20, 30], [12, 18, 32]), 2)
        4.0
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    sum_a = sum(actual)
    if sum_a == 0:
        return float('inf')
    return 100 * sum(f - a for a, f in zip(actual, forecast)) / sum_a
