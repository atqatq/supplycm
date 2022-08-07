"""Earliest start schedule from precedence graph."""
from typing import List


def earliest_start_schedule(durations: List[float],
                             predecessors: List[List[int]]) -> List[float]:
    """Compute earliest start time per activity.

    Example:
        >>> ess = earliest_start_schedule([3, 5, 2, 4], [[], [0], [0], [1, 2]])
        >>> ess[3] == 8
        True
    """
    n = len(durations)
    es = [0.0] * n
    # Topological order
    in_degree = [len(p) for p in predecessors]
    queue = [i for i in range(n) if in_degree[i] == 0]
    while queue:
        i = queue.pop(0)
        for j in range(n):
            if i in predecessors[j]:
                es[j] = max(es[j], es[i] + durations[i])
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
    return es
