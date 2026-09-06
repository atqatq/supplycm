"""Least Slack (LS) dispatching rule."""
from typing import List


def least_slack(processing_times: List[float], due_dates: List[float],
                current_time: float = 0) -> List[int]:
    """Slack = due_date - now - processing_time. Order ascending.

    Example:
        >>> least_slack([5, 10, 2], [10, 30, 5])
        [2, 0, 1]
    """
    def slack(i):
        return due_dates[i] - current_time - processing_times[i]
    return sorted(range(len(processing_times)), key=slack)
