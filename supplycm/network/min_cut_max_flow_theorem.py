"""Verify min-cut equals max-flow."""
from typing import List, Tuple
from .edmonds_karp_max_flow import edmonds_karp_max_flow


def min_cut_max_flow_theorem(capacity: List[List[float]], source: int, sink: int) -> Tuple[float, List[int]]:
    """Compute max-flow and the corresponding min-cut (reachable set in residual).

    Example:
        >>> cap = [[0, 3, 0, 2], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        >>> flow, cut = min_cut_max_flow_theorem(cap, 0, 3)
        >>> flow == 4.0
        True
    """
    n = len(capacity)
    residual = [row[:] for row in capacity]
    # Run Edmonds-Karp manually to get residual
    from collections import deque
    max_flow = 0.0
    while True:
        parent = [-1] * n
        parent[source] = source
        flow_arr = [0.0] * n
        flow_arr[source] = float('inf')
        q = deque([source])
        while q:
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    flow_arr[v] = min(flow_arr[u], residual[u][v])
                    if v == sink:
                        break
                    q.append(v)
            if parent[sink] != -1:
                break
        if parent[sink] == -1:
            break
        max_flow += flow_arr[sink]
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= flow_arr[sink]
            residual[v][u] += flow_arr[sink]
            v = u
    # Find reachable set in residual
    reachable = set()
    stack = [source]
    while stack:
        u = stack.pop()
        if u in reachable:
            continue
        reachable.add(u)
        for v in range(n):
            if residual[u][v] > 0 and v not in reachable:
                stack.append(v)
    return max_flow, sorted(reachable)
