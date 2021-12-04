"""MultiFit algorithm for parallel machine scheduling."""
from typing import List


def multifit_algorithm(processing_times: List[float], num_machines: int,
                       iterations: int = 10) -> List[List[int]]:
    """MultiFit uses binary search on bin capacity.

    Example:
        >>> sched = multifit_algorithm([3, 5, 2, 4, 1], 2)
        >>> sum(len(s) for s in sched) == 5
        True
    """
    sorted_jobs = sorted(range(len(processing_times)),
                         key=lambda i: -processing_times[i])
    def fits(capacity):
        bins = [0.0] * num_machines
        for j in sorted_jobs:
            placed = False
            for i in range(num_machines):
                if bins[i] + processing_times[j] <= capacity:
                    bins[i] += processing_times[j]
                    placed = True
                    break
            if not placed:
                return False, None
        return True, bins
    lo = max(processing_times) if processing_times else 0
    hi = sum(processing_times)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        ok, _ = fits(mid)
        if ok:
            hi = mid
        else:
            lo = mid
    # Reconstruct
    bins = [0.0] * num_machines
    assignment = [[] for _ in range(num_machines)]
    for j in sorted_jobs:
        for i in range(num_machines):
            if bins[i] + processing_times[j] <= hi:
                bins[i] += processing_times[j]
                assignment[i].append(j)
                break
    return assignment
