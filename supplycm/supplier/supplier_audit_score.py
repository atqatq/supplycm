"""Supplier audit score from checklist."""
from typing import Dict, List


def supplier_audit_score(findings: Dict[str, List[int]],
                          max_scores: Dict[str, int]) -> Dict[str, float]:
    """Compute audit scores by category.

    Args:
        findings: Category -> list of scores.
        max_scores: Category -> max possible score.

    Example:
        >>> score = supplier_audit_score({'quality': [8, 9, 7]}, {'quality': 10})
        >>> score['quality'] == 0.8
        True
    """
    result = {}
    for cat, scores in findings.items():
        avg = sum(scores) / len(scores) if scores else 0
        mx = max_scores.get(cat, 1)
        result[cat] = avg / mx if mx > 0 else 0
    return result
