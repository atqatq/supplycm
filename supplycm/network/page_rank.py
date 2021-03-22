"""PageRank centrality."""
from typing import Dict, List


def page_rank(graph: Dict[int, List[int]], num_nodes: int,
              damping: float = 0.85, iterations: int = 100,
              tol: float = 1e-6) -> Dict[int, float]:
    """Compute PageRank for each node.

    Example:
        >>> pr = page_rank({0: [1], 1: [0, 2], 2: [0]}, 3)
        >>> abs(sum(pr.values()) - 1.0) < 1e-3
        True
    """
    pr = {i: 1.0 / num_nodes for i in range(num_nodes)}
    for _ in range(iterations):
        new_pr = {i: (1 - damping) / num_nodes for i in range(num_nodes)}
        dangling_sum = 0.0
        for i in range(num_nodes):
            if not graph.get(i):
                dangling_sum += pr[i]
        for u in graph:
            out_degree = len(graph[u])
            if out_degree == 0:
                continue
            for v in graph[u]:
                new_pr[v] += damping * pr[u] / out_degree
        # Distribute dangling
        for i in range(num_nodes):
            new_pr[i] += damping * dangling_sum / num_nodes
        diff = sum(abs(new_pr[i] - pr[i]) for i in range(num_nodes))
        pr = new_pr
        if diff < tol:
            break
    return pr
