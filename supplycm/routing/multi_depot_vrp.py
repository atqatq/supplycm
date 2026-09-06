"""Multi-depot VRP heuristic."""
from typing import List, Tuple
import math


def multi_depot_vrp(customers: List[Tuple[float, float, float]],
                    depots: List[Tuple[float, float]],
                    vehicle_capacity: float) -> List[List[int]]:
    """Assign customers to nearest depot, then run greedy VRP per depot.

    Args:
        customers: List of (x, y, demand).
        depots: List of depot (x, y) coordinates.

    Returns:
        List of routes (each route prefixed with depot index as negative).

    Example:
        >>> routes = multi_depot_vrp([(1,1,1),(2,2,1),(-1,-1,1),(-2,-2,1)],
        ...                          [(0,0),(0,0)], 5)
        >>> len(routes) >= 1
        True
    """
    if not customers or not depots:
        return []
    # Assign each customer to nearest depot
    depot_assignments = [[] for _ in depots]
    for i, (cx, cy, _) in enumerate(customers):
        best_d = float('inf')
        best_dep = 0
        for d_idx, (dx, dy) in enumerate(depots):
            d = math.hypot(cx - dx, cy - dy)
            if d < best_d:
                best_d = d
                best_dep = d_idx
        depot_assignments[best_dep].append(i)
    # Solve VRP per depot
    routes = []
    for d_idx, cluster in enumerate(depot_assignments):
        if not cluster:
            continue
        unvisited = set(cluster)
        load = 0
        route = [-(d_idx + 1)]  # negative depot index marker
        dx, dy = depots[d_idx]
        current = (dx, dy)
        while unvisited:
            feasible = [c for c in unvisited if load + customers[c][2] <= vehicle_capacity]
            if not feasible:
                routes.append(route)
                route = [-(d_idx + 1)]
                load = 0
                current = (dx, dy)
                continue
            next_c = min(feasible, key=lambda c: math.hypot(
                customers[c][0] - current[0], customers[c][1] - current[1]))
            route.append(next_c)
            load += customers[next_c][2]
            unvisited.discard(next_c)
            current = (customers[next_c][0], customers[next_c][1])
        routes.append(route)
    return routes
