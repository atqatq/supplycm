"""Cycle Time Efficiency (Process Cycle Efficiency)."""


def cycle_time_efficiency(value_added_time: float, total_cycle_time: float) -> float:
    """PCE = value_added_time / total_cycle_time.

    Example:
        >>> round(cycle_time_efficiency(5, 50), 2)
        0.1
    """
    if total_cycle_time <= 0:
        raise ValueError("total cycle time must be positive")
    return value_added_time / total_cycle_time
