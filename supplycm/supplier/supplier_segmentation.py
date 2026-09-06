"""Supplier segmentation matrix (Kraljic)."""
from typing import List, Tuple


def supplier_segmentation(suppliers: List[Tuple[str, float, float]],
                          profit_threshold: float = 0.5,
                          risk_threshold: float = 0.5) -> List[Tuple[str, str]]:
    """Classify suppliers as Strategic/Leverage/Bottleneck/Routine.

    Args:
        suppliers: (id, profit_impact, supply_risk).

    Example:
        >>> seg = supplier_segmentation([('A', 0.8, 0.7), ('B', 0.3, 0.3)])
        >>> seg[0][1] == 'Strategic'
        True
    """
    result = []
    for sid, profit, risk in suppliers:
        if profit >= profit_threshold and risk >= risk_threshold:
            cls = 'Strategic'
        elif profit >= profit_threshold and risk < risk_threshold:
            cls = 'Leverage'
        elif profit < profit_threshold and risk >= risk_threshold:
            cls = 'Bottleneck'
        else:
            cls = 'Routine'
        result.append((sid, cls))
    return result
