"""Compute cannibalization effect of new product on existing."""
from typing import List, Tuple


def cannibalization_effect(existing_before: float, existing_after: float,
                           new_product_sales: float) -> float:
    """Fraction of new product sales that came from existing product.

    Example:
        >>> round(cannibalization_effect(100, 80, 50), 4)
        0.4
    """
    lost_sales = existing_before - existing_after
    if new_product_sales <= 0:
        return 0.0
    return lost_sales / new_product_sales
