"""Buyback contract analysis."""


def buyback_contract(wholesale_price: float, retail_price: float,
                      buyback_price: float, demand: float,
                      unit_cost: float, salvage_value: float = 0) -> dict:
    """Analyze buyback contract.

    Example:
        >>> result = buyback_contract(50, 100, 30, 800, 20, 10)
        >>> isinstance(result['supplier_profit'], float)
        True
    """
    if buyback_price > wholesale_price:
        raise ValueError("buyback should not exceed wholesale")
    order_qty = demand
    unsold = max(0, order_qty - demand)
    supplier_revenue = wholesale_price * order_qty - buyback_price * unsold + salvage_value * unsold
    supplier_cost = unit_cost * order_qty
    supplier_profit = supplier_revenue - supplier_cost
    retailer_revenue = retail_price * demand + buyback_price * unsold
    retailer_cost = wholesale_price * order_qty
    retailer_profit = retailer_revenue - retailer_cost
    return {
        "supplier_profit": supplier_profit,
        "retailer_profit": retailer_profit,
        "total_profit": supplier_profit + retailer_profit,
    }
