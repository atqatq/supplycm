"""Compute total tardiness for a sequence."""
from typing import List


def tardiness_calculation(sequence: List[int], processing_times: List[float],
                          due_dates: List[float]) -> float:
    """Sum of max(0, completion - due_date).

    Example:
        >>> tardiness_calculation([0, 1, 2], [3, 2, 4], [5, 10, 12])
        2.0
    """
    time = 0
    total = 0.0
    for j in sequence:
        time += processing_times[j]
        if time > due_dates[j]:
            total += time - due_dates[j]
    return total
