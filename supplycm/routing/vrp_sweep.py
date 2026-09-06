"""VRP Sweep algorithm."""
from typing import List, Tuple
import math


def vrp_sweep(customers: List[Tuple[float, float, float]],  # (x, y, demand)
              depot: Tuple[float, float],
              vehicle_capacity: float) -> List[List[int]]:
    """Cluster customers by sweeping polar angle from depot.

    Args:
        customers: List of (x, y, demand).
        depot: (x, y) depot location.
        vehicle_capacity: Max demand per vehicle.

    Returns:
        List of routes (each route is a list of customer indices, depot at start/end).

    Example:
        >>> routes = vrp_sweep([(1,0,1),(0,1,1),(-1,0,1),(0,-1,1)], (0,0), 2)
        >>> sum(len(r) for r in routes) >= 4
        True
    """
    n = len(customers)
    if n == 0:
        return []
    # Compute angles
    angles = []
    for i, (x, y, _) in enumerate(customers):
        angle = math.atan2(y - depot[1], x - depot[0])
        angles.append((angle, i))
    angles.sort()
    # Sweep and assign to vehicles
    routes = []
    current_route = []
    current_load = 0
    for _, i in angles:
        demand = customers[i][2]
        if current_load + demand > vehicle_capacity and current_route:
            routes.append(current_route)
            current_route = []
            current_load = 0
        current_route.append(i)
        current_load += demand
    if current_route:
        routes.append(current_route)
    return routes
