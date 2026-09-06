"""Unit tests for supplycm.routing algorithms."""
import unittest
from supplycm.routing import (
    tsp_nearest_neighbor,
    tsp_two_opt,
    tsp_held_karp,
    vrp_sweep,
    vrp_savings,
    vrp_capacitated_greedy,
    assignment_problem_hungarian,
    northwest_corner_method,
    vogels_approximation,
    least_cost_method,
    vehicle_scheduling,
)


class TestTSPNearestNeighbor(unittest.TestCase):
    def test_three_cities(self):
        route, dist = tsp_nearest_neighbor([[0, 1, 2], [1, 0, 3], [2, 3, 0]])
        self.assertEqual(len(route), 4)
        self.assertEqual(route[0], route[-1])
        self.assertGreater(dist, 0)

    def test_empty(self):
        route, dist = tsp_nearest_neighbor([])
        self.assertEqual(route, [])


class TestTSPTwoOpt(unittest.TestCase):
    def test_four_cities(self):
        route, dist = tsp_two_opt([[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 6], [3, 5, 6, 0]])
        self.assertEqual(len(route), 5)
        self.assertGreater(dist, 0)


class TestTSPHeldKarp(unittest.TestCase):
    def test_three_cities(self):
        route, dist = tsp_held_karp([[0, 1, 2], [1, 0, 3], [2, 3, 0]])
        self.assertAlmostEqual(dist, 6.0)

    def test_too_many_cities_raises(self):
        with self.assertRaises(ValueError):
            tsp_held_karp([[0] * 20 for _ in range(20)])


class TestVRPSweep(unittest.TestCase):
    def test_basic(self):
        customers = [(1, 0, 1), (0, 1, 1), (-1, 0, 1), (0, -1, 1)]
        routes = vrp_sweep(customers, (0, 0), 2)
        self.assertGreater(len(routes), 0)
        total = sum(len(r) for r in routes)
        self.assertEqual(total, 4)


class TestVRPSavings(unittest.TestCase):
    def test_basic(self):
        distances = [[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 6], [3, 5, 6, 0]]
        demands = [0, 1, 1, 1]
        routes = vrp_savings(distances, demands, 3)
        self.assertGreater(len(routes), 0)


class TestVRPCapacitatedGreedy(unittest.TestCase):
    def test_basic(self):
        distances = [[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 6], [3, 5, 6, 0]]
        demands = [0, 1, 1, 1]
        routes = vrp_capacitated_greedy(distances, demands, 2)
        self.assertGreater(len(routes), 0)


class TestAssignmentProblemHungarian(unittest.TestCase):
    def test_basic(self):
        assign, cost = assignment_problem_hungarian([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
        self.assertEqual(len(assign), 3)
        self.assertAlmostEqual(cost, 5.0)


class TestNorthwestCorner(unittest.TestCase):
    def test_basic(self):
        alloc = northwest_corner_method([20, 30], [10, 20, 20])
        total = sum(sum(row) for row in alloc)
        self.assertAlmostEqual(total, 50.0)


class TestVogelsApproximation(unittest.TestCase):
    def test_basic(self):
        alloc = vogels_approximation([20, 30], [10, 20, 20], [[2, 3, 4], [3, 2, 1]])
        total = sum(sum(row) for row in alloc)
        self.assertAlmostEqual(total, 50.0)


class TestLeastCostMethod(unittest.TestCase):
    def test_basic(self):
        alloc = least_cost_method([20, 30], [10, 20, 20], [[2, 3, 4], [3, 2, 1]])
        total = sum(sum(row) for row in alloc)
        self.assertAlmostEqual(total, 50.0)


class TestVehicleScheduling(unittest.TestCase):
    def test_non_overlapping(self):
        result = vehicle_scheduling([(1, 3), (4, 6)])
        self.assertEqual(result, 1)

    def test_overlapping(self):
        result = vehicle_scheduling([(1, 5), (3, 7), (5, 9)])
        self.assertGreaterEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
