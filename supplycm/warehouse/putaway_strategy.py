"""Putaway location assignment."""
from typing import Dict, List, Tuple


def putaway_strategy(items: List[Tuple[str, str, float, float]],
                     slots: List[Tuple[str, float]]) -> Dict[str, str]:
    """Assign items to slots by volume and ABC class.

    Args:
        items: (item_id, abc_class, volume, demand).
        slots: (slot_id, capacity).

    Example:
        >>> assignments = putaway_strategy([('A', 'A', 5, 100), ('B', 'B', 10, 20)],
        ...                                [('S1', 10), ('S2', 20)])
        >>> len(assignments) == 2
        True
    """
    # Sort items: A-class first, then by demand
    sorted_items = sorted(items, key=lambda x: (x[1], -x[3]))
    sorted_slots = sorted(slots, key=lambda s: s[1])  # smallest first for A items? configurable
    assignments = {}
    used_slots = set()
    for item_id, cls, vol, _ in sorted_items:
        for slot_id, cap in sorted_slots:
            if slot_id not in used_slots and vol <= cap:
                assignments[item_id] = slot_id
                used_slots.add(slot_id)
                break
    return assignments
