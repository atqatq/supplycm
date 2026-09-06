"""Should-cost analysis for negotiated pricing."""
from typing import Dict


def should_cost_analysis(material_costs: Dict[str, float],
                          labor_hours: float, labor_rate: float,
                          overhead_rate: float, profit_margin: float) -> float:
    """Estimate fair price.

    Example:
        >>> round(should_cost_analysis({'steel': 50, 'plastic': 20}, 2, 30, 1.5, 0.1), 2)
        173.5
    """
    material = sum(material_costs.values())
    labor = labor_hours * labor_rate
    overhead = labor * overhead_rate
    subtotal = material + labor + overhead
    return subtotal * (1 + profit_margin)
