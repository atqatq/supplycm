"""Ljung-Box test for autocorrelation."""
from typing import List
import math


def ljung_box_test(residuals: List[float], max_lag: int = 10) -> float:
    """Compute Ljung-Box Q statistic.

    Example:
        >>> q = ljung_box_test([1, -1, 1, -1, 1, -1, 1, -1, 1, -1], 5)
        >>> q > 0
        True
    """
    n = len(residuals)
    if n < max_lag + 1:
        raise ValueError("not enough residuals")
    mean = sum(residuals) / n
    centered = [r - mean for r in residuals]
    var = sum(c * c for c in centered) / n
    if var == 0:
        return 0.0
    def acf(k):
        return sum(centered[t] * centered[t - k] for t in range(k, n)) / n / var
    q = n * (n + 2) * sum(acf(k) ** 2 / (n - k) for k in range(1, max_lag + 1))
    return q
