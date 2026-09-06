"""Compute machine utilization from schedule."""
from typing import List


def machine_utilization(machine_loads: List[float], makespan: float) -> List[float]:
    """Utilization = load / makespan.

    Example:
        >>> machine_utilization([8, 6, 10], 10)
        [0.8, 0.6, 1.0]
    """
    if makespan <= 0:
        return [0.0] * len(machine_loads)
    return [load / makespan for load in machine_loads]
