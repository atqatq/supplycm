"""VED classification for spare parts."""
from typing import List, Tuple


def spare_parts_ved(criticality_scores: List[Tuple[str, float]]) -> List[Tuple[str, str]]:
    """Classify spare parts by criticality.

    V (Vital) score >= 0.7, E (Essential) 0.4-0.7, D (Desirable) < 0.4.

    Example:
        >>> spare_parts_ved([('a', 0.9), ('b', 0.5), ('c', 0.2)])
        [('a', 'V'), ('b', 'E'), ('c', 'D')]
    """
    result = []
    for item, score in criticality_scores:
        cls = 'V' if score >= 0.7 else ('E' if score >= 0.4 else 'D')
        result.append((item, cls))
    return result
