"""Detect off-contract purchases."""
from typing import List, Set, Tuple


def maverick_spend_detection(transactions: List[Tuple[str, str, float]],
                              preferred_suppliers: Set[str]) -> List[Tuple[str, float]]:
    """Find purchases from non-preferred suppliers.

    Args:
        transactions: (item, supplier, amount).

    Example:
        >>> maverick = maverick_spend_detection([('a', 'A', 100), ('b', 'X', 200)],
        ...                                      {'A', 'B'})
        >>> maverick[0][1] == 200
        True
    """
    return [(item, amt) for item, sup, amt in transactions if sup not in preferred_suppliers]
