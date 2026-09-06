"""Job shop scheduling with operation precedence."""
from typing import Dict, List, Tuple


def job_shop_schedule(jobs: List[List[Tuple[int, float]]]) -> Dict[Tuple[int, int], Tuple[float, float]]:
    """Greedy job shop scheduling.

    Args:
        jobs: For each job, list of (machine, processing_time) in order.

    Returns:
        Dict mapping (job_idx, op_idx) to (start, end).

    Example:
        >>> sched = job_shop_schedule([[(0, 3), (1, 5)], [(1, 2), (0, 4)]])
        >>> len(sched) == 4
        True
    """
    machine_avail = {}
    job_step = [0] * len(jobs)
    job_avail = [0.0] * len(jobs)
    schedule = {}
    total_ops = sum(len(j) for j in jobs)
    completed = 0
    while completed < total_ops:
        # Pick job whose next op can start earliest
        best = None
        best_start = float('inf')
        for j in range(len(jobs)):
            if job_step[j] >= len(jobs[j]):
                continue
            machine, p = jobs[j][job_step[j]]
            start = max(job_avail[j], machine_avail.get(machine, 0))
            if start < best_start:
                best_start = start
                best = (j, machine, p)
        j, machine, p = best
        start = best_start
        end = start + p
        schedule[(j, job_step[j])] = (start, end)
        job_avail[j] = end
        machine_avail[machine] = end
        job_step[j] += 1
        completed += 1
    return schedule
