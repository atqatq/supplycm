"""SPT (Shortest Processing Time) dispatching rule."""
from typing import List


def spt_rule(processing_times: List[float]) -> List[int]:
    """Order jobs by shortest processing time.

    Example:
        >>> spt_rule([5, 2, 8, 1])
        [3, 1, 0, 2]
    """
    return sorted(range(len(processing_times)), key=lambda i: processing_times[i])
