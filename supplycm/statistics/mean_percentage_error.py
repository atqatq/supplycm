"""Mean Percentage Error (MPE)."""
from typing import List


def mean_percentage_error(actual: List[float], forecast: List[float]) -> float:
    """MPE = mean((F-A)/A) * 100.

    Example:
        >>> round(mean_percentage_error([100, 200], [110, 190]), 2)
        0.0
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    total = 0.0
    count = 0
    for a, f in zip(actual, forecast):
        if a != 0:
            total += (f - a) / a
            count += 1
    if count == 0:
        return float('inf')
    return 100 * total / count
