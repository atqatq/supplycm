"""Single Exponential Smoothing."""
from typing import List


def single_exponential_smoothing(data: List[float], alpha: float = 0.3) -> List[float]:
    """Single (simple) exponential smoothing.

    Recurrence: ``s_t = alpha * x_t + (1 - alpha) * s_{t-1}``.

    Args:
        data: Observations.
        alpha: Smoothing factor in (0, 1).

    Returns:
        Smoothed series of same length as input.

    Example:
        >>> single_exponential_smoothing([10, 20, 30], 0.5)
        [10.0, 15.0, 22.5]
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0, 1)")
    if not data:
        return []
    out = [float(data[0])]
    for x in data[1:]:
        out.append(alpha * x + (1 - alpha) * out[-1])
    return out
