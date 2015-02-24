"""Naive forecast."""
from typing import List


def naive_forecast(data: List[float]) -> List[float]:
    """Naive forecast: forecast equals last observed value.

    Example:
        >>> naive_forecast([1, 2, 3, 4])
        [None, 1.0, 2.0, 3.0]
    """
    if not data:
        return []
    return [None] + [float(x) for x in data[:-1]]
