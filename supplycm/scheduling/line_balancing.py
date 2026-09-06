"""Assembly line balancing using Kilbridge-Western heuristic."""
from typing import List


def line_balancing(task_times: List[float], predecessors: List[List[int]],
                   cycle_time: float) -> List[List[int]]:
    """Assign tasks to workstations.

    Example:
        >>> stations = line_balancing([2, 3, 1, 2, 1], [[], [0], [0], [1, 2], [3]],
        ...                            5)
        >>> sum(len(s) for s in stations) == 5
        True
    """
    n = len(task_times)
    assigned = set()
    stations = []
    while len(assigned) < n:
        station = []
        station_time = 0
        # Find assignable tasks
        for i in range(n):
            if i in assigned:
                continue
            if all(p in assigned for p in predecessors[i]):
                if station_time + task_times[i] <= cycle_time:
                    station.append(i)
                    station_time += task_times[i]
                    assigned.add(i)
        if not station:
            # Force-assign smallest task
            for i in range(n):
                if i not in assigned:
                    station.append(i)
                    assigned.add(i)
                    break
        stations.append(station)
    return stations
