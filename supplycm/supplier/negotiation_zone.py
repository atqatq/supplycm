"""Negotiation zone analysis (ZOPA)."""
from typing import Tuple


def negotiation_zone(buyer_walkaway: float, supplier_walkaway: float) -> Tuple[float, float, bool]:
    """Compute Zone of Possible Agreement.

    Returns (lower_bound, upper_bound, agreement_possible).

    Example:
        >>> lo, hi, ok = negotiation_zone(100, 80)
        >>> ok and lo <= hi
        True
    """
    if buyer_walkaway >= supplier_walkaway:
        return supplier_walkaway, buyer_walkaway, True
    return buyer_walkaway, supplier_walkaway, False
