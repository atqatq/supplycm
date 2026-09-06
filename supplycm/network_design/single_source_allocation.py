"""Assign each customer to exactly one facility (single sourcing)."""
from typing import List, Tuple


def single_source_allocation(demands: List[float],
                              distances: List[List[float]],
                              capacities: List[float]) -> List[int]:
    """Assign customers to nearest facility respecting capacity.

    Args:
        demands: Demand per customer.
        distances: Customer x Facility distance matrix.
        capacities: Capacity per facility.

    Returns:
        List of facility index per customer.

    Example:
        >>> alloc = single_source_allocation([5, 10, 8],
        ...     [[1, 5], [5, 1], [3, 2]], [15, 10])
        >>> len(alloc) == 3
        True
    """
    n_customers = len(demands)
    n_facilities = len(capacities)
    remaining_cap = list(capacities)
    assignment = [-1] * n_customers
    # Sort customers by demand descending (greedy)
    order = sorted(range(n_customers), key=lambda c: -demands[c])
    for c in order:
        # Find nearest feasible facility
        best_f = None
        best_dist = float('inf')
        for f in range(n_facilities):
            if remaining_cap[f] >= demands[c] and distances[c][f] < best_dist:
                best_dist = distances[c][f]
                best_f = f
        if best_f is None:
            raise ValueError('no feasible facility for customer ' + str(c))
        assignment[c] = best_f
        remaining_cap[best_f] -= demands[c]
    return assignment
