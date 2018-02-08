"""Allocate joint ordering cost across items."""
from typing import List


def ordering_cost_allocation(item_costs: List[float], total_ordering_cost: float) -> List[float]:
    """Allocate by item value share.

    Example:
        >>> ordering_cost_allocation([100, 200, 300], 60)
        [10.0, 20.0, 30.0]
    """
    total = sum(item_costs)
    if total == 0:
        raise ValueError("total item cost cannot be zero")
    return [c / total * total_ordering_cost for c in item_costs]
