"""Clarke-Wright Savings algorithm for VRP."""
from typing import List, Tuple


def vrp_savings(distances: List[List[float]],
                demands: List[float],
                vehicle_capacity: float) -> List[List[int]]:
    """Clarke-Wright parallel savings algorithm.

    Args:
        distances: NxN distance matrix (index 0 = depot).
        demands: Demand per customer (index 0 unused or 0).
        vehicle_capacity: Max demand per vehicle.

    Returns:
        List of routes (each route = list of customer indices).

    Example:
        >>> routes = vrp_savings([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]],
        ...                      [0, 1, 1, 1], 3)
        >>> sum(len(r) for r in routes) == 3
        True
    """
    n = len(distances)
    if n < 2:
        return []
    # Initial routes: 0-i-0 for each customer
    routes = {i: [0, i, 0] for i in range(1, n) if demands[i] > 0}
    route_of = {i: i for i in range(1, n) if demands[i] > 0}
    load = {i: demands[i] for i in range(1, n) if demands[i] > 0}
    # Compute savings
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if demands[i] > 0 and demands[j] > 0:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True)
    # Merge routes
    for s, i, j in savings:
        if i not in route_of or j not in route_of:
            continue
        ri = route_of[i]
        rj = route_of[j]
        if ri == rj:
            continue
        # Check capacity
        if load[ri] + load[rj] > vehicle_capacity:
            continue
        # Try to merge at endpoints
        new_route = None
        if routes[ri][-2] == i and routes[rj][1] == j:
            new_route = routes[ri][:-1] + routes[rj][1:]
        elif routes[ri][1] == i and routes[rj][-2] == j:
            new_route = routes[rj][:-1] + routes[ri][1:]
        elif routes[ri][-2] == i and routes[rj][-2] == j:
            new_route = routes[ri][:-1] + routes[rj][1:][::-1]
        elif routes[ri][1] == i and routes[rj][1] == j:
            new_route = routes[ri][:0:-1] + routes[rj][1:]
        if new_route is None:
            continue
        # Merge
        for c in routes[rj]:
            if c != 0:
                route_of[c] = ri
        routes[ri] = new_route
        load[ri] += load[rj]
        del routes[rj]
        del load[rj]
    return [r for r in routes.values()]
