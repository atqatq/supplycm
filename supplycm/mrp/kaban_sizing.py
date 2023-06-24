"""Kanban card sizing calculation."""
from typing import List


def kaban_sizing(demand_rate: float, lead_time: float, container_size: float,
                 safety_factor: float = 1.1) -> int:
    """Number of kanban cards = (D * L * alpha) / container_size.

    Example:
        >>> kaban_sizing(100, 2, 50, 1.1)
        5
    """
    if container_size <= 0:
        raise ValueError("container size must be positive")
    import math
    return math.ceil(demand_rate * lead_time * safety_factor / container_size)
