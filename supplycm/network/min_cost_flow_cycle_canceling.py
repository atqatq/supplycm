"""Min-cost flow via cycle-canceling (simplified)."""
from typing import List, Tuple


def min_cost_flow_cycle_canceling(capacity: List[List[float]],
                                  costs: List[List[float]],
                                  supply: List[float]) -> float:
    """Simplified min-cost flow solver.

    Args:
        capacity: Capacity matrix.
        costs: Per-unit cost matrix.
        supply: Supply (>0) or demand (<0) per node.

    Returns:
        Total cost.

    Example:
        >>> cap = [[0, 10], [0, 0]]
        >>> cost = [[0, 5], [0, 0]]
        >>> supply = [5, -5]
        >>> min_cost_flow_cycle_canceling(cap, cost, supply) == 25
        True
    """
    n = len(capacity)
    flow = [[0.0] * n for _ in range(n)]
    residual = [row[:] for row in capacity]
    total_cost = 0.0
    # Push flow greedily from supply to demand
    for i in range(n):
        while supply[i] > 0:
            # Find shortest path from i to any demand node using Bellman-Ford
            dist = [float('inf')] * n
            dist[i] = 0
            prev = [-1] * n
            for _ in range(n - 1):
                for u in range(n):
                    for v in range(n):
                        if residual[u][v] > 0 and dist[u] + costs[u][v] < dist[v]:
                            dist[v] = dist[u] + costs[u][v]
                            prev[v] = u
            # Find a demand node
            target = -1
            for j in range(n):
                if supply[j] < 0 and dist[j] < float('inf'):
                    target = j
                    break
            if target < 0:
                break
            # Bottleneck
            path_flow = min(supply[i], -supply[target], float('inf'))
            v = target
            while v != i:
                u = prev[v]
                path_flow = min(path_flow, residual[u][v])
                v = u
            v = target
            while v != i:
                u = prev[v]
                flow[u][v] += path_flow
                residual[u][v] -= path_flow
                residual[v][u] += path_flow
                total_cost += path_flow * costs[u][v]
                v = u
            supply[i] -= path_flow
            supply[target] += path_flow
    return total_cost
