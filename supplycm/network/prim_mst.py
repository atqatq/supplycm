"""Prim's MST algorithm."""
from typing import Dict, List, Tuple
import heapq


def prim_mst(graph: Dict[int, List[Tuple[int, float]]],
             start: int = 0) -> Tuple[List[Tuple[int, int, float]], float]:
    """Compute MST via Prim's algorithm.

    Example:
        >>> g = {0: [(1, 1), (2, 4)], 1: [(0, 1), (2, 2)], 2: [(0, 4), (1, 2)]}
        >>> mst, w = prim_mst(g, 0)
        >>> w == 3
        True
    """
    in_tree = {start}
    edges = [(w, start, v) for v, w in graph.get(start, [])]
    heapq.heapify(edges)
    mst = []
    total = 0.0
    while edges and len(in_tree) < len(graph):
        w, u, v = heapq.heappop(edges)
        if v in in_tree:
            continue
        in_tree.add(v)
        mst.append((u, v, w))
        total += w
        for nxt, w2 in graph.get(v, []):
            if nxt not in in_tree:
                heapq.heappush(edges, (w2, v, nxt))
    return mst, total
