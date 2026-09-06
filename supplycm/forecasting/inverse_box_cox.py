"""Inverse Box-Cox transformation."""
from typing import List
import math


def inverse_box_cox(data: List[float], lam: float = 0.0) -> List[float]:
    """Invert a Box-Cox transform.

    Example:
        >>> round(inverse_box_cox([0.0, 1.0, 2.0], 0.0)[1], 4)
        2.7183
    """
    if lam == 0:
        return [math.exp(x) for x in data]
    return [(x * lam + 1) ** (1 / lam) for x in data]
