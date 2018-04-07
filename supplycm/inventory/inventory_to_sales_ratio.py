"""Inventory-to-Sales ratio."""


def inventory_to_sales_ratio(inventory_value: float, sales_value: float) -> float:
    """I/S ratio = inventory / sales.

    Example:
        >>> inventory_to_sales_ratio(50000, 200000)
        0.25
    """
    if sales_value <= 0:
        raise ValueError("sales must be positive")
    return inventory_value / sales_value
