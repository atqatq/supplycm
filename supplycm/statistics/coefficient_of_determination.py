"""Alias for R-squared."""
from typing import List


def coefficient_of_determination(actual: List[float], forecast: List[float]) -> float:
    """Compute R^2.

    Example:
        >>> round(coefficient_of_determination([1, 2, 3, 4], [1, 2, 3, 4]), 4)
        1.0
    """
    n = len(actual)
    if n != len(forecast) or n < 2:
        raise ValueError("equal non-trivial lengths required")
    mean_a = sum(actual) / n
    ss_res = sum((a - f) ** 2 for a, f in zip(actual, forecast))
    ss_tot = sum((a - mean_a) ** 2 for a in actual)
    if ss_tot == 0:
        return 1.0
    return 1 - ss_res / ss_tot
