"""Confidence interval for the mean (normal)."""
from typing import List, Tuple
import math


def confidence_interval_mean(data: List[float], z: float = 1.96) -> Tuple[float, float]:
    """CI = mean ± z * (s / sqrt(n)).

    Example:
        >>> lo, hi = confidence_interval_mean([10, 20, 30, 40, 50])
        >>> lo < 30 < hi
        True
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    se = math.sqrt(var / n)
    return mean - z * se, mean + z * se
