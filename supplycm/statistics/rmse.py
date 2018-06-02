"""Root Mean Squared Error (RMSE)."""
from typing import List
import math


def rmse(actual: List[float], forecast: List[float]) -> float:
    """RMSE = sqrt(mean((A-F)^2)).

    Example:
        >>> round(rmse([1, 2, 3], [1, 2, 4]), 4)
        0.5774
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    return math.sqrt(sum((a - f) ** 2 for a, f in zip(actual, forecast)) / n)
