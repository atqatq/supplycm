"""Ford-Fulkerson max flow."""
from typing import List


def ford_fulkerson_max_flow(capacity: List[List[float]], source: int, sink: int) -> float:
    """Compute maximum flow using Ford-Fulkerson with DFS.

    Example:
        >>> cap = [[0, 3, 0, 2], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        >>> round(ford_fulkerson_max_flow(cap, 0, 3), 4)
        4.0
    """
    n = len(capacity)
    residual = [row[:] for row in capacity]
    max_flow = 0.0
    def dfs(s, t, visited, flow):
        if s == t:
            return flow
        visited.add(s)
        for v in range(n):
            if v not in visited and residual[s][v] > 0:
                pushed = dfs(v, t, visited, min(flow, residual[s][v]))
                if pushed > 0:
                    residual[s][v] -= pushed
                    residual[v][s] += pushed
                    return pushed
        return 0
    while True:
        visited = set()
        pushed = dfs(source, sink, visited, float('inf'))
        if pushed == 0:
            break
        max_flow += pushed
    return max_flow
