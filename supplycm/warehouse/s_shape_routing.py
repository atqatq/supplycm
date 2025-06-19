"""S-shape (transversal) routing for order picking."""
from typing import List, Tuple


def s_shape_routing(pick_aisles: List[int]) -> List[int]:
    """Route through aisles in S-shape pattern.

    Args:
        pick_aisles: List of aisle numbers to visit (sorted).

    Example:
        >>> s_shape_routing([1, 3, 5, 7])
        [1, 3, 5, 7, 5, 3, 1]
    """
    if not pick_aisles:
        return []
    sorted_aisles = sorted(pick_aisles)
    return sorted_aisles + sorted_aisles[-2::-1] if len(sorted_aisles) > 1 else sorted_aisles
