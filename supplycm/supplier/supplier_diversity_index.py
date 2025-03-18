"""Supplier diversity index (Herfindahl-like)."""
from typing import List


def supplier_diversity_index(spend_per_supplier: List[float]) -> float:
    """Compute 1 - HHI to measure diversity (0=monopoly, 1=fully diverse).

    Example:
        >>> round(supplier_diversity_index([100, 100, 100]), 4)
        0.9667
    """
    total = sum(spend_per_supplier)
    if total == 0:
        return 1.0
    hhi = sum((s / total) ** 2 for s in spend_per_supplier)
    return 1 - hhi
