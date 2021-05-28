"""Johnson's rule for 2-machine flow shop."""
from typing import List, Tuple


def johnsons_rule(jobs: List[Tuple[float, float]]) -> List[int]:
    """Schedule jobs on 2 machines to minimize makespan.

    Args:
        jobs: List of (time_on_M1, time_on_M2).

    Returns:
        Optimal job order (list of indices).

    Example:
        >>> johnsons_rule([(3, 5), (1, 2), (4, 1)])
        [1, 0, 2]
    """
    n = len(jobs)
    scheduled = []
    front = []
    back = []
    remaining = list(range(n))
    while remaining:
        # Find job with minimum processing time
        min_time = float('inf')
        min_job = -1
        min_machine = -1
        for j in remaining:
            if jobs[j][0] < min_time:
                min_time = jobs[j][0]
                min_job = j
                min_machine = 1
            if jobs[j][1] < min_time:
                min_time = jobs[j][1]
                min_job = j
                min_machine = 2
        if min_machine == 1:
            front.append(min_job)
        else:
            back.append(min_job)
        remaining.remove(min_job)
    return front + back[::-1]
