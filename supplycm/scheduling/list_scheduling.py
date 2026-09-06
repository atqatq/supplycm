"""List scheduling for parallel machines."""
from typing import List


def list_scheduling(processing_times: List[float], num_machines: int) -> List[List[int]]:
    """Assign jobs to machines using list scheduling (greedy).

    Example:
        >>> sched = list_scheduling([3, 5, 2, 4, 1], 2)
        >>> sum(len(s) for s in sched) == 5
        True
    """
    machine_loads = [0.0] * num_machines
    machine_jobs = [[] for _ in range(num_machines)]
    for i, p in enumerate(processing_times):
        # Assign to least loaded machine
        m = min(range(num_machines), key=lambda x: machine_loads[x])
        machine_jobs[m].append(i)
        machine_loads[m] += p
    return machine_jobs
