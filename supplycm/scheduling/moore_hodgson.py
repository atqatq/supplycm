"""Moore-Hodgson algorithm to minimize number of tardy jobs."""
from typing import List


def moore_hodgson(processing_times: List[float], due_dates: List[float]) -> List[int]:
    """Minimize the number of tardy jobs on a single machine.

    Example:
        >>> moore_hodgson([3, 1, 2], [5, 1, 6])
        [1, 0, 2]
    """
    n = len(processing_times)
    jobs = sorted(range(n), key=lambda i: due_dates[i])
    on_time = []
    time = 0
    for j in jobs:
        on_time.append(j)
        time += processing_times[j]
        if time > due_dates[j]:
            # Remove longest job from on_time set
            longest = max(on_time, key=lambda i: processing_times[i])
            on_time.remove(longest)
            time -= processing_times[longest]
    tardy = [j for j in jobs if j not in on_time]
    return on_time + tardy
