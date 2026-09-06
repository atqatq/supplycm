"""Return (largest-gap) routing heuristic."""
from typing import List, Tuple


def return_routing(pick_aisles: List[Tuple[int, float, float]]) -> List[int]:
    """Route through aisles entering from one end.

    Args:
        pick_aisles: (aisle_num, start_pos, end_pos).

    Example:
        >>> route = return_routing([(1, 0, 10), (2, 0, 15)])
        >>> len(route) > 0
        True
    """
    if not pick_aisles:
        return []
    sorted_aisles = sorted(pick_aisles, key=lambda x: x[0])
    route = []
    for aisle, _, _ in sorted_aisles:
        route.append(aisle)
    for aisle in reversed(sorted_aisles[:-1]):
        route.append(aisle[0])
    return route
