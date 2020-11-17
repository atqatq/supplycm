"""Topological sort via Kahn's algorithm."""
from typing import Dict, List
from collections import deque


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    """Kahn's topological sort.

    Example:
        >>> topological_sort({0: [1, 2], 1: [3], 2: [3], 3: []})
        [0, 1, 2, 3]
    """
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
    q = deque([u for u in in_degree if in_degree[u] == 0])
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    return result
