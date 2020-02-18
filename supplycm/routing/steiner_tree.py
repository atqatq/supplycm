"""Steiner tree approximation (MST of metric closure)."""
from typing import List, Set, Tuple
import math


def steiner_tree(distances: List[List[float]], terminals: Set[int]) -> Tuple[List[Tuple[int, int]], float]:
    """Approximate Steiner tree via 2-approx MST on the metric closure of terminals.

    Example:
        >>> edges, cost = steiner_tree([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]], {0, 1, 2})
        >>> cost > 0
        True
    """
    terminals = sorted(terminals)
    k = len(terminals)
    if k < 2:
        return [], 0.0
    # All-pairs shortest paths (Floyd-Warshall)
    n = len(distances)
    dist = [row[:] for row in distances]
    for kk in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][kk] + dist[kk][j] < dist[i][j]:
                    dist[i][j] = dist[i][kk] + dist[kk][j]
    # MST on terminals using distances
    in_tree = [False] * k
    in_tree[0] = True
    edges = []
    total = 0.0
    for _ in range(k - 1):
        best_w = float('inf')
        best_u = best_v = -1
        for i in range(k):
            if not in_tree[i]:
                continue
            for j in range(k):
                if not in_tree[j] and dist[terminals[i]][terminals[j]] < best_w:
                    best_w = dist[terminals[i]][terminals[j]]
                    best_u, best_v = i, j
        edges.append((terminals[best_u], terminals[best_v]))
        total += best_w
        in_tree[best_v] = True
    return edges, total
