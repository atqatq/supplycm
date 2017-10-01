"""HML classification by unit cost."""
from typing import List, Tuple


def spare_parts_hml(prices: List[Tuple[str, float]],
                    high_threshold: float = 100.0,
                    medium_threshold: float = 20.0) -> List[Tuple[str, str]]:
    """Classify parts by unit price: High/Medium/Low.

    Example:
        >>> spare_parts_hml([('a', 500), ('b', 50), ('c', 5)])
        [('a', 'H'), ('b', 'M'), ('c', 'L')]
    """
    result = []
    for item, price in prices:
        cls = 'H' if price >= high_threshold else ('M' if price >= medium_threshold else 'L')
        result.append((item, cls))
    return result
