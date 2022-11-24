"""Rough-Cut Capacity Planning (RCCP)."""
from typing import List


def rough_cut_capacity_planning(production_plan: List[float],
                                 resource_utilization: List[List[float]],
                                 capacities: List[float]) -> List[float]:
    """Check capacity utilization per resource per period.

    Args:
        production_plan: Production quantity per period.
        resource_utilization: Resource x Period matrix of per-unit resource needs.
        capacities: Capacity per resource per period.

    Returns:
        List of utilization ratios per resource.

    Example:
        >>> rccp = rough_cut_capacity_planning([100, 200], [[0.5, 0.3]], [80, 80])
        >>> round(rccp[0], 2) > 0
        True
    """
    num_resources = len(resource_utilization)
    utilization = [0.0] * num_resources
    for r in range(num_resources):
        total_used = 0.0
        total_cap = 0.0
        for t in range(len(production_plan)):
            used = production_plan[t] * resource_utilization[r][t]
            total_used += used
            total_cap += capacities[t]
        utilization[r] = total_used / total_cap if total_cap > 0 else 0
    return utilization
