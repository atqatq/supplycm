"""Open shop scheduling greedy heuristic."""
from typing import List, Tuple


def open_shop_schedule(processing_times: List[List[float]]) -> List[List[Tuple[int, int]]]:
    """Schedule jobs on machines where order is flexible.

    Args:
        processing_times: Job x Machine matrix.

    Returns:
        List per machine of (job, start, end).

    Example:
        >>> sched = open_shop_schedule([[3, 5], [1, 2]])
        >>> len(sched) == 2
        True
    """
    n = len(processing_times)
    m = len(processing_times[0]) if n > 0 else 0
    job_avail = [0.0] * n
    machine_avail = [0.0] * m
    machine_schedule = [[] for _ in range(m)]
    remaining = {(j, k): processing_times[j][k] for j in range(n) for k in range(m)}
    while remaining:
        # Pick operation with earliest possible start
        best = None
        best_start = float('inf')
        for (j, k), p in remaining.items():
            start = max(job_avail[j], machine_avail[k])
            if start < best_start:
                best_start = start
                best = (j, k, p)
        j, k, p = best
        start = best_start
        end = start + p
        machine_schedule[k].append((j, start, end))
        job_avail[j] = end
        machine_avail[k] = end
        del remaining[(j, k)]
    return machine_schedule


from typing import List, Tuple
