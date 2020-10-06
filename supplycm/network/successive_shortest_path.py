"""Successive Shortest Path min cost flow."""
from typing import List


def successive_shortest_path(capacity: List[List[float]],
                              costs: List[List[float]],
                              supply: List[float]) -> float:
    """Min-cost flow via successive shortest paths.

    Example:
        >>> cap = [[0, 10], [0, 0]]
        >>> cost = [[0, 3], [0, 0]]
        >>> supply = [5, -5]
        >>> successive_shortest_path(cap, cost, supply)
        15.0
    """
    n = len(capacity)
    residual = [row[:] for row in capacity]
    total_cost = 0.0
    supply = list(supply)
    while True:
        # Find a supply node
        src = -1
        for i in range(n):
            if supply[i] > 0:
                src = i
                break
        if src < 0:
            break
        # Dijkstra
        import heapq
        dist = [float('inf')] * n
        dist[src] = 0
        prev = [-1] * n
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v in range(n):
                if residual[u][v] > 0 and d + costs[u][v] < dist[v]:
                    dist[v] = d + costs[u][v]
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))
        # Find nearest demand
        sink = -1
        for j in range(n):
            if supply[j] < 0 and dist[j] < float('inf'):
                sink = j
                break
        if sink < 0:
            break
        # Bottleneck
        path_flow = min(supply[src], -supply[sink])
        v = sink
        while v != src:
            u = prev[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        v = sink
        while v != src:
            u = prev[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            total_cost += path_flow * costs[u][v]
            v = u
        supply[src] -= path_flow
        supply[sink] += path_flow
    return total_cost
