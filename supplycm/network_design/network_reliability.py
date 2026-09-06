"""Network reliability calculation for supply chain networks."""
from typing import Dict, List


def network_reliability(node_reliabilities: Dict[int, float],
                         edges: List[tuple]) -> float:
    """Compute approximate network reliability (series-parallel).

    Args:
        node_reliabilities: Dict node -> reliability (0 to 1).
        edges: List of (node1, node2) tuples.

    Returns:
        Overall network reliability estimate.

    Example:
        >>> round(network_reliability({0: 0.9, 1: 0.95, 2: 0.85},
        ...     [(0, 1), (1, 2)]), 4)
        0.7268
    """
    # For a series network, multiply all reliabilities
    reliability = 1.0
    for node, rel in node_reliabilities.items():
        if rel < 0 or rel > 1:
            raise ValueError("reliability must be in [0, 1]")
        reliability *= rel
    return reliability
