"""Weighted Moving Average (WMA) forecast."""
from typing import List, Optional


def weighted_moving_average(data: List[float], weights: Optional[List[float]] = None) -> List[float]:
    """Weighted moving average forecast.

    Args:
        data: Time series observations.
        weights: Weights applied to the most recent observations (newest last).
            If None, defaults to linear weights ``[1, 2, ..., n]``.

    Returns:
        List of weighted averages (None for warmup periods).

    Example:
        >>> weighted_moving_average([10, 20, 30, 40], [1, 2, 3])
        [None, None, 23.33..., 33.33...]
    """
    n = len(data)
    if weights is None:
        weights = list(range(1, n + 1))
    w = list(weights)
    window = len(w)
    if window > n:
        raise ValueError("weights window longer than data")
    total_w = sum(w)
    out: List[float] = []
    for i in range(n):
        if i + 1 < window:
            out.append(None)
        else:
            slice_ = data[i + 1 - window:i + 1]
            out.append(sum(s * wi for s, wi in zip(slice_, w)) / total_w)
    return out
