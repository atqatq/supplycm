"""Apply planning time fence for lot sizing method selection."""
from typing import List


def planning_time_fence(demands: List[float], fence_period: int,
                        lot_size_fenced: int, lot_size_open: int = 1) -> List[float]:
    """Use lot-for-lot inside fence, fixed lot size outside.

    Example:
        >>> ptf = planning_time_fence([10, 20, 30, 40], 2, 50)
        >>> ptf[0] == 10 and ptf[2] == 50
        True
    """
    n = len(demands)
    result = []
    for t in range(n):
        if t < fence_period:
            result.append(demands[t])  # lot-for-lot
        else:
            # Use fixed lot size if any demand
            if demands[t] > 0:
                lots = -(-demands[t] // lot_size_fenced) if lot_size_fenced > 0 else 1
                result.append(lots * lot_size_fenced)
            else:
                result.append(0)
    return result
