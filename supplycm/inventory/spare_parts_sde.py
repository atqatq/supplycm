"""SDE classification by procurement difficulty."""
from typing import List, Tuple


def spare_parts_sde(lead_time_data: List[Tuple[str, float]],
                    scarce_threshold: float = 90,
                    difficult_threshold: float = 30) -> List[Tuple[str, str]]:
    """Classify parts by procurement lead time.

    Example:
        >>> spare_parts_sde([('a', 120), ('b', 60), ('c', 10)])
        [('a', 'S'), ('b', 'D'), ('c', 'E')]
    """
    result = []
    for item, lt in lead_time_data:
        cls = 'S' if lt >= scarce_threshold else ('D' if lt >= difficult_threshold else 'E')
        result.append((item, cls))
    return result
