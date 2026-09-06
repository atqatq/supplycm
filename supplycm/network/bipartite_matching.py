"""Maximum bipartite matching via augmenting paths."""
from typing import Dict, List, Set


def bipartite_matching(graph: Dict[int, List[int]], left_nodes: List[int]) -> Dict[int, int]:
    """Find maximum matching in bipartite graph using DFS augmenting paths.

    Example:
        >>> g = {1: [4, 5], 2: [4], 3: [5]}
        >>> m = bipartite_matching(g, [1, 2, 3])
        >>> len(m) >= 2
        True
    """
    match_l = {}
    match_r = {}
    def try_match(u, visited):
        for v in graph.get(u, []):
            if v in visited:
                continue
            visited.add(v)
            if v not in match_r or try_match(match_r[v], visited):
                match_l[u] = v
                match_r[v] = u
                return True
        return False
    for u in left_nodes:
        try_match(u, set())
    return match_l
