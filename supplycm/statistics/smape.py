"""Symmetric MAPE (sMAPE)."""
from typing import List


def smape(actual: List[float], forecast: List[float]) -> float:
    """sMAPE = mean(2*|A-F| / (|A|+|F|)) * 100.

    Example:
        >>> round(smape([100, 200], [110, 190]), 2) < 6
        True
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    total = 0.0
    for a, f in zip(actual, forecast):
        denom = abs(a) + abs(f)
        if denom != 0:
            total += 2 * abs(a - f) / denom
    return 100 * total / n
