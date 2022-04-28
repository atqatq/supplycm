"""Critical Path Method (CPM) for project scheduling."""
from typing import List


def critical_path_method(durations: List[float],
                         successors: List[List[int]]) -> List[int]:
    """Find the critical path in a project network.

    Args:
        durations: Activity durations (activity 0 = start, last = finish).
        successors: List of successor indices per activity.

    Returns:
        List of activity indices on the critical path.

    Example:
        >>> cpm = critical_path_method([0, 3, 5, 2, 0], [[1, 2], [3], [3], [4], []])
        >>> 0 in cpm and 4 in cpm
        True
    """
    n = len(durations)
    # Forward pass
    es = [0.0] * n
    for i in range(n):
        for s in successors[i]:
            es[s] = max(es[s], es[i] + durations[i])
    # Backward pass
    ef = [es[-1] + durations[-1]] * n
    for i in range(n - 1, -1, -1):
        for s in successors[i]:
            ef[i] = min(ef[i], ef[s] - durations[i])
    # Critical path: activities where es == ef - durations
    critical = [i for i in range(n) if es[i] == ef[i] - durations[i]]
    return critical
