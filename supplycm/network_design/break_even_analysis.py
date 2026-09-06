"""Break-even analysis for facility decisions."""


def break_even_analysis(fixed_cost: float, variable_cost_per_unit: float,
                        price_per_unit: float) -> float:
    """Find break-even quantity where total revenue equals total cost.

    Args:
        fixed_cost: Total fixed costs.
        variable_cost_per_unit: Variable cost per unit.
        price_per_unit: Selling price per unit.

    Returns:
        Break-even quantity.

    Example:
        >>> break_even_analysis(10000, 5, 10)
        2000.0
    """
    contribution = price_per_unit - variable_cost_per_unit
    if contribution <= 0:
        raise ValueError("price must exceed variable cost")
    return fixed_cost / contribution
