"""Greedy graph coloring."""
from typing import Dict, List


def graph_coloring_greedy(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """Color graph using first available color per node.

    Example:
        >>> gc = graph_coloring_greedy({0: [1, 2], 1: [0, 2], 2: [0, 1]})
        >>> max(gc.values()) <= 2
        True
    """
    colors = {}
    for node in sorted(graph.keys()):
        used = set()
        for neighbor in graph.get(node, []):
            if neighbor in colors:
                used.add(colors[neighbor])
        c = 0
        while c in used:
            c += 1
        colors[node] = c
    return colors
