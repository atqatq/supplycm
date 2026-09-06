"""Mean Absolute Error (MAE)."""
from typing import List


def mae(actual: List[float], forecast: List[float]) -> float:
    """MAE = mean(|A-F|).

    Example:
        >>> mae([1, 2, 3], [1, 2, 5])
        0.6666...
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    return sum(abs(a - f) for a, f in zip(actual, forecast)) / n
