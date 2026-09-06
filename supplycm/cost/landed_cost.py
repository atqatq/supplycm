"""Landed cost calculation."""


def landed_cost(unit_price: float, freight: float, duty_rate: float = 0,
                insurance_rate: float = 0, handling: float = 0,
                customs_broker: float = 0, quantity: float = 1) -> float:
    """Total cost per unit including all logistics expenses.

    Example:
        >>> round(landed_cost(100, 500, 0.05, 0.01, 100, 50, 10), 2)
        165.5
    """
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    subtotal = unit_price * quantity
    duty = subtotal * duty_rate
    insurance = subtotal * insurance_rate
    total = subtotal + freight + duty + insurance + handling + customs_broker
    return total / quantity
