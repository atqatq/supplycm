"""Tracking signal for forecast bias monitoring."""
from typing import List


def tracking_signal(actual: List[float], forecast: List[float]) -> List[float]:
    """Tracking signal = cumulative forecast error / MAD.

    Example:
        >>> ts = tracking_signal([10, 20, 30], [12, 18, 30])
        >>> round(ts[-1], 4)
        0.0
    """
    n = len(actual)
    if n != len(forecast):
        raise ValueError("lengths must match")
    errors = [actual[i] - forecast[i] for i in range(n)]
    out = []
    cum = 0.0
    mad = 0.0
    for t in range(n):
        cum += errors[t]
        mad = (mad * t + abs(errors[t])) / (t + 1)
        out.append(cum / mad if mad != 0 else 0.0)
    return out
