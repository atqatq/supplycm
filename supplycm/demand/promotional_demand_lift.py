"""Calculate promotional lift factor."""
from typing import List, Tuple


def promotional_demand_lift(baseline_demand: float, promotion_demand: float) -> float:
    """Lift factor = promotion_demand / baseline.

    Example:
        >>> promotional_demand_lift(100, 150)
        1.5
    """
    if baseline_demand <= 0:
        raise ValueError("baseline demand must be positive")
    return promotion_demand / baseline_demand
