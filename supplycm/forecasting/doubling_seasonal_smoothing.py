"""3-parameter seasonal smoothing (Holt-Winters variant)."""
from typing import List


def doubling_seasonal_smoothing(data: List[float],
                                alpha: float = 0.3,
                                beta: float = 0.1,
                                gamma: float = 0.2,
                                season_length: int = 4,
                                horizon: int = 1) -> List[float]:
    """3-parameter smoothing with linear trend and additive seasonality.

    Example:
        >>> f = doubling_seasonal_smoothing([10,20,30,40,12,22,32,42], 0.3,0.1,0.2,4,2)
        >>> len(f) == 2
        True
    """
    if len(data) < 2 * season_length:
        raise ValueError("need at least 2 full seasons")
    level = sum(data[:season_length]) / season_length
    trend = (sum(data[season_length:2 * season_length]) - sum(data[:season_length])) / (season_length ** 2)
    seasonal = [data[i] - level for i in range(season_length)]
    n = len(data)
    for t in range(season_length, n):
        s = seasonal[t % season_length]
        new_level = alpha * (data[t] - s) + (1 - alpha) * (level + trend)
        new_trend = beta * (new_level - level) + (1 - beta) * trend
        seasonal[t % season_length] = gamma * (data[t] - new_level) + (1 - gamma) * s
        level, trend = new_level, new_trend
    forecasts = []
    for h in range(horizon):
        s = seasonal[(n + h) % season_length]
        forecasts.append(level + (h + 1) * trend + s)
    return forecasts
