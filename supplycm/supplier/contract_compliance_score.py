"""Contract compliance scoring."""
from typing import Dict, List


def contract_compliance_score(terms: Dict[str, bool]) -> float:
    """Fraction of contract terms met.

    Example:
        >>> round(contract_compliance_score({'on_time': True, 'quality': True, 'cost': False}), 2)
        0.67
    """
    if not terms:
        return 0.0
    return sum(1 for v in terms.values() if v) / len(terms)
