"""Compute makespan for parallel machine assignment."""
from typing import List


def parallel_machine_cmax(assignment: List[List[int]],
                          processing_times: List[float]) -> float:
    """Compute max load across machines.

    Example:
        >>> parallel_machine_cmax([[0, 2], [1, 3]], [3, 5, 2, 4])
        9.0
    """
    if not assignment:
        return 0.0
    loads = [sum(processing_times[j] for j in machine) for machine in assignment]
    return max(loads)
