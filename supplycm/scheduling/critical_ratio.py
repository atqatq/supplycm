"""Critical Ratio dispatching rule."""
from typing import List


def critical_ratio(processing_times: List[float], due_dates: List[float],
                   current_time: float = 0) -> List[int]:
    """Order by CR = (due_date - now) / processing_time ascending.

    Example:
        >>> critical_ratio([5, 10, 2], [10, 30, 5])
        [2, 0, 1]
    """
    def cr(i):
        remaining = due_dates[i] - current_time
        return remaining / processing_times[i] if processing_times[i] > 0 else float('inf')
    return sorted(range(len(processing_times)), key=cr)
