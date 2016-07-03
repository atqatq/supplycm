"""Croston's method with exponential decay for ageing demand."""
from typing import List


def croston_with_decay(data: List[float], alpha: float = 0.2, decay: float = 0.95) -> List[float]:
    """Croston's variant that applies decay to demand-size between demands.

    Example:
        >>> out = croston_with_decay([0, 10, 0, 0, 20, 0, 5], 0.2, 0.9)
        >>> len(out) == 7
        True
    """
    if not 0 < alpha < 1 or not 0 < decay <= 1:
        raise ValueError("invalid parameters")
    n = len(data)
    z = 0.0
    out = [0.0] * n
    for t in range(n):
        if data[t] > 0:
            z = alpha * data[t] + (1 - alpha) * z if z > 0 else data[t]
        else:
            z *= decay
        out[t] = z
    return out
