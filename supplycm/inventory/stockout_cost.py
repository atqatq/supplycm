"""Expected stockout cost."""


def stockout_cost(expected_shortage: float, shortage_penalty: float) -> float:
    """Cost = expected shortage * unit shortage cost.

    Example:
        >>> stockout_cost(5, 10)
        50
    """
    if expected_shortage < 0 or shortage_penalty < 0:
        raise ValueError("inputs must be non-negative")
    return expected_shortage * shortage_penalty
