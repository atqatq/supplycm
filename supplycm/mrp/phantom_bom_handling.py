"""Handle phantom items in BOM (skip-level processing)."""
from typing import Dict, List, Set, Tuple


def phantom_bom_handling(bom: Dict[int, List[Tuple[int, float]]],
                          phantoms: Set[int],
                          top_item: int, demand: float) -> Dict[int, float]:
    """Process BOM treating phantom items as transparent (no inventory).

    Example:
        >>> bom = {0: [(1, 2)], 1: [(2, 3)], 2: []}
        >>> req = phantom_bom_handling(bom, {1}, 0, 10)
        >>> req[2] == 60
        True
    """
    requirements = {}
    def explode(item, qty):
        if item in phantoms:
            for comp, per in bom.get(item, []):
                explode(comp, qty * per)
        else:
            for comp, per in bom.get(item, []):
                requirements[comp] = requirements.get(comp, 0) + qty * per
                explode(comp, qty * per)
    explode(top_item, demand)
    return requirements
