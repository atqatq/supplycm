"""Mean forecast bias."""
from typing import List


def bias(actual: List[float], forecast: List[float]) -> float:
    """Bias = mean(F - A).

    Example:
        >>> bias([10, 20, 30], [12, 18, 32])
        0.6666...
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    return sum(f - a for a, f in zip(actual, forecast)) / n
