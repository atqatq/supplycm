"""Mean Absolute Percentage Error (MAPE)."""
from typing import List


def mape(actual: List[float], forecast: List[float]) -> float:
    """MAPE = mean(|A-F|/|A|) * 100.

    Example:
        >>> round(mape([100, 200, 300], [110, 190, 310]), 2)
        6.0
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    total = 0.0
    count = 0
    for a, f in zip(actual, forecast):
        if a != 0:
            total += abs(a - f) / abs(a)
            count += 1
    if count == 0:
        return float('inf')
    return 100 * total / count
