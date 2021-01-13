"""Articulation points via Tarjan."""
from typing import Dict, List, Set


def articulation_points(graph: Dict[int, List[int]]) -> Set[int]:
    """Find articulation points.

    Example:
        >>> articulation_points({0: [1], 1: [0, 2], 2: [1]})
        {1}
    """
    visited = set()
    disc = {}
    low = {}
    parent = {}
    ap = set()
    timer = [0]
    def dfs(u):
        children = 0
        visited.add(u)
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent.get(u) is None and children > 1:
                    ap.add(u)
                if parent.get(u) is not None and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])
    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)
    return ap
