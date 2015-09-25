"""Theil's U statistic for forecast accuracy."""
from typing import List
import math


def theils_u(actual: List[float], forecast: List[float]) -> float:
    """Theil's U: sqrt(mean((F-A)^2)) / sqrt(mean(A^2)).

    Example:
        >>> round(theils_u([10, 20, 30], [11, 19, 31]), 4)
        0.0393
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("actual and forecast must have equal non-zero length")
    num = sum((forecast[i] - actual[i]) ** 2 for i in range(n)) / n
    den = sum(actual[i] ** 2 for i in range(n)) / n
    if den == 0:
        return 0.0
    return math.sqrt(num / den)
