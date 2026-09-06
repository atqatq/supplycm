"""Simple Moving Average (SMA) forecast."""
from typing import List


def simple_moving_average(data: List[float], window: int = 3) -> List[float]:
    """Compute simple moving average forecast.

    Args:
        data: Time series of historical values.
        window: Number of periods to average.

    Returns:
        List of forecasted values aligned to the input length. The first
        ``window - 1`` entries are NaN-free because the SMA is only defined
        once enough observations are available; we return None placeholders.

    Example:
        >>> simple_moving_average([10, 20, 30, 40], 2)
        [None, 15.0, 25.0, 35.0]
    """
    if window <= 0:
        raise ValueError("window must be positive")
    out: List[float] = []
    for i in range(len(data)):
        if i + 1 < window:
            out.append(None)
        else:
            out.append(sum(data[i + 1 - window:i + 1]) / window)
    return out
