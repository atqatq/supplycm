"""Degree centrality."""
from typing import Dict, List


def degree_centrality(graph: Dict[int, List[int]], num_nodes: int) -> Dict[int, float]:
    """Degree centrality = number of neighbors / (N-1).

    Example:
        >>> dc = degree_centrality({0: [1, 2], 1: [0], 2: [0]}, 3)
        >>> dc[0] == 1.0
        True
    """
    if num_nodes <= 1:
        return {n: 0.0 for n in graph}
    return {n: len(graph.get(n, [])) / (num_nodes - 1) for n in range(num_nodes)}
