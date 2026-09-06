"""Where-used query to find parents of a component."""
from typing import Dict, List


def where_used_query(bom: Dict[int, List[int]], component: int) -> List[int]:
    """Find all items that directly or indirectly use a component.

    Example:
        >>> bom = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> where_used_query(bom, 3)
        [0, 1, 2]
    """
    parents = {c: [] for c in bom}
    for parent, children in bom.items():
        for c in children:
            parents.setdefault(c, []).append(parent)
    result = set()
    def traverse(item):
        for p in parents.get(item, []):
            if p not in result:
                result.add(p)
                traverse(p)
    traverse(component)
    return sorted(result)
