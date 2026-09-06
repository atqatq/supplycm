"""Schedule with parallel stations per workstation."""
from typing import List


def parallel_station_scheduling(arrival_times: List[float],
                                 processing_times: List[float],
                                 num_stations: int) -> List[List[int]]:
    """Assign jobs to parallel stations, each processing one at a time.

    Example:
        >>> sched = parallel_station_scheduling([0, 0, 1, 2], [3, 5, 2, 4], 2)
        >>> sum(len(s) for s in sched) == 4
        True
    """
    station_avail = [0.0] * num_stations
    assignment = [[] for _ in range(num_stations)]
    jobs = sorted(range(len(arrival_times)), key=lambda i: arrival_times[i])
    for j in jobs:
        # Find station available earliest after job arrival
        best_s = min(range(num_stations),
                     key=lambda s: max(station_avail[s], arrival_times[j]))
        assignment[best_s].append(j)
        station_avail[best_s] = max(station_avail[best_s], arrival_times[j]) + processing_times[j]
    return assignment
