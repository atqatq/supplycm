"""Connected components of undirected graph."""
from typing import Dict, List


def connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Return list of connected components.

    Example:
        >>> connected_components({0: [1], 1: [0], 2: [3], 3: [2], 4: []})
    """
    visited = set()
    components = []
    for node in graph:
        if node in visited:
            continue
        component = []
        stack = [node]
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            component.append(n)
            stack.extend(graph.get(n, []))
        components.append(component)
    return components
