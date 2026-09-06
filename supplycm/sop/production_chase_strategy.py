"""Chase production strategy."""
from typing import List


def production_chase_strategy(demand: List[float], initial_inventory: float = 0,
                               safety_stock: float = 0) -> List[float]:
    """Match production to demand each period.

    Example:
        >>> production_chase_strategy([100, 120, 130])
        [100, 120, 130]
    """
    production = []
    inventory = initial_inventory
    for d in demand:
        needed = d + safety_stock - inventory
        production.append(max(0, needed))
        inventory = inventory + needed - d
    return production
