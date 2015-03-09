"""Seasonal naive forecast."""
from typing import List


def seasonal_naive_forecast(data: List[float], season_length: int = 4) -> List[float]:
    """Forecast using the observation from the same period of the previous season.

    Example:
        >>> seasonal_naive_forecast([10,20,30,40,50,60], 4)
        [None, None, None, None, 10.0, 20.0]
    """
    if season_length <= 0:
        raise ValueError("season_length must be positive")
    out: List[float] = []
    for i in range(len(data)):
        if i < season_length:
            out.append(None)
        else:
            out.append(float(data[i - season_length]))
    return out
