"""Competitive bidding evaluation."""
from typing import Dict, List, Tuple


def competitive_bidding(bids: List[Tuple[str, float, float]],
                         price_weight: float = 0.7,
                         quality_weight: float = 0.3) -> Tuple[str, float]:
    """Evaluate bids and select winner.

    Args:
        bids: List of (supplier, price, quality_score).

    Example:
        >>> winner, score = competitive_bidding([('A', 100, 80), ('B', 110, 95)])
        >>> winner in ('A', 'B')
        True
    """
    if not bids:
        raise ValueError("no bids")
    min_price = min(b[1] for b in bids)
    max_quality = max(b[2] for b in bids)
    best_supplier = None
    best_score = -1
    for supplier, price, quality in bids:
        norm_price = min_price / price if price > 0 else 0
        norm_quality = quality / max_quality if max_quality > 0 else 0
        score = price_weight * norm_price + quality_weight * norm_quality
        if score > best_score:
            best_score = score
            best_supplier = supplier
    return best_supplier, best_score
