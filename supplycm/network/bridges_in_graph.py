"""Find bridges in graph."""
from typing import Dict, List, Set, Tuple


def bridges_in_graph(graph: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    """Find bridge edges.

    Example:
        >>> bridges_in_graph({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]})
        [(0, 1), (2, 3)]
    """
    visited = set()
    disc = {}
    low = {}
    timer = [0]
    bridges = []
    def dfs(u, parent):
        visited.add(u)
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent:
                low[u] = min(low[u], disc[v])
    for node in graph:
        if node not in visited:
            dfs(node, None)
    return bridges
