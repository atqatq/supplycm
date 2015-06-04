"""Drift method forecast."""
from typing import List


def drift_method(data: List[float], horizon: int = 1) -> List[float]:
    """Random walk with drift: F(t+h) = X(t) + h * (X(t)-X(1)) / (t-1).

    Example:
        >>> drift_method([10, 20, 30], horizon=2)
        [40.0, 50.0]
    """
    if len(data) < 2:
        raise ValueError("need at least 2 observations")
    n = len(data)
    drift = (data[-1] - data[0]) / (n - 1)
    return [data[-1] + (h + 1) * drift for h in range(horizon)]
