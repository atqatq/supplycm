"""Price analysis comparing supplier quotes."""
from typing import List, Tuple
import statistics


def price_analysis(quotes: List[float]) -> Tuple[float, float, float, float]:
    """Return (min, mean, median, stdev) of quotes.

    Example:
        >>> m, mu, med, s = price_analysis([100, 110, 105, 95])
        >>> m == 95
        True
    """
    if not quotes:
        raise ValueError("quotes cannot be empty")
    n = len(quotes)
    mean = sum(quotes) / n
    median = statistics.median(quotes)
    if n > 1:
        var = sum((q - mean) ** 2 for q in quotes) / (n - 1)
        std = var ** 0.5
    else:
        std = 0.0
    return min(quotes), mean, median, std
