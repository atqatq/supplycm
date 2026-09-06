"""Planning BOM with option percentages."""
from typing import Dict, List


def planning_bom(forecast: float, option_percentages: Dict[str, float]) -> Dict[str, float]:
    """Compute requirements for product options based on planning percentages.

    Example:
        >>> pb = planning_bom(1000, {'red': 0.3, 'blue': 0.5, 'green': 0.2})
        >>> pb['blue']
        500.0
    """
    return {opt: forecast * pct for opt, pct in option_percentages.items()}
