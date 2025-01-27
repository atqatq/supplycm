"""Supplier consolidation analysis."""
from typing import List, Tuple


def supplier_consolidation(current_spend: List[float],
                            consolidation_ratio: float = 0.3) -> Tuple[float, float]:
    """Estimate savings from reducing supplier count.

    Returns (estimated_savings, new_supplier_count).

    Example:
        >>> savings, count = supplier_consolidation([100, 200, 300, 400])
        >>> savings > 0
        True
    """
    total_spend = sum(current_spend)
    new_count = max(1, int(len(current_spend) * (1 - consolidation_ratio)))
    # Estimated savings: 5-15% of spend
    savings = total_spend * 0.1 * consolidation_ratio
    return savings, new_count
