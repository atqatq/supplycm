"""Dijkstra's shortest path algorithm."""
from typing import Dict, List, Optional, Tuple
import heapq


def dijkstra_shortest_path(graph: Dict[int, List[Tuple[int, float]]],
                           source: int, target: int = None) -> Tuple[Dict[int, float], Dict[int, int]]:
    """Dijkstra's algorithm.

    Args:
        graph: Adjacency dict mapping node -> list of (neighbor, weight).
        source: Source node.
        target: Optional target node.

    Returns:
        Tuple (distances, predecessors).

    Example:
        >>> g = {0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}
        >>> d, p = dijkstra_shortest_path(g, 0)
        >>> d[2]
        3.0
    """
    dist = {source: 0.0}
    prev = {}
    pq = [(0.0, source)]
    visited = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if target is not None and u == target:
            break
        for v, w in graph.get(u, []):
            new_d = d + w
            if v not in dist or new_d < dist[v]:
                dist[v] = new_d
                prev[v] = u
                heapq.heappush(pq, (new_d, v))
    return dist, prev
