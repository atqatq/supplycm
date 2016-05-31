"""Rolling mean forecast."""
from typing import List


def rolling_mean_forecast(data: List[float], window: int = 3, horizon: int = 1) -> List[float]:
    """Forecast using the mean of the last ``window`` observations.

    Example:
        >>> rolling_mean_forecast([10, 20, 30, 40], window=2, horizon=2)
        [35.0, 35.0]
    """
    if window <= 0:
        raise ValueError("window must be positive")
    if len(data) < window:
        raise ValueError("not enough data")
    last_window = data[-window:]
    mean = sum(last_window) / window
    return [mean] * horizon
