"""Ranked Positional Weight (RPW) for line balancing."""
from typing import List


def rpw_priority(task_times: List[float], successors: List[List[int]]) -> List[int]:
    """Compute RPW = task_time + sum of successor times.

    Example:
        >>> rpw = rpw_priority([2, 3, 1, 2, 1], [[1, 2], [3], [3], [4], []])
        >>> rpw[0] > rpw[4]
        True
    """
    n = len(task_times)
    rpw = [0.0] * n
    # Process in reverse topological order
    in_degree = [0] * n
    for i in range(n):
        for s in successors[i]:
            in_degree[s] += 1
    # Reverse: compute cumulative from end
    for i in range(n - 1, -1, -1):
        rpw[i] = task_times[i]
        for s in successors[i]:
            rpw[i] += rpw[s]
    return sorted(range(n), key=lambda i: -rpw[i])
