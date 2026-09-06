"""Total and free slack calculation."""
from typing import List, Tuple


def slack_time_calculation(durations: List[float],
                           successors: List[List[int]]) -> List[Tuple[float, float]]:
    """Compute (total_slack, free_slack) per activity.

    Example:
        >>> slacks = slack_time_calculation([0, 3, 5, 2, 0],
        ...                                 [[1, 2], [3], [3], [4], []])
        >>> len(slacks) == 5
        True
    """
    n = len(durations)
    es = [0.0] * n
    for i in range(n):
        for s in successors[i]:
            es[s] = max(es[s], es[i] + durations[i])
    ef = [es[-1] + durations[-1]] * n
    for i in range(n - 1, -1, -1):
        for s in successors[i]:
            ef[i] = min(ef[i], ef[s] - durations[i])
    total_slack = [ef[i] - es[i] - durations[i] for i in range(n)]
    free_slack = []
    for i in range(n):
        if successors[i]:
            fs = min(es[s] - es[i] - durations[i] for s in successors[i])
        else:
            fs = ef[-1] - es[i] - durations[i]
        free_slack.append(fs)
    return list(zip(total_slack, free_slack))
