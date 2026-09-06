"""Real-time inventory monitoring with threshold alerts."""
from typing import List, Dict


def realtime_inventory_monitor(current_levels: Dict[str, float],
                                reorder_points: Dict[str, float],
                                safety_stocks: Dict[str, float]) -> List[Dict]:
    """Generate alerts based on current inventory vs thresholds.

    Args:
        current_levels: Item -> current inventory.
        reorder_points: Item -> reorder point.
        safety_stocks: Item -> safety stock.

    Returns:
        List of alert dicts with severity levels.

    Example:
        >>> alerts = realtime_inventory_monitor(
        ...     {'A': 50, 'B': 20}, {'A': 40, 'B': 30}, {'A': 20, 'B': 15})
        >>> len(alerts) >= 1
        True
    """
    alerts = []
    for item, current in current_levels.items():
        rop = reorder_points.get(item, 0)
        ss = safety_stocks.get(item, 0)
        if current <= ss:
            alerts.append({
                'item': item,
                'severity': 'CRITICAL',
                'message': 'Inventory at or below safety stock',
                'current': current,
                'threshold': ss,
            })
        elif current <= rop:
            alerts.append({
                'item': item,
                'severity': 'WARNING',
                'message': 'Inventory at reorder point',
                'current': current,
                'threshold': rop,
            })
    return alerts
