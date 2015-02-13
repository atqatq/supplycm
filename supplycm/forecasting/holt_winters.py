"""Holt-Winters triple exponential smoothing."""
from typing import List, Tuple


def holt_winters(data: List[float],
                 alpha: float = 0.5,
                 beta: float = 0.1,
                 gamma: float = 0.1,
                 season_length: int = 4,
                 multiplicative: bool = False) -> Tuple[List[float], List[float], List[float]]:
    """Holt-Winters triple exponential smoothing.

    Args:
        data: Observations.
        alpha: Level smoothing.
        beta: Trend smoothing.
        gamma: Seasonal smoothing.
        season_length: Number of periods in one season.
        multiplicative: Use multiplicative seasonality if True.

    Returns:
        Tuple of (level, trend, seasonal) series.

    Example:
        >>> L, T, S = holt_winters([10,20,30,40,50,60,70,80], 0.5,0.1,0.1,4)
        >>> len(L) == 8
        True
    """
    if season_length <= 0 or len(data) < 2 * season_length:
        raise ValueError("need at least 2 full seasons of data")
    n = len(data)
    level = [0.0] * n
    trend = [0.0] * n
    seasonals = [0.0] * n
    # Initialize level
    level[0] = sum(data[:season_length]) / season_length
    trend[0] = (sum(data[season_length:2 * season_length])
                - sum(data[:season_length])) / (season_length ** 2)
    # Initial seasonal indices
    avg_first_season = sum(data[:season_length]) / season_length
    for i in range(season_length):
        if multiplicative:
            seasonals[i] = data[i] / avg_first_season if avg_first_season else 1.0
        else:
            seasonals[i] = data[i] - avg_first_season
    for t in range(season_length, n):
        last_season = seasonals[t - season_length]
        if multiplicative:
            level[t] = alpha * (data[t] / last_season) + (1 - alpha) * (level[t - 1] + trend[t - 1])
            trend[t] = beta * (level[t] - level[t - 1]) + (1 - beta) * trend[t - 1]
            seasonals[t] = gamma * (data[t] / level[t]) + (1 - gamma) * last_season
        else:
            level[t] = alpha * (data[t] - last_season) + (1 - alpha) * (level[t - 1] + trend[t - 1])
            trend[t] = beta * (level[t] - level[t - 1]) + (1 - beta) * trend[t - 1]
            seasonals[t] = gamma * (data[t] - level[t]) + (1 - gamma) * last_season
    return level, trend, seasonals
