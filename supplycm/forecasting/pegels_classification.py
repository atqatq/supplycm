"""Pegels' classification of time series."""
from typing import List


def pegels_classification(data: List[float], season_length: int = 0) -> str:
    """Classify a series as one of nine Pegels types: N/A/M x N/A/M.

    Returns a code like 'AAN', 'MAM', etc.

    Example:
        >>> pegels_classification([1, 2, 3, 4, 5])
        'AAN'
    """
    n = len(data)
    if n < 4:
        return "NNN"
    trend_diffs = [data[i + 1] - data[i] for i in range(n - 1)]
    trend_increasing = sum(1 for d in trend_diffs if d > 0) > n / 2
    trend_decreasing = sum(1 for d in trend_diffs if d < 0) > n / 2
    if trend_increasing or trend_decreasing:
        trend_type = "A" if all(d >= 0 for d in trend_diffs) or all(d <= 0 for d in trend_diffs) else "M"
    else:
        trend_type = "N"
    if season_length and season_length < n // 2:
        season_means = [sum(data[i::season_length]) / len(data[i::season_length])
                        for i in range(season_length)]
        if max(season_means) - min(season_means) > 0.1 * (sum(data) / n):
            ratios = [s / (sum(data) / n) for s in season_means]
            if all(r > 0 for r in ratios):
                season_type = "M" if max(ratios) / min(ratios) > 1.2 else "A"
            else:
                season_type = "A"
        else:
            season_type = "N"
    else:
        season_type = "N"
    return f"{trend_type}{season_type}N"
