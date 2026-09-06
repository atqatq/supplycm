"""Detect slow-moving inventory."""
from typing import List, Tuple


def slow_moving_detection(items: List[Tuple[str, float, float]],
                          slow_threshold: float = 0.2) -> List[Tuple[str, bool]]:
    """Flag items whose usage rate is below threshold.

    Args:
        items: List of (item_id, usage_rate, max_rate).
        slow_threshold: Ratio below which item is slow.

    Example:
        >>> slow_moving_detection([('a', 10, 100), ('b', 80, 100)])
        [('a', True), ('b', False)]
    """
    result = []
    for item, usage, max_rate in items:
        ratio = usage / max_rate if max_rate > 0 else 0
        result.append((item, ratio < slow_threshold))
    return result
