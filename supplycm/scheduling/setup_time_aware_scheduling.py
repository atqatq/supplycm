"""Sequence-dependent setup time scheduling."""
from typing import List, Sequence


def setup_time_aware_scheduling(processing_times: List[float],
                                 setup_matrix: List[List[float]]) -> List[int]:
    """Greedy nearest-neighbor considering setup times.

    Example:
        >>> seq = setup_time_aware_scheduling([5, 3, 8],
        ...     [[0, 2, 5], [3, 0, 1], [4, 2, 0]])
        >>> len(seq) == 3
        True
    """
    n = len(processing_times)
    sequence = [0]
    unvisited = set(range(1, n))
    while unvisited:
        current = sequence[-1]
        next_job = min(unvisited, key=lambda j: setup_matrix[current][j])
        sequence.append(next_job)
        unvisited.discard(next_job)
    return sequence
