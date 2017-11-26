"""Inventory position calculation."""


def inventory_position(on_hand: float, on_order: float, backorders: float = 0.0) -> float:
    """IP = on_hand + on_order - backorders.

    Example:
        >>> inventory_position(100, 50, 20)
        130
    """
    return on_hand + on_order - backorders
