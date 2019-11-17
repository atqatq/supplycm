"""Cluster-first route-second VRP heuristic."""
from typing import List, Tuple
import math


def vrp_cluster_first_route_second(customers: List[Tuple[float, float, float]],
                                    depot: Tuple[float, float],
                                    vehicle_capacity: float,
                                    k: int = None) -> List[List[int]]:
    """K-means style clustering then TSP per cluster.

    Example:
        >>> routes = vrp_cluster_first_route_second(
        ...     [(1,0,1),(0,1,1),(-1,0,1),(0,-1,1)], (0,0), 2, k=2)
        >>> len(routes) == 2
        True
    """
    n = len(customers)
    if n == 0:
        return []
    # Simplified clustering: assign by angle to k sectors
    if k is None:
        k = max(1, math.ceil(sum(c[2] for c in customers) / vehicle_capacity))
    angles = []
    for i, (x, y, _) in enumerate(customers):
        angles.append((math.atan2(y - depot[1], x - depot[0]), i))
    angles.sort()
    clusters = [[] for _ in range(k)]
    for idx, (a, i) in enumerate(angles):
        clusters[idx % k].append(i)
    # Route within each cluster using nearest neighbor
    routes = []
    for cluster in clusters:
        if not cluster:
            continue
        # Nearest neighbor from depot
        unvisited = set(cluster)
        route = [0]
        current = 0
        while unvisited:
            next_c = min(unvisited, key=lambda c: math.hypot(
                customers[c][0] - (depot[0] if current == 0 else customers[current][0]),
                customers[c][1] - (depot[1] if current == 0 else customers[current][1])))
            route.append(next_c)
            unvisited.discard(next_c)
            current = next_c
        route.append(0)
        routes.append(route)
    return routes
