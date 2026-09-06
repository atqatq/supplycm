"""Inventory carrying rate."""


def inventory_carrying_rate(capital_cost: float, storage_cost: float,
                            risk_cost: float, inventory_value: float) -> float:
    """Carrying rate = (capital + storage + risk) / inventory_value.

    Example:
        >>> round(inventory_carrying_rate(0.10, 0.05, 0.02, 1.0), 4)
        0.17
    """
    if inventory_value <= 0:
        raise ValueError("inventory value must be positive")
    return (capital_cost + storage_cost + risk_cost) / inventory_value
