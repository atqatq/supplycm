"""PERT expected duration and variance."""
from typing import List, Tuple


def pert_expected_duration(optimistic: List[float], most_likely: List[float],
                            pessimistic: List[float]) -> List[Tuple[float, float]]:
    """Expected time = (o + 4m + p) / 6, variance = ((p-o)/6)^2.

    Example:
        >>> pert = pert_expected_duration([1, 2], [3, 4], [5, 6])
        >>> round(pert[0][0], 4)
        3.0
    """
    result = []
    for o, m, p in zip(optimistic, most_likely, pessimistic):
        exp = (o + 4 * m + p) / 6
        var = ((p - o) / 6) ** 2
        result.append((exp, var))
    return result


from typing import List, Tuple
