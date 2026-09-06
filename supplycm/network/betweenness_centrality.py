"""Betweenness centrality (simplified)."""
from typing import Dict, List
from collections import deque


def betweenness_centrality(graph: Dict[int, List[int]], nodes: List[int]) -> Dict[int, float]:
    """Compute betweenness centrality for each node.

    Example:
        >>> g = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}
        >>> bc = betweenness_centrality(g, [0, 1, 2, 3])
        >>> bc[1] > 0
        True
    """
    bc = {n: 0.0 for n in nodes}
    for s in nodes:
        # BFS from s
        dist = {s: 0}
        sigma = {s: 1}
        pred = {n: [] for n in nodes}
        q = deque([s])
        S = []
        while q:
            v = q.popleft()
            S.append(v)
            for w in graph.get(v, []):
                if w not in dist:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] = sigma.get(w, 0) + sigma.get(v, 0)
                    pred[w].append(v)
        delta = {n: 0.0 for n in nodes}
        while S:
            w = S.pop()
            for v in pred[w]:
                delta[v] += (sigma.get(v, 0) / sigma.get(w, 1)) * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    # Normalize undirected
    for n in bc:
        bc[n] /= 2.0
    return bc
