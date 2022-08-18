"""Bill of Materials (BOM) explosion for MRP."""
from typing import Dict, List, Tuple


def bom_explosion(demand: float, bom: Dict[int, List[Tuple[int, float]]],
                  parent: int = 0) -> Dict[int, float]:
    """Recursively compute component requirements from BOM.

    Args:
        demand: Demand for top-level item.
        bom: Dict item -> list of (component, quantity_per).
        parent: Top-level item.

    Returns:
        Dict component -> total quantity required.

    Example:
        >>> bom = {0: [(1, 2), (2, 3)], 1: [(3, 1)], 2: [], 3: []}
        >>> req = bom_explosion(10, bom, 0)
        >>> req[3] == 20
        True
    """
    requirements = {}
    def explode(item, qty):
        for comp, per in bom.get(item, []):
            requirements[comp] = requirements.get(comp, 0) + qty * per
            explode(comp, qty * per)
    explode(parent, demand)
    return requirements
