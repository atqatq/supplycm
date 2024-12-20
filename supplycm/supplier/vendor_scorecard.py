"""Build vendor scorecard."""
from typing import Dict, List


def vendor_scorecard(vendors: List[str], metrics: List[str],
                     scores: List[List[float]],
                     weights: List[float]) -> Dict[str, Dict]:
    """Build scorecard with weighted totals and ranks.

    Example:
        >>> sc = vendor_scorecard(['A', 'B'], ['quality', 'delivery'],
        ...                       [[90, 85], [80, 95]], [0.6, 0.4])
        >>> sc['A']['total']
        88.0
    """
    totals = [sum(scores[i][j] * weights[j] for j in range(len(metrics)))
              for i in range(len(vendors))]
    ranks = sorted(range(len(vendors)), key=lambda i: -totals[i])
    rank_of = {vendors[ranks[r]]: r + 1 for r in range(len(vendors))}
    return {
        v: {
            'scores': {metrics[j]: scores[i][j] for j in range(len(metrics))},
            'total': totals[i],
            'rank': rank_of[v],
        }
        for i, v in enumerate(vendors)
    }
