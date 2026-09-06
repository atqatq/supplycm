"""Pallet building / carton packing (simplified)."""
from typing import List, Tuple


def pallet_building(items: List[Tuple[float, float, float]],
                     pallet_capacity: float) -> List[List[int]]:
    """Bin-pack items into pallets (First-Fit Decreasing by volume).

    Args:
        items: (length, width, height) per item.

    Example:
        >>> pallets = pallet_building([(1,1,1), (2,2,2), (1,1,1)], 8)
        >>> sum(len(p) for p in pallets) == 3
        True
    """
    volumes = [(i, l * w * h) for i, (l, w, h) in enumerate(items)]
    volumes.sort(key=lambda x: -x[1])
    pallets = []  # list of (remaining_capacity, [item_indices])
    for idx, vol in volumes:
        placed = False
        for i, (rem, items_list) in enumerate(pallets):
            if vol <= rem:
                pallets[i] = (rem - vol, items_list + [idx])
                placed = True
                break
        if not placed:
            pallets.append((pallet_capacity - vol, [idx]))
    return [items_list for _, items_list in pallets]
