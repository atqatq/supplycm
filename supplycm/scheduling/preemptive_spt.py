"""Preemptive SPT for single machine (SRPT)."""
from typing import List


def preemptive_spt(arrival_times: List[float], processing_times: List[float]) -> float:
    """Schedule with preemption, always processing job with shortest remaining time.

    Returns total completion time.

    Example:
        >>> round(preemptive_spt([0, 0, 0], [3, 5, 2]), 2)
        22.0
    """
    n = len(arrival_times)
    remaining = list(processing_times)
    completed = [0.0] * n
    time = 0.0
    done = 0
    events = sorted([(arrival_times[i], i) for i in range(n)])
    event_idx = 0
    while done < n:
        # Add arrivals up to current time
        while event_idx < n and events[event_idx][0] <= time:
            event_idx += 1
        # Find shortest remaining available job
        available = [i for i in range(n) if remaining[i] > 0 and arrival_times[i] <= time]
        if not available:
            if event_idx < n:
                time = events[event_idx][0]
                continue
            else:
                break
        current = min(available, key=lambda i: remaining[i])
        # Next event
        next_arrival = events[event_idx][0] if event_idx < n else float('inf')
        process_time = min(remaining[current], next_arrival - time)
        remaining[current] -= process_time
        time += process_time
        if remaining[current] == 0:
            completed[current] = time
            done += 1
    return sum(completed)
