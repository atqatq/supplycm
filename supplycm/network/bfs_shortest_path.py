"""BFS shortest path on unweighted graph."""
from typing import Dict, List
from collections import deque


def bfs_shortest_path(graph: Dict[int, List[int]], source: int, target: int) -> List[int]:
    """Return shortest path from source to target.

    Example:
        >>> bfs_shortest_path({0: [1, 2], 1: [3], 2: [3], 3: []}, 0, 3)
        [0, 1, 3]
    """
    visited = {source}
    queue = deque([(source, [source])])
    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for nxt in graph.get(node, []):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return []
