"""Modular BOM for product families."""
from typing import Dict, List, Tuple


def modular_bom(product_family_demand: Dict[str, float],
                module_ratios: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    """Compute module/component requirements for a product family.

    Args:
        product_family_demand: Family -> demand.
        module_ratios: Family -> (module -> ratio per unit).

    Returns:
        Dict module -> total requirement.

    Example:
        >>> req = modular_bom({'A': 100, 'B': 50}, {'A': {'M1': 2}, 'B': {'M1': 1}})
        >>> req['M1'] == 250
        True
    """
    result = {}
    for family, demand in product_family_demand.items():
        for module, ratio in module_ratios.get(family, {}).items():
            result[module] = result.get(module, 0) + demand * ratio
    return result
