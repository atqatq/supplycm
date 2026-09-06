"""Edmonds-Karp max flow (BFS)."""
from typing import List
from collections import deque


def edmonds_karp_max_flow(capacity: List[List[float]], source: int, sink: int) -> float:
    """Max flow using BFS.

    Example:
        >>> cap = [[0, 3, 0, 2], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        >>> round(edmonds_karp_max_flow(cap, 0, 3), 4)
        4.0
    """
    n = len(capacity)
    residual = [row[:] for row in capacity]
    max_flow = 0.0
    while True:
        parent = [-1] * n
        parent[source] = source
        flow = [0.0] * n
        flow[source] = float('inf')
        q = deque([source])
        while q:
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    flow[v] = min(flow[u], residual[u][v])
                    if v == sink:
                        break
                    q.append(v)
            if parent[sink] != -1:
                break
        if parent[sink] == -1:
            break
        max_flow += flow[sink]
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= flow[sink]
            residual[v][u] += flow[sink]
            v = u
    return max_flow
