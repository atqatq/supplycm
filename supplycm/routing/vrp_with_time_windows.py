"""VRPTW greedy insertion heuristic."""
from typing import List, Tuple


def vrp_with_time_windows(distances: List[List[float]], demands: List[float],
                          time_windows: List[Tuple[float, float]],
                          service_times: List[float],
                          vehicle_capacity: float,
                          speed: float = 1.0) -> List[List[int]]:
    """Greedy insertion respecting time windows.

    Args:
        distances: Distance matrix.
        demands: Demand per node.
        time_windows: (earliest, latest) per node.
        service_times: Service time per node.
        vehicle_capacity: Max load.
        speed: Travel speed (distance/speed = time).

    Example:
        >>> routes = vrp_with_time_windows(
        ...     [[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]],
        ...     [0,1,1,1], [(0,100)]*4, [0,1,1,1], 5)
        >>> len(routes) >= 1
        True
    """
    n = len(distances)
    unvisited = set(i for i in range(1, n) if demands[i] > 0)
    routes = []
    while unvisited:
        route = [0]
        load = 0
        current_time = 0
        current = 0
        while unvisited:
            best_c = None
            best_arrival = float('inf')
            for c in unvisited:
                if load + demands[c] > vehicle_capacity:
                    continue
                travel = distances[current][c] / speed
                arrival = current_time + travel
                if arrival > time_windows[c][1]:
                    continue
                # Wait if too early
                start = max(arrival, time_windows[c][0])
                if start < best_arrival:
                    best_arrival = start
                    best_c = c
            if best_c is None:
                break
            route.append(best_c)
            load += demands[best_c]
            current_time = best_arrival + service_times[best_c]
            current = best_c
            unvisited.discard(best_c)
        route.append(0)
        routes.append(route)
    return routes
