"""Sum of completion times for a sequence."""
from typing import List


def total_completion_time(sequence: List[int], processing_times: List[float]) -> float:
    """Sum of completion times.

    Example:
        >>> total_completion_time([0, 1, 2], [3, 2, 4])
        16.0
    """
    time = 0
    total = 0.0
    for j in sequence:
        time += processing_times[j]
        total += time
    return total
