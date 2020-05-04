"""Vehicle scheduling problem."""
from typing import List, Tuple


def vehicle_scheduling(trips: List[Tuple[float, float]]) -> int:
    """Minimum number of vehicles to cover all trips (interval partitioning).

    Args:
        trips: List of (start_time, end_time).

    Returns:
        Minimum number of vehicles.

    Example:
        >>> vehicle_scheduling([(1, 3), (2, 4), (3, 5), (4, 6)])
        2
    """
    if not trips:
        return 0
    events = []
    for s, e in trips:
        events.append((s, 1))
        events.append((e, -1))
    events.sort()
    current = 0
    max_vehicles = 0
    for _, delta in events:
        current += delta
        max_vehicles = max(max_vehicles, current)
    return max_vehicles
