"""Eigenvector centrality via power iteration."""
from typing import Dict, List


def eigenvector_centrality(graph: Dict[int, List[int]], nodes: List[int],
                            iterations: int = 100, tol: float = 1e-6) -> Dict[int, float]:
    """Power iteration to compute eigenvector centrality.

    Example:
        >>> g = {0: [1, 2], 1: [0], 2: [0]}
        >>> ec = eigenvector_centrality(g, [0, 1, 2])
        >>> ec[0] > ec[1]
        True
    """
    ec = {n: 1.0 for n in nodes}
    for _ in range(iterations):
        new_ec = {n: 0.0 for n in nodes}
        for u in graph:
            for v in graph[u]:
                new_ec[v] += ec[u]
        # Normalize
        norm = sum(v * v for v in new_ec.values()) ** 0.5
        if norm == 0:
            break
        new_ec = {n: v / norm for n, v in new_ec.items()}
        diff = sum(abs(new_ec[n] - ec[n]) for n in nodes)
        ec = new_ec
        if diff < tol:
            break
    return ec
