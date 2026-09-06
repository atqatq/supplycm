"""No-wait flow shop scheduling heuristic."""
from typing import List


def no_wait_scheduling(processing_times: List[List[float]]) -> List[int]:
    """Greedy nearest-neighbor on no-wait completion times.

    Example:
        >>> seq = no_wait_scheduling([[3, 5, 2], [1, 2, 4], [4, 1, 3]])
        >>> len(seq) == 3
        True
    """
    n = len(processing_times)
    if n == 0:
        return []
    m = len(processing_times[0])
    def wait_time(j1, j2):
        # Time between start of j1 and start of j2 so no waiting occurs
        # = sum_{k<m} max(0, sum p[j1][:k+1] - sum p[j2][:k])
        delay = 0
        for k in range(1, m):
            s1 = sum(processing_times[j1][:k + 1])
            s2 = sum(processing_times[j2][:k])
            delay = max(delay, s1 - s2)
        return delay
    sequence = [0]
    unvisited = set(range(1, n))
    while unvisited:
        current = sequence[-1]
        next_job = min(unvisited, key=lambda j: wait_time(current, j))
        sequence.append(next_job)
        unvisited.discard(next_job)
    return sequence
