"""Preferred supplier index computation."""
from typing import Dict, List


def preferred_supplier_index(suppliers: List[Dict[str, float]],
                              weights: Dict[str, float],
                              threshold: float = 70.0) -> List[str]:
    """Return names of suppliers above threshold.

    Example:
        >>> psi = preferred_supplier_index(
        ...     [{'name': 'A', 'quality': 80, 'delivery': 90},
        ...      {'name': 'B', 'quality': 60, 'delivery': 65}],
        ...     {'quality': 0.5, 'delivery': 0.5}, 70)
        >>> psi
        ['A']
    """
    preferred = []
    for sup in suppliers:
        score = sum(sup[k] * weights.get(k, 0) for k in weights)
        if score >= threshold:
            preferred.append(sup['name'])
    return preferred
