"""Longest Processing Time first for parallel machines."""
from typing import List


def lpt_rule(processing_times: List[float], num_machines: int) -> List[List[int]]:
    """Sort jobs by LPT, then list-schedule.

    Example:
        >>> sched = lpt_rule([3, 5, 2, 4, 1], 2)
        >>> len(sched[0]) + len(sched[1]) == 5
        True
    """
    order = sorted(range(len(processing_times)), key=lambda i: -processing_times[i])
    machine_loads = [0.0] * num_machines
    machine_jobs = [[] for _ in range(num_machines)]
    for j in order:
        m = min(range(num_machines), key=lambda x: machine_loads[x])
        machine_jobs[m].append(j)
        machine_loads[m] += processing_times[j]
    return machine_jobs
