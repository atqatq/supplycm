"""Pickup and Delivery Problem greedy heuristic."""
from typing import List, Tuple


def pickup_delivery_problem(distances: List[List[float]],
                            pickup_pairs: List[Tuple[int, int]]) -> List[int]:
    """Greedy: always go to nearest feasible pickup or delivery.

    Args:
        distances: Distance matrix.
        pickup_pairs: List of (pickup_node, delivery_node).

    Returns:
        Route starting and ending at depot (index 0).

    Example:
        >>> route = pickup_delivery_problem([[0,1,2,3,4],[1,0,1,2,3],[2,1,0,1,2],
        ...                                  [3,2,1,0,1],[4,3,2,1,0]],
        ...                                  [(1, 3), (2, 4)])
        >>> route[0] == 0 and route[-1] == 0
        True
    """
    n = len(distances)
    visited = set()
    pending_pickups = set()
    pending_deliveries = {}
    for p, d in pickup_pairs:
        pending_pickups.add(p)
        pending_deliveries[p] = d
    route = [0]
    current = 0
    carried = set()  # pickups we've done, awaiting delivery
    while pending_pickups or carried:
        candidates = []
        for p in pending_pickups:
            candidates.append((distances[current][p], p, 'pickup'))
        for p in carried:
            d = pending_deliveries[p]
            candidates.append((distances[current][d], d, 'delivery'))
        if not candidates:
            break
        candidates.sort()
        next_dist, next_node, action = candidates[0]
        route.append(next_node)
        visited.add(next_node)
        if action == 'pickup':
            pending_pickups.discard(next_node)
            carried.add(next_node)
        else:
            # Find which pickup this delivery belongs to
            for p in list(carried):
                if pending_deliveries[p] == next_node:
                    carried.discard(p)
                    break
        current = next_node
    route.append(0)
    return route
