"""On-time delivery rate calculation."""
from typing import List, Tuple


def on_time_delivery_rate(deliveries: List[Tuple[float, float]]) -> float:
    """Fraction of deliveries on or before due date.

    Args:
        deliveries: (due_date, actual_date) tuples.

    Example:
        >>> on_time_delivery_rate([(10, 9), (15, 15), (20, 22)])
        0.6666...
    """
    if not deliveries:
        return 0.0
    on_time = sum(1 for due, actual in deliveries if actual <= due)
    return on_time / len(deliveries)
