"""Master Production Schedule (MPS) generation."""
from typing import List


def master_production_schedule(forecast: List[float], actual_orders: List[float],
                                on_hand: float, lot_size: int,
                                planning_horizon: int) -> List[float]:
    """Generate MPS quantities per period.

    Example:
        >>> mps = master_production_schedule([10, 20, 30, 40], [5, 10, 15, 20],
        ...                                   10, 50, 4)
        >>> len(mps) == 4
        True
    """
    n = min(planning_horizon, len(forecast))
    production = [0.0] * n
    inventory = on_hand
    for t in range(n):
        # Use max of forecast and actual orders (consumes forecast)
        demand = max(forecast[t], actual_orders[t])
        if inventory < demand:
            needed = demand - inventory
            lots = -(-needed // lot_size) if lot_size > 0 else 1
            production[t] = lots * lot_size if lot_size > 0 else needed
            inventory += production[t]
        inventory -= demand
    return production
