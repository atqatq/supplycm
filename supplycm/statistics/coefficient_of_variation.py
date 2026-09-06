"""Coefficient of variation."""
from typing import List
import math


def coefficient_of_variation(data: List[float]) -> float:
    """CV = std / mean.

    Example:
        >>> round(coefficient_of_variation([10, 20, 30]), 4)
        0.4082
    """
    if len(data) < 2:
        raise ValueError("need at least 2 observations")
    mean = sum(data) / len(data)
    if mean == 0:
        return float('inf')
    var = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(var) / mean
