"""DFS traversal."""
from typing import Dict, List


def dfs_traversal(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Iterative DFS.

    Example:
        >>> dfs_traversal({0: [1, 2], 1: [3], 2: [], 3: []}, 0)
        [0, 2, 1, 3]
    """
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        # Push neighbors in reverse so leftmost is processed first
        for nxt in reversed(graph.get(node, [])):
            if nxt not in visited:
                stack.append(nxt)
    return result
