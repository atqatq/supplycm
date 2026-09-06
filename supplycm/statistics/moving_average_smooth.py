"""Centered moving average smoothing."""
from typing import List


def moving_average_smooth(data: List[float], window: int = 3) -> List[float]:
    """Centered moving average smoothing.

    Example:
        >>> moving_average_smooth([1, 2, 3, 4, 5], 3)
        [1.5, 2.0, 3.0, 4.0, 4.5]
    """
    n = len(data)
    half = window // 2
    out: List[float] = []
    for i in range(n):
        lo = max(0, i - half)
        hi = min(n, i + half + 1)
        out.append(sum(data[lo:hi]) / (hi - lo))
    return out
