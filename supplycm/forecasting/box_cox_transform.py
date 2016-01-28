"""Box-Cox transformation."""
from typing import List
import math


def box_cox_transform(data: List[float], lam: float = 0.0) -> List[float]:
    """Apply Box-Cox transformation.

    lam != 0: (x^lam - 1) / lam
    lam == 0: ln(x)

    Example:
        >>> round(box_cox_transform([1.0, math.e, math.e**2], 0.0)[1], 4)
        1.0
    """
    if any(d <= 0 for d in data):
        raise ValueError("Box-Cox requires positive data")
    if lam == 0:
        return [math.log(x) for x in data]
    return [(x ** lam - 1) / lam for x in data]
