"""Kruskal's MST algorithm."""
from typing import List, Tuple


def kruskal_mst(num_nodes: int, edges: List[Tuple[int, int, float]]) -> Tuple[List[Tuple[int, int, float]], float]:
    """Compute MST using Kruskal's algorithm with union-find.

    Args:
        num_nodes: Number of nodes.
        edges: List of (u, v, weight).

    Returns:
        Tuple (mst_edges, total_weight).

    Example:
        >>> mst, w = kruskal_mst(4, [(0,1,1),(1,2,2),(2,3,3),(0,3,4),(1,3,5)])
        >>> w
        6
    """
    parent = list(range(num_nodes))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst = []
    total = 0.0
    for u, v, w in sorted_edges:
        if union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == num_nodes - 1:
                break
    return mst, total
