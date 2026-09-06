"""Center of Gravity method for facility location."""
from typing import List, Tuple


def center_of_gravity(customers: List[Tuple[float, float, float]]) -> Tuple[float, float]:
    """Find optimal facility location minimizing weighted distance.

    Args:
        customers: List of (x, y, volume) tuples.

    Returns:
        Tuple (x, y) of optimal facility location.

    Example:
        >>> x, y = center_of_gravity([(0, 0, 10), (10, 0, 20), (5, 10, 15)])
        >>> round(x, 2)
        6.11
    """
    total_vol = sum(c[2] for c in customers)
    if total_vol == 0:
        raise ValueError("total volume must be positive")
    cx = sum(c[0] * c[2] for c in customers) / total_vol
    cy = sum(c[1] * c[2] for c in customers) / total_vol
    return cx, cy
