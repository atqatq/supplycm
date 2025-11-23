"""Compute seasonality index per period."""
from typing import List


def seasonality_index(demand_series: List[float], season_length: int) -> List[float]:
    """Seasonality index = period_avg / overall_avg.

    Example:
        >>> idx = seasonality_index([10, 20, 30, 40, 50, 60, 70, 80], 4)
        >>> len(idx) == 4
        True
    """
    if season_length <= 0 or len(demand_series) < season_length:
        raise ValueError("invalid season length or insufficient data")
    overall_avg = sum(demand_series) / len(demand_series)
    if overall_avg == 0:
        return [1.0] * season_length
    indices = []
    for i in range(season_length):
        period_values = demand_series[i::season_length]
        avg = sum(period_values) / len(period_values)
        indices.append(avg / overall_avg)
    return indices
