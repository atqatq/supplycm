"""Backflush inventory deduction upon completion."""
from typing import Dict, List, Tuple


def backflush(completed_qty: float, bom: Dict[int, List[Tuple[int, float]]],
              item: int = 0) -> Dict[int, float]:
    """Deduct components from inventory based on completed quantity.

    Example:
        >>> bf = backflush(10, {0: [(1, 2), (2, 3)]})
        >>> bf[1] == 20
        True
    """
    deductions = {}
    for comp, per in bom.get(item, []):
        deductions[comp] = per * completed_qty
    return deductions
