"""Scheduling with learning effect."""
from typing import List


def learning_curve_scheduling(processing_times: List[float], learning_rate: float = 0.9) -> List[int]:
    """Order jobs to minimize total completion time with learning effect.

    Example:
        >>> seq = learning_curve_scheduling([5, 3, 8, 2], 0.9)
        >>> len(seq) == 4
        True
    """
    # Sort by SPT (proven optimal for learning effect)
    return sorted(range(len(processing_times)), key=lambda i: processing_times[i])
