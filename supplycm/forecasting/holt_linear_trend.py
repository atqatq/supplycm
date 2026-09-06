"""Holt's linear trend exponential smoothing (1957)."""
from typing import List, Tuple


def holt_linear_trend(data: List[float],
                      alpha: float = 0.5,
                      beta: float = 0.1) -> Tuple[List[float], List[float]]:
    """Holt's linear trend method.

    Maintains separate level (L) and trend (T) components.

    Args:
        data: Observations.
        alpha: Level smoothing factor.
        beta: Trend smoothing factor.

    Returns:
        Tuple of (level series, trend series).

    Example:
        >>> L, T = holt_linear_trend([1, 2, 3, 4])
        >>> round(L[-1], 4), round(T[-1], 4)
        (4.0, 1.0)
    """
    if not 0 < alpha < 1 or not 0 < beta < 1:
        raise ValueError("alpha and beta must be in (0, 1)")
    if len(data) < 2:
        raise ValueError("need at least 2 observations")
    level = [float(data[0])]
    trend = [float(data[1] - data[0])]
    for t in range(1, len(data)):
        new_level = alpha * data[t] + (1 - alpha) * (level[-1] + trend[-1])
        new_trend = beta * (new_level - level[-1]) + (1 - beta) * trend[-1]
        level.append(new_level)
        trend.append(new_trend)
    return level, trend
