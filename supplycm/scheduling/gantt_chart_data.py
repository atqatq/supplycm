"""Generate Gantt chart data from schedule."""
from typing import Dict, List, Tuple


def gantt_chart_data(schedule: Dict[Tuple[int, int], Tuple[float, float]],
                     num_machines: int) -> List[List[Tuple[int, float, float]]]:
    """Convert schedule dict to per-machine list of (job, start, end).

    Example:
        >>> sched = {(0, 0): (0, 3), (1, 0): (3, 5)}
        >>> gantt = gantt_chart_data(sched, 1)
        >>> len(gantt[0]) == 2
        True
    """
    result = [[] for _ in range(num_machines)]
    # We need machine info; infer from op index assuming same routing
    # This is a simplified version
    for (job, op), (start, end) in sorted(schedule.items(), key=lambda x: x[1][0]):
        machine = op % num_machines  # simplistic assignment
        result[machine].append((job, start, end))
    return result
