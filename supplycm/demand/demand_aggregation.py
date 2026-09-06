"""Aggregate demand by time bucket."""
from typing import List


def demand_aggregation(daily_demand: List[float], bucket_size: int) -> List[float]:
    """Aggregate daily demand into larger buckets.

    Example:
        >>> demand_aggregation([10, 20, 30, 40, 50, 60], 3)
        [60.0, 150.0]
    """
    if bucket_size <= 0:
        raise ValueError("bucket_size must be positive")
    result = []
    for i in range(0, len(daily_demand), bucket_size):
        result.append(sum(daily_demand[i:i + bucket_size]))
    return result
