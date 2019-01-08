"""Exponential smoothing filter."""
from typing import List


def exponential_smooth(data: List[float], alpha: float = 0.3) -> List[float]:
    """Apply exponential smoothing.

    Example:
        >>> exponential_smooth([10, 20, 30], 0.5)
        [10.0, 15.0, 22.5]
    """
    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")
    if not data:
        return []
    out = [float(data[0])]
    for x in data[1:]:
        out.append(alpha * x + (1 - alpha) * out[-1])
    return out
