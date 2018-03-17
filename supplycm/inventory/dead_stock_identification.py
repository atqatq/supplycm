"""Identify dead stock."""
from typing import List, Tuple


def dead_stock_identification(items: List[Tuple[str, List[float]]],
                              periods: int = 6) -> List[Tuple[str, bool]]:
    """Flag items with zero demand in the last `periods` periods.

    Example:
        >>> dead_stock_identification([('a', [10, 0, 0, 0, 0, 0]), ('b', [0]*6)])
        [('a', False), ('b', True)]
    """
    result = []
    for item, history in items:
        last_n = history[-periods:]
        result.append((item, sum(last_n) == 0))
    return result
