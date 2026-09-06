"""TSP Nearest Neighbor heuristic."""
from typing import List, Tuple
import math


def tsp_nearest_neighbor(distances: List[List[float]], start: int = 0) -> Tuple[List[int], float]:
    """Solve TSP via nearest-neighbor heuristic.

    Args:
        distances: NxN distance matrix.
        start: Starting city index.

    Returns:
        Tuple (route, total_distance).

    Example:
        >>> route, dist = tsp_nearest_neighbor([[0,1,2],[1,0,3],[2,3,0]])
        >>> len(route) == 4
        True
    """
    n = len(distances)
    if n == 0:
        return [], 0.0
    visited = [False] * n
    route = [start]
    visited[start] = True
    total = 0.0
    current = start
    for _ in range(n - 1):
        nearest = -1
        nearest_dist = float('inf')
        for j in range(n):
            if not visited[j] and distances[current][j] < nearest_dist:
                nearest_dist = distances[current][j]
                nearest = j
        route.append(nearest)
        visited[nearest] = True
        total += nearest_dist
        current = nearest
    total += distances[current][start]
    route.append(start)
    return route, total
