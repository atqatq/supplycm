"""WSPT (Weighted SPT) rule."""
from typing import List


def wspt_rule(processing_times: List[float], weights: List[float]) -> List[int]:
    """Order by ratio weight/processing_time descending.

    Example:
        >>> wspt_rule([5, 2, 8], [1, 1, 4])
        [2, 1, 0]
    """
    return sorted(range(len(processing_times)),
                  key=lambda i: -weights[i] / processing_times[i] if processing_times[i] > 0 else 0)
