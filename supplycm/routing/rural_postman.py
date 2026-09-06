"""Rural Postman Problem (simplified)."""
from typing import Dict, List, Set, Tuple


def rural_postman(adjacency: Dict[int, List[Tuple[int, float]]],
                  required_edges: Set[Tuple[int, int]]) -> Tuple[List[int], float]:
    """Approximate Rural Postman by traversing required edges twice.

    Example:
        >>> adj = {0: [(1, 1.0)], 1: [(0, 1.0), (2, 2.0)], 2: [(1, 2.0)]}
        >>> required = {(0, 1), (1, 2)}
        >>> tour, length = rural_postman(adj, required)
        >>> length > 0
        True
    """
    total = 0.0
    edges_traversed = []
    for u, v in required_edges:
        w = None
        for neighbor, weight in adjacency.get(u, []):
            if neighbor == v:
                w = weight
                break
        if w is None:
            for neighbor, weight in adjacency.get(v, []):
                if neighbor == u:
                    w = weight
                    break
        if w is not None:
            edges_traversed.extend([(u, v), (v, u)])
            total += 2 * w
    # Return a basic tour
    nodes = list(adjacency.keys())
    return nodes, total
