"""PO compliance rate."""
from typing import List


def purchase_order_compliance(orders: List, contracts: List) -> float:
    """Fraction of orders that match an existing contract.

    Example:
        >>> purchase_order_compliance(['a', 'b', 'c'], ['a', 'c'])
        0.6666...
    """
    if not orders:
        return 0.0
    contracts_set = set(contracts)
    compliant = sum(1 for o in orders if o in contracts_set)
    return compliant / len(orders)
