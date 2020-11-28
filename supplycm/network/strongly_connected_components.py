"""Tarjan's strongly connected components."""
from typing import Dict, List


def strongly_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Find SCCs using Tarjan's algorithm.

    Example:
        >>> sccs = strongly_connected_components({0: [1], 1: [2], 2: [0, 3], 3: []})
        >>> any(0 in s for s in sccs)
        True
    """
    index_counter = [0]
    stack = []
    lowlink = {}
    index = {}
    on_stack = {}
    result = []
    def strongconnect(v):
        index[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        for w in graph.get(v, []):
            if w not in index:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack.get(w):
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)
    for v in graph:
        if v not in index:
            strongconnect(v)
    return result
