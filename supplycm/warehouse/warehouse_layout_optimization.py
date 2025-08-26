"""Simple warehouse layout optimization (slot-distance minimization)."""
from typing import Dict, List, Tuple


def warehouse_layout_optimization(items: List[Tuple[str, float]],
                                   slots: List[Tuple[str, float]]) -> Dict[str, str]:
    """Assign items to slots minimizing total weighted travel distance.

    Args:
        items: (item_id, demand_frequency).
        slots: (slot_id, distance_from_picking_start).

    Example:
        >>> assign = warehouse_layout_optimization(
        ...     [('A', 100), ('B', 50), ('C', 10)],
        ...     [('S1', 1), ('S2', 5), ('S3', 10)])
        >>> assign['A'] == 'S1'
        True
    """
    sorted_items = sorted(items, key=lambda x: -x[1])
    sorted_slots = sorted(slots, key=lambda x: x[1])
    return {item_id: slot_id
            for (item_id, _), (slot_id, _) in zip(sorted_items, sorted_slots)}
