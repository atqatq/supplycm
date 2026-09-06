"""Bellman-Ford algorithm."""
from typing import Dict, List, Tuple


def bellman_ford(graph: Dict[int, List[Tuple[int, float]]],
                 source: int, num_nodes: int) -> Tuple[Dict[int, float], bool]:
    """Bellman-Ford: handles negative weights, detects negative cycles.

    Returns:
        Tuple (distances, has_negative_cycle).

    Example:
        >>> g = {0: [(1, 1)], 1: [(2, -1)], 2: [(0, 1)]}
        >>> d, neg = bellman_ford(g, 0, 3)
        >>> d[2] == 0
        True
    """
    dist = {i: float('inf') for i in range(num_nodes)}
    dist[source] = 0.0
    for _ in range(num_nodes - 1):
        updated = False
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break
    # Check for negative cycle
    has_neg_cycle = False
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    return dist, has_neg_cycle
