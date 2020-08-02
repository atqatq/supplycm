"""All-pairs shortest paths via repeated Dijkstra."""
from typing import Dict, List, Tuple


def all_pairs_shortest_path(graph: Dict[int, List[Tuple[int, float]]],
                            nodes: List[int]) -> Dict[int, Dict[int, float]]:
    """Compute shortest distances between all pairs.

    Example:
        >>> g = {0: [(1, 1)], 1: [(2, 2)], 2: []}
        >>> apsp = all_pairs_shortest_path(g, [0, 1, 2])
        >>> apsp[0][2]
        3.0
    """
    import heapq
    result = {}
    for src in nodes:
        dist = {src: 0.0}
        pq = [(0.0, src)]
        visited = set()
        while pq:
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            for v, w in graph.get(u, []):
                nd = d + w
                if v not in dist or nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        result[src] = {n: dist.get(n, float('inf')) for n in nodes}
    return result
