"""Quantity flexibility contract analysis."""


def quantity_flexibility_contract(wholesale_price: float, retail_price: float,
                                   order_quantity: float, actual_demand: float,
                                   unit_cost: float, flexibility_fraction: float = 0.2) -> dict:
    """Analyze quantity flexibility contract.

    Example:
        >>> result = quantity_flexibility_contract(50, 100, 1000, 900, 20, 0.2)
        >>> result['final_quantity'] <= 1000
        True
    """
    if flexibility_fraction < 0 or flexibility_fraction > 1:
        raise ValueError("flexibility must be in [0, 1]")
    min_qty = order_quantity * (1 - flexibility_fraction)
    max_qty = order_quantity * (1 + flexibility_fraction)
    final_qty = max(min_qty, min(max_qty, actual_demand))
    sales = min(final_qty, actual_demand)
    unsold = final_qty - sales
    supplier_profit = wholesale_price * final_qty - unit_cost * final_qty
    retailer_profit = retail_price * sales + 0 * unsold - wholesale_price * final_qty
    return {
        "final_quantity": final_qty,
        "supplier_profit": supplier_profit,
        "retailer_profit": retailer_profit,
        "total_profit": supplier_profit + retailer_profit,
    }
