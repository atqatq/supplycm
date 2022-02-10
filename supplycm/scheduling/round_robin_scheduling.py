"""Round-robin scheduling with time quantum."""
from typing import List
from collections import deque


def round_robin_scheduling(arrival_times: List[float], processing_times: List[float],
                            quantum: float = 1.0) -> List[float]:
    """Round-robin scheduling. Returns completion times per job.

    Example:
        >>> ct = round_robin_scheduling([0, 0, 0], [3, 5, 2], 1.0)
        >>> len(ct) == 3
        True
    """
    n = len(arrival_times)
    remaining = list(processing_times)
    completion = [0.0] * n
    ready = deque()
    arrived = [False] * n
    time = 0.0
    # Initial arrivals
    for i in sorted(range(n), key=lambda x: arrival_times[x]):
        if arrival_times[i] <= time:
            ready.append(i)
            arrived[i] = True
    while ready or not all(arrived):
        if not ready:
            # Find next arrival
            for i in sorted(range(n), key=lambda x: arrival_times[x]):
                if not arrived[i]:
                    ready.append(i)
                    arrived[i] = True
                    time = max(time, arrival_times[i])
                    break
            continue
        job = ready.popleft()
        process = min(quantum, remaining[job])
        time += process
        remaining[job] -= process
        # Add new arrivals
        for i in range(n):
            if not arrived[i] and arrival_times[i] <= time:
                ready.append(i)
                arrived[i] = True
        if remaining[job] > 0:
            ready.append(job)
        else:
            completion[job] = time
    return completion
