"""Hierholzer's algorithm for Eulerian tour."""
from typing import Dict, List, Tuple


def eulerian_tour(adjacency: Dict[int, List[int]]) -> List[int]:
    """Find Eulerian tour if one exists.

    Example:
        >>> tour = eulerian_tour({0: [1, 2], 1: [0, 2], 2: [0, 1]})
        >>> len(tour) >= 3
        True
    """
    adj_copy = {n: list(neighbors) for n, neighbors in adjacency.items()}
    start = next(iter(adj_copy))
    stack = [start]
    tour = []
    while stack:
        v = stack[-1]
        if adj_copy[v]:
            u = adj_copy[v].pop()
            adj_copy[u].remove(v)
            stack.append(u)
        else:
            tour.append(stack.pop())
    tour.reverse()
    return tour
