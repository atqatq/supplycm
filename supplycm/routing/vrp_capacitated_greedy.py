"""Capacitated VRP greedy heuristic."""
from typing import List, Tuple
import math


def vrp_capacitated_greedy(distances: List[List[float]], demands: List[float],
                            vehicle_capacity: float) -> List[List[int]]:
    """Greedy VRP: assign nearest feasible customer until capacity is exhausted.

    Example:
        >>> routes = vrp_capacitated_greedy([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]],
        ...                                   [0, 1, 1, 1], 2)
        >>> len(routes) >= 1
        True
    """
    n = len(distances)
    unvisited = set(i for i in range(1, n) if demands[i] > 0)
    routes = []
    while unvisited:
        route = [0]
        load = 0
        current = 0
        while unvisited:
            # Find nearest feasible
            feasible = [c for c in unvisited if load + demands[c] <= vehicle_capacity]
            if not feasible:
                break
            next_c = min(feasible, key=lambda c: distances[current][c])
            route.append(next_c)
            load += demands[next_c]
            unvisited.discard(next_c)
            current = next_c
        route.append(0)
        routes.append(route)
    return routes
