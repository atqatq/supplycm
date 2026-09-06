"""Total weighted tardiness."""
from typing import List


def total_weighted_tardiness(sequence: List[int], processing_times: List[float],
                              due_dates: List[float], weights: List[float]) -> float:
    """Sum of weight * max(0, completion - due_date).

    Example:
        >>> total_weighted_tardiness([0, 1, 2], [3, 2, 4], [5, 10, 12], [1, 2, 3])
        6.0
    """
    time = 0
    total = 0.0
    for j in sequence:
        time += processing_times[j]
        if time > due_dates[j]:
            total += weights[j] * (time - due_dates[j])
    return total
