"""Strategic supplier scorecard with weighted KPIs."""
from typing import Dict, List


def strategic_supplier_scorecard(kpis: Dict[str, float],
                                  weights: Dict[str, float]) -> Dict[str, float]:
    """Compute weighted KPIs and overall score.

    Example:
        >>> sc = strategic_supplier_scorecard(
        ...     {'quality': 95, 'delivery': 90, 'cost': 85, 'innovation': 80},
        ...     {'quality': 0.3, 'delivery': 0.3, 'cost': 0.2, 'innovation': 0.2})
        >>> 80 < sc['overall_score'] < 100
        True
    """
    overall = sum(kpis[k] * weights.get(k, 0) for k in kpis)
    result = {f'weighted_{k}': kpis[k] * weights.get(k, 0) for k in kpis}
    result['overall_score'] = overall
    return result
