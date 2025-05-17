"""ABC-based warehouse slotting (A items near front)."""
from typing import List, Tuple


def warehouse_slotting_abc(items: List[Tuple[str, float, float]],
                            num_zones: int = 3) -> List[Tuple[str, int]]:
    """Assign items to zones based on demand frequency (ABC).

    Args:
        items: (item_id, demand_volume, cube_size).

    Returns:
        List of (item, zone) where zone 0 is closest to shipping.

    Example:
        >>> slotting = warehouse_slotting_abc([('a', 1000, 1), ('b', 100, 1), ('c', 10, 1)])
        >>> slotting[0][1] == 0  # highest-demand item in zone 0
        True
    """
    sorted_items = sorted(items, key=lambda x: -x[1])
    n = len(sorted_items)
    if n == 0:
        return []
    zone_size = max(1, n // num_zones)
    result = []
    for i, (item, _, _) in enumerate(sorted_items):
        zone = min(i // zone_size, num_zones - 1)
        result.append((item, zone))
    return result
