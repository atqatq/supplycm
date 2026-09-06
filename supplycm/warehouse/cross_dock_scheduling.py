"""Cross-docking door assignment."""
from typing import List, Tuple


def cross_dock_scheduling(inbound_trailers: List[Tuple[float, float]],
                          outbound_trailers: List[Tuple[float, float]],
                          num_doors: int) -> Tuple[List[int], List[int]]:
    """Assign trailers to doors (FCFS).

    Args:
        inbound_trailers: (arrival, unload_time).
        outbound_trailers: (arrival, load_time).

    Returns:
        (inbound_door_assignments, outbound_door_assignments).

    Example:
        >>> ib, ob = cross_dock_scheduling([(0, 30), (10, 20)], [(20, 15)], 2)
        >>> len(ib) == 2 and len(ob) == 1
        True
    """
    door_avail = [0.0] * num_doors
    ib_assign = []
    for arr, unload in inbound_trailers:
        door = min(range(num_doors), key=lambda d: max(door_avail[d], arr))
        ib_assign.append(door)
        door_avail[door] = max(door_avail[door], arr) + unload
    door_avail = [0.0] * num_doors
    ob_assign = []
    for arr, load in outbound_trailers:
        door = min(range(num_doors), key=lambda d: max(door_avail[d], arr))
        ob_assign.append(door)
        door_avail[door] = max(door_avail[door], arr) + load
    return ib_assign, ob_assign
