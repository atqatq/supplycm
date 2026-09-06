"""Bron-Kerbosch maximal cliques."""
from typing import Dict, List, Set


def maximal_clique_bron_kerbosch(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Find all maximal cliques in undirected graph.

    Example:
        >>> cliques = maximal_clique_bron_kerbosch({0: [1, 2], 1: [0, 2], 2: [0, 1]})
        >>> any(set([0, 1, 2]) == set(c) for c in cliques)
        True
    """
    cliques = []
    def bk(r: Set, p: Set, x: Set):
        if not p and not x:
            cliques.append(sorted(r))
            return
        for v in list(p):
            neighbors = set(graph.get(v, []))
            bk(r | {v}, p & neighbors, x & neighbors)
            p = p - {v}
            x = x | {v}
    bk(set(), set(graph.keys()), set())
    return cliques
