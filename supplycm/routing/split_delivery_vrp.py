"""Split delivery VRP greedy heuristic."""
from typing import List, Tuple


def split_delivery_vrp(distances: List[List[float]], demands: List[float],
                       vehicle_capacity: float) -> List[Tuple[List[int], List[float]]]:
    """Allow demand splitting across vehicles.

    Returns:
        List of (route, deliveries) tuples.

    Example:
        >>> routes = split_delivery_vrp([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]],
        ...                              [0, 5, 5, 5], 4)
        >>> sum(sum(d) for _, d in routes) == 15
        True
    """
    n = len(distances)
    remaining = list(demands)
    routes = []
    while sum(remaining[1:]) > 0:
        route = [0]
        deliveries = [0.0] * n
        load = 0
        current = 0
        while load < vehicle_capacity:
            # Find nearest customer with remaining demand
            best_c = -1
            best_dist = float('inf')
            for c in range(1, n):
                if remaining[c] > 0 and distances[current][c] < best_dist:
                    best_dist = distances[current][c]
                    best_c = c
            if best_c < 0:
                break
            deliver = min(remaining[best_c], vehicle_capacity - load)
            deliveries[best_c] = deliver
            remaining[best_c] -= deliver
            load += deliver
            route.append(best_c)
            current = best_c
        route.append(0)
        routes.append((route, deliveries))
    return routes
