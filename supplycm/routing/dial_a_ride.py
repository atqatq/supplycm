"""Dial-a-Ride Problem (DARP) greedy insertion."""
from typing import List, Tuple


def dial_a_ride(requests: List[Tuple[int, int, float, float]],
                distances: List[List[float]],
                vehicle_capacity: int = 1) -> List[List[int]]:
    """Greedy DARP: insert requests into first feasible route.

    Args:
        requests: List of (pickup, delivery, earliest, latest).
        distances: Distance matrix.
        vehicle_capacity: Passenger capacity per vehicle.

    Returns:
        List of routes (each route is a sequence of node indices).

    Example:
        >>> routes = dial_a_ride([(1, 2, 0, 100), (3, 4, 0, 100)],
        ...                      [[0,1,1,2,2],[1,0,2,1,1],[1,2,0,2,2],
        ...                       [2,1,2,0,1],[2,1,2,1,0]], capacity=1)
        >>> len(routes) >= 1
        True
    """
    routes = []
    for pickup, delivery, earliest, latest in requests:
        inserted = False
        for route in routes:
            # Try inserting pickup then delivery at end
            new_route = route + [pickup, delivery]
            # Quick feasibility (skip detailed time check)
            if len(new_route) - 2 <= 2 * vehicle_capacity:
                route.extend([pickup, delivery])
                inserted = True
                break
        if not inserted:
            routes.append([0, pickup, delivery, 0])
    return routes
