"""FSN classification by usage rate."""
from typing import List, Tuple


def spare_parts_fsn(usage_data: List[Tuple[str, float, float]],
                    fast_threshold: float = 0.7,
                    slow_threshold: float = 0.3) -> List[Tuple[str, str]]:
    """Classify parts by usage rate (Fast/Slow/Non-moving).

    Args:
        usage_data: List of (item_id, annual_usage, max_possible_usage).
        fast_threshold: Ratio above which item is Fast.
        slow_threshold: Ratio above which item is Slow (else Non-moving).

    Example:
        >>> spare_parts_fsn([('a', 80, 100), ('b', 40, 100), ('c', 5, 100)])
        [('a', 'F'), ('b', 'S'), ('c', 'N')]
    """
    result = []
    for item, usage, max_usage in usage_data:
        ratio = usage / max_usage if max_usage > 0 else 0
        cls = 'F' if ratio >= fast_threshold else ('S' if ratio >= slow_threshold else 'N')
        result.append((item, cls))
    return result
