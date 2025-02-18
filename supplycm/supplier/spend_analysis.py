"""Spend analysis by category."""
from typing import Dict, List, Tuple


def spend_analysis(transactions: List[Tuple[str, str, float]]) -> Dict[str, Dict]:
    """Analyze spend by category and supplier.

    Args:
        transactions: List of (category, supplier, amount).

    Example:
        >>> sa = spend_analysis([('IT', 'A', 100), ('IT', 'B', 200), ('HR', 'A', 50)])
        >>> sa['IT']['total'] == 300
        True
    """
    by_category = {}
    for cat, sup, amt in transactions:
        if cat not in by_category:
            by_category[cat] = {'total': 0, 'suppliers': {}}
        by_category[cat]['total'] += amt
        by_category[cat]['suppliers'][sup] = by_category[cat]['suppliers'].get(sup, 0) + amt
    return by_category
