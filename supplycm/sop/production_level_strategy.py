"""Level production strategy."""
from typing import List


def production_level_strategy(demand: List[float], initial_inventory: float = 0,
                               safety_stock: float = 0) -> List[float]:
    """Constant production rate to meet total demand.

    Example:
        >>> production_level_strategy([90, 120, 150])
        [120.0, 120.0, 120.0]
    """
    total_demand = sum(demand)
    n = len(demand)
    rate = (total_demand + safety_stock - initial_inventory) / n
    return [rate] * n
