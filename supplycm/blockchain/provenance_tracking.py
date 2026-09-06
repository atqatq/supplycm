"""Track product provenance through the supply chain."""
from typing import List, Dict


def provenance_tracking(events: List[Dict], product_id: str) -> List[Dict]:
    """Extract the full history of a product from supply chain events.

    Args:
        events: List of all supply chain events.
        product_id: Product to track.

    Returns:
        Chronological list of events for the product.

    Example:
        >>> events = [
        ...     {'product': 'A', 'event': 'manufactured', 'time': 1},
        ...     {'product': 'B', 'event': 'manufactured', 'time': 2},
        ...     {'product': 'A', 'event': 'shipped', 'time': 3},
        ... ]
        >>> history = provenance_tracking(events, 'A')
        >>> len(history) == 2
        True
    """
    history = [e for e in events if e.get('product') == product_id]
    history.sort(key=lambda e: e.get('time', 0))
    return history
