"""Smooth noisy sensor data using exponential weighted moving average."""
from typing import List


def sensor_data_smoothing(raw_data: List[float], alpha: float = 0.3) -> List[float]:
    """Apply exponential smoothing to sensor readings.

    Args:
        raw_data: Noisy sensor values.
        alpha: Smoothing factor (0 to 1). Higher = more responsive.

    Returns:
        Smoothed data series.

    Example:
        >>> result = sensor_data_smoothing([10, 15, 12, 18, 11], 0.5)
        >>> len(result) == 5
        True
    """
    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")
    if not raw_data:
        return []
    smoothed = [float(raw_data[0])]
    for x in raw_data[1:]:
        smoothed.append(alpha * x + (1 - alpha) * smoothed[-1])
    return smoothed
