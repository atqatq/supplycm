"""Apply demand time fence to MRP."""
from typing import List


def demand_time_fence(gross_requirements: List[float], actual_orders: List[float],
                      fence_period: int) -> List[float]:
    """Within fence use actual orders; outside use forecast.

    Example:
        >>> dtf = demand_time_fence([100, 100, 100, 100], [50, 60, 0, 0], 2)
        >>> dtf[0] == 50 and dtf[2] == 100
        True
    """
    return [actual_orders[t] if t < fence_period else gross_requirements[t]
            for t in range(len(gross_requirements))]
