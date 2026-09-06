"""Unit tests for supplycm.network algorithms."""
import unittest
from supplycm.network import (
    dijkstra_shortest_path,
    bellman_ford,
    floyd_warshall,
    kruskal_mst,
    prim_mst,
    ford_fulkerson_max_flow,
    edmonds_karp_max_flow,
    bipartite_matching,
    topological_sort,
    strongly_connected_components,
    bfs_shortest_path,
    dfs_traversal,
    connected_components,
    page_rank,
    degree_centrality,
    eigenvector_centrality,
    a_star_search,
)


class TestDijkstra(unittest.TestCase):
    def test_basic(self):
        graph = {0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}
        dist, prev = dijkstra_shortest_path(graph, 0)
        self.assertEqual(dist[0], 0.0)
        self.assertEqual(dist[1], 1.0)
        self.assertEqual(dist[2], 3.0)


class TestBellmanFord(unittest.TestCase):
    def test_basic(self):
        graph = {0: [(1, 1)], 1: [(2, 2)], 2: []}
        dist, neg_cycle = bellman_ford(graph, 0, 3)
        self.assertFalse(neg_cycle)
        self.assertEqual(dist[0], 0.0)
        self.assertEqual(dist[2], 3.0)


class TestFloydWarshall(unittest.TestCase):
    def test_basic(self):
        dist = floyd_warshall([[0, 3, 999], [3, 0, 1], [999, 1, 0]])
        self.assertEqual(dist[0][2], 4)


class TestKruskalMST(unittest.TestCase):
    def test_basic(self):
        edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 4), (1, 3, 5)]
        mst, total = kruskal_mst(4, edges)
        self.assertEqual(total, 6)
        self.assertEqual(len(mst), 3)


class TestPrimMST(unittest.TestCase):
    def test_basic(self):
        graph = {0: [(1, 1), (2, 4)], 1: [(0, 1), (2, 2)], 2: [(0, 4), (1, 2)]}
        mst, total = prim_mst(graph, 0)
        self.assertEqual(total, 3)


class TestFordFulkerson(unittest.TestCase):
    def test_basic(self):
        cap = [[0, 3, 0, 2], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        result = ford_fulkerson_max_flow(cap, 0, 3)
        self.assertAlmostEqual(result, 4.0)


class TestEdmondsKarp(unittest.TestCase):
    def test_basic(self):
        cap = [[0, 3, 0, 2], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        result = edmonds_karp_max_flow(cap, 0, 3)
        self.assertAlmostEqual(result, 4.0)


class TestBipartiteMatching(unittest.TestCase):
    def test_basic(self):
        graph = {1: [4, 5], 2: [4], 3: [5]}
        matching = bipartite_matching(graph, [1, 2, 3])
        self.assertGreaterEqual(len(matching), 2)


class TestTopologicalSort(unittest.TestCase):
    def test_basic(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort(graph)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 3)


class TestStronglyConnectedComponents(unittest.TestCase):
    def test_basic(self):
        graph = {0: [1], 1: [2], 2: [0, 3], 3: []}
        sccs = strongly_connected_components(graph)
        self.assertGreater(len(sccs), 0)


class TestBFS(unittest.TestCase):
    def test_shortest_path(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        path = bfs_shortest_path(graph, 0, 3)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 3)


class TestDFS(unittest.TestCase):
    def test_basic(self):
        graph = {0: [1, 2], 1: [3], 2: [], 3: []}
        result = dfs_traversal(graph, 0)
        self.assertEqual(result[0], 0)
        self.assertEqual(len(result), 4)


class TestConnectedComponents(unittest.TestCase):
    def test_basic(self):
        graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
        components = connected_components(graph)
        self.assertEqual(len(components), 3)


class TestPageRank(unittest.TestCase):
    def test_sums_to_one(self):
        graph = {0: [1], 1: [0, 2], 2: [0]}
        pr = page_rank(graph, 3)
        self.assertAlmostEqual(sum(pr.values()), 1.0, places=2)


class TestDegreeCentrality(unittest.TestCase):
    def test_basic(self):
        graph = {0: [1, 2], 1: [0], 2: [0]}
        dc = degree_centrality(graph, 3)
        self.assertEqual(dc[0], 1.0)


class TestEigenvectorCentrality(unittest.TestCase):
    def test_basic(self):
        graph = {0: [1, 2], 1: [0], 2: [0]}
        ec = eigenvector_centrality(graph, [0, 1, 2])
        self.assertGreater(ec[0], 0)


class TestAStar(unittest.TestCase):
    def test_basic(self):
        graph = {0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}
        path, cost = a_star_search(graph, 0, 2, lambda n: 0)
        self.assertEqual(cost, 3)


if __name__ == '__main__':
    unittest.main()
