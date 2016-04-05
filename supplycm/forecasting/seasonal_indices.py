"""Seasonal indices via ratio-to-moving-average."""
from typing import List


def seasonal_indices(data: List[float], season_length: int = 4) -> List[float]:
    """Compute seasonal indices (multiplicative) for one season.

    Example:
        >>> idx = seasonal_indices([10, 20, 30, 40, 12, 22, 32, 42], 4)
        >>> len(idx) == 4
        True
    """
    n = len(data)
    if n < 2 * season_length:
        raise ValueError("need at least 2 full seasons")
    # Centered moving average
    half = season_length // 2
    ma = [None] * n
    for t in range(half, n - half):
        window = data[t - half:t + half + 1]
        ma[t] = sum(window) / len(window)
    # Ratios
    ratios = [[] for _ in range(season_length)]
    for t in range(n):
        if ma[t] is not None and ma[t] != 0:
            ratios[t % season_length].append(data[t] / ma[t])
    indices = [sum(r) / len(r) if r else 1.0 for r in ratios]
    # Normalize to average 1
    avg = sum(indices) / season_length
    return [i / avg for i in indices]
