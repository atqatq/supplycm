"""Low-level coding for BOM items."""
from typing import Dict, List


def low_level_coding(bom: Dict[int, List[int]]) -> Dict[int, int]:
    """Assign each item its lowest level in the BOM hierarchy.

    Args:
        bom: Dict item -> list of immediate children.

    Returns:
        Dict item -> level (0 = top).

    Example:
        >>> bom = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> llc = low_level_coding(bom)
        >>> llc[3] >= 2
        True
    """
    levels = {}
    def level(item):
        if item in levels:
            return levels[item]
        children = bom.get(item, [])
        if not children:
            levels[item] = 0
        else:
            levels[item] = 1 + max(level(c) for c in children)
        return levels[item]
    for item in bom:
        level(item)
    return levels
