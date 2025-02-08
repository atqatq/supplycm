"""Purchase Price Variance (PPV)."""
from typing import List


def purchase_price_variance(actual_price: float, standard_price: float,
                             quantity: float) -> float:
    """PPV = (actual - standard) * quantity.

    Example:
        >>> purchase_price_variance(11, 10, 1000)
        1000.0
    """
    return (actual_price - standard_price) * quantity
