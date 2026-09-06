"""Fixed-charge facility location problem (greedy heuristic)."""
from typing import List, Tuple


def facility_location_fixed_cost(demands: List[float],
                                  distances: List[List[float]],
                                  fixed_costs: List[float],
                                  num_facilities: int) -> Tuple[List[int], float]:
    """Select facilities to minimize total cost (fixed + transport).

    Args:
        demands: Demand per customer.
        distances: Customer x Facility distance matrix.
        fixed_costs: Fixed cost per facility.
        num_facilities: Number of facilities to open.

    Returns:
        Tuple (selected_facilities, total_cost).

    Example:
        >>> facs, cost = facility_location_fixed_cost(
        ...     [10, 20, 30], [[1, 5, 3], [5, 1, 2], [3, 2, 1]], [100, 120, 80], 1)
        >>> len(facs) == 1
        True
    """
    n_customers = len(demands)
    n_facilities = len(fixed_costs)
    selected = []
    remaining = list(range(n_facilities))
    while len(selected) < num_facilities and remaining:
        best_f = None
        best_cost = float('inf')
        for f in remaining:
            trial = selected + [f]
            transport = 0
            for c in range(n_customers):
                min_dist = min(distances[c][j] for j in trial)
                transport += demands[c] * min_dist
            total = transport + sum(fixed_costs[j] for j in trial)
            if total < best_cost:
                best_cost = total
                best_f = f
        selected.append(best_f)
        remaining.remove(best_f)
    transport = sum(demands[c] * min(distances[c][j] for j in selected)
                    for c in range(n_customers))
    total_cost = transport + sum(fixed_costs[j] for j in selected)
    return selected, total_cost
