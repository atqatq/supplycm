"""Hamiltonian path via backtracking."""
from typing import Dict, List, Optional


def hamiltonian_path_backtrack(adjacency: Dict[int, List[int]]) -> Optional[List[int]]:
    """Find a Hamiltonian path using DFS with backtracking.

    Example:
        >>> hamiltonian_path_backtrack({0: [1], 1: [0, 2], 2: [1]})
        [0, 1, 2]
    """
    nodes = list(adjacency.keys())
    n = len(nodes)
    if n == 0:
        return []
    def backtrack(path, visited):
        if len(path) == n:
            return path[:]
        last = path[-1]
        for nxt in adjacency.get(last, []):
            if nxt not in visited:
                visited.add(nxt)
                path.append(nxt)
                result = backtrack(path, visited)
                if result:
                    return result
                path.pop()
                visited.discard(nxt)
        return None
    for start in nodes:
        result = backtrack([start], {start})
        if result:
            return result
    return None
