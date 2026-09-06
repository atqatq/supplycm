"""Capacity Requirements Planning (CRP)."""
from typing import Dict, List, Tuple


def capacity_requirements_planning(planned_orders: Dict[int, List[float]],
                                    routing: Dict[int, List[Tuple[int, float]]],
                                    capacities: List[float]) -> Dict[int, List[float]]:
    """Compute capacity needed per work center per period.

    Args:
        planned_orders: Item -> planned order quantities per period.
        routing: Item -> list of (work_center, time_per_unit).
        capacities: Capacity per work center per period.

    Returns:
        Dict work_center -> load per period.

    Example:
        >>> crp = capacity_requirements_planning({'A': [10, 20]},
        ...     {'A': [(0, 0.5)]}, [100, 100])
        >>> crp[0][1] == 10.0
        True
    """
    num_periods = len(capacities) // max(1, len(set(wc for r in routing.values() for wc, _ in r)))
    # Simplified: assume single work center per period
    result = {}
    for item, orders in planned_orders.items():
        for wc, time_per in routing.get(item, []):
            if wc not in result:
                result[wc] = [0.0] * len(orders)
            for t, qty in enumerate(orders):
                result[wc][t] += qty * time_per
    return result


from typing import List, Dict, Tuple
