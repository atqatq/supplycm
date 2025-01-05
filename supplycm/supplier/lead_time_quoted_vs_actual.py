"""Compare quoted vs actual lead times."""
from typing import List, Tuple


def lead_time_quoted_vs_actual(lead_times: List[Tuple[float, float]]) -> Tuple[float, float, float]:
    """Compute (avg_quoted, avg_actual, avg_deviation).

    Example:
        >>> q, a, d = lead_time_quoted_vs_actual([(10, 12), (15, 14)])
        >>> q == 12.5
        True
    """
    if not lead_times:
        return 0, 0, 0
    quoted = sum(lt[0] for lt in lead_times) / len(lead_times)
    actual = sum(lt[1] for lt in lead_times) / len(lead_times)
    deviation = actual - quoted
    return quoted, actual, deviation
