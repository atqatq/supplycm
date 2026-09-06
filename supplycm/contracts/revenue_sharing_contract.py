"""Revenue sharing contract analysis."""


def revenue_sharing_contract(wholesale_price: float, retail_price: float,
                              revenue_share_fraction: float,
                              demand: float, unit_cost: float) -> dict:
    """Analyze revenue sharing contract.

    Example:
        >>> result = revenue_sharing_contract(40, 100, 0.2, 1000, 20)
        >>> result['supplier_profit'] > 0
        True
    """
    if revenue_share_fraction < 0 or revenue_share_fraction > 1:
        raise ValueError("share must be in [0, 1]")
    supplier_revenue = wholesale_price * demand + revenue_share_fraction * retail_price * demand
    supplier_cost = unit_cost * demand
    supplier_profit = supplier_revenue - supplier_cost
    retailer_revenue = (1 - revenue_share_fraction) * retail_price * demand
    retailer_cost = wholesale_price * demand
    retailer_profit = retailer_revenue - retailer_cost
    return {
        "supplier_profit": supplier_profit,
        "retailer_profit": retailer_profit,
        "total_profit": supplier_profit + retailer_profit,
    }
