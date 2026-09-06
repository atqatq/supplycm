"""Bidirectional BFS."""
from typing import Dict, List
from collections import deque


def bidirectional_search(graph: Dict[int, List[int]], source: int, target: int) -> List[int]:
    """Bidirectional BFS shortest path.

    Example:
        >>> bidirectional_search({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}, 0, 3)
        [0, 1, 2, 3]
    """
    if source == target:
        return [source]
    front_visited = {source: None}
    back_visited = {target: None}
    front_q = deque([source])
    back_q = deque([target])
    meeting = None
    while front_q and back_q:
        # Expand front
        u = front_q.popleft()
        for v in graph.get(u, []):
            if v not in front_visited:
                front_visited[v] = u
                front_q.append(v)
                if v in back_visited:
                    meeting = v
                    break
        if meeting:
            break
        # Expand back
        u = back_q.popleft()
        for v in graph.get(u, []):
            if v not in back_visited:
                back_visited[v] = u
                back_q.append(v)
                if v in front_visited:
                    meeting = v
                    break
        if meeting:
            break
    if meeting is None:
        return []
    # Reconstruct
    front_path = []
    node = meeting
    while node is not None:
        front_path.append(node)
        node = front_visited[node]
    front_path.reverse()
    back_path = []
    node = back_visited[meeting]
    while node is not None:
        back_path.append(node)
        node = back_visited[node]
    return front_path + back_path
