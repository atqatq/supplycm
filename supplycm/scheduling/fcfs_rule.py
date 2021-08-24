"""First Come First Served scheduling."""
from typing import List


def fcfs_rule(arrival_times: List[float]) -> List[int]:
    """Order by arrival time.

    Example:
        >>> fcfs_rule([3, 1, 2])
        [1, 2, 0]
    """
    return sorted(range(len(arrival_times)), key=lambda i: arrival_times[i])
