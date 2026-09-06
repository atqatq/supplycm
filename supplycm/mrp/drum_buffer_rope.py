"""Drum-Buffer-Rope (DBR) scheduling from Theory of Constraints."""
from typing import List


def drum_buffer_rope(demands: List[float], constraint_capacity: float,
                     buffer_time: float, shipping_buffer: float = 0) -> List[float]:
    """Schedule production based on constraint (drum).

    Example:
        >>> dbr = drum_buffer_rope([10, 20, 30], 25, 2)
        >>> len(dbr) == 3
        True
    """
    n = len(demands)
    schedule = [0.0] * n
    # Constraint dictates pace
    cum_constraint = 0
    cum_demand = 0
    for t in range(n):
        cum_demand += demands[t]
        # Constraint can only process constraint_capacity per period
        cum_constraint = min(cum_demand, cum_constraint + constraint_capacity)
        # Release material buffer_time periods earlier
        release_t = t - buffer_time
        if 0 <= release_t < n:
            schedule[release_t] = demands[t]
    return schedule
