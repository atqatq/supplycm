"""Dampened trend exponential smoothing."""
from typing import List


def dampened_trend(data: List[float],
                   alpha: float = 0.5,
                   beta: float = 0.1,
                   phi: float = 0.95,
                   horizon: int = 1) -> List[float]:
    """Dampened trend Holt's method (Gardner & McKenzie 1985).

    Args:
        data: Observations.
        alpha: Level smoothing.
        beta: Trend smoothing.
        phi: Dampening factor (0 < phi <= 1).
        horizon: Forecast horizon.

    Returns:
        Forecasts for the next horizon periods.

    Example:
        >>> f = dampened_trend([1, 2, 3, 4, 5], phi=0.9, horizon=2)
        >>> len(f) == 2
        True
    """
    if not 0 < alpha < 1 or not 0 < beta < 1 or not 0 < phi <= 1:
        raise ValueError("invalid parameters")
    if len(data) < 2:
        raise ValueError("need at least 2 observations")
    level = float(data[0])
    trend = float(data[1] - data[0])
    for t in range(1, len(data)):
        new_level = alpha * data[t] + (1 - alpha) * (level + phi * trend)
        new_trend = beta * (new_level - level) + (1 - beta) * phi * trend
        level, trend = new_level, new_trend
    forecasts = []
    cum_phi = 0.0
    phi_pow = 1.0
    for h in range(horizon):
        cum_phi += phi_pow
        phi_pow *= phi
        forecasts.append(level + cum_phi * trend)
    return forecasts
