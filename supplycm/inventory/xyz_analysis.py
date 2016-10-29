"""XYZ analysis based on coefficient of variation."""
from typing import List, Tuple
import math


def xyz_analysis(demand_series: List[Tuple[str, List[float]]],
                x_threshold: float = 0.1,
                y_threshold: float = 0.25) -> List[Tuple[str, str, float]]:
    """Classify items by demand variability.

    X: CV <= 0.1 (stable), Y: 0.1 < CV <= 0.25, Z: CV > 0.25 (erratic).

    Example:
        >>> xyz_analysis([('a', [100, 100, 100]), ('b', [100, 50, 150])])
        [('a', 'X', 0.0), ('b', 'Z', 0.4082...)]
    """
    result = []
    for item, demands in demand_series:
        if not demands or len(demands) < 2:
            result.append((item, 'Z', 0.0))
            continue
        mean = sum(demands) / len(demands)
        if mean == 0:
            result.append((item, 'Z', 0.0))
            continue
        var = sum((d - mean) ** 2 for d in demands) / (len(demands) - 1)
        cv = math.sqrt(var) / mean
        cls = 'X' if cv <= x_threshold else ('Y' if cv <= y_threshold else 'Z')
        result.append((item, cls, cv))
    return result
