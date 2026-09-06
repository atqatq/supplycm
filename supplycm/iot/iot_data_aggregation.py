"""Aggregate IoT sensor data by time window."""
from typing import List, Tuple, Dict


def iot_data_aggregation(timestamps: List[float], values: List[float],
                          window_size: float) -> List[Dict]:
    """Aggregate sensor readings into time windows.

    Args:
        timestamps: List of timestamps.
        values: Corresponding sensor values.
        window_size: Time window for aggregation.

    Returns:
        List of dicts with window stats (mean, min, max, count).

    Example:
        >>> result = iot_data_aggregation(
        ...     [1, 2, 3, 4, 5], [10, 20, 30, 40, 50], window_size=2)
        >>> len(result) >= 2
        True
    """
    if len(timestamps) != len(values):
        raise ValueError("lengths must match")
    if not timestamps:
        return []
    windows = []
    t_start = timestamps[0]
    current_vals = []
    for t, v in zip(timestamps, values):
        if t - t_start >= window_size and current_vals:
            windows.append({
                'start': t_start,
                'end': t,
                'mean': sum(current_vals) / len(current_vals),
                'min': min(current_vals),
                'max': max(current_vals),
                'count': len(current_vals),
            })
            t_start = t
            current_vals = []
        current_vals.append(v)
    if current_vals:
        windows.append({
            'start': t_start,
            'end': timestamps[-1],
            'mean': sum(current_vals) / len(current_vals),
            'min': min(current_vals),
            'max': max(current_vals),
            'count': len(current_vals),
        })
    return windows
