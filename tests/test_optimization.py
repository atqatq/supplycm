"""Unit tests for supplycm.optimization algorithms."""
import unittest
from supplycm.optimization import (
    simplex_method, branch_and_bound, genetic_algorithm,
    simulated_annealing, tabu_search, knapsack_01_dp,
    fractional_knapsack, dynamic_programming_lcs, edit_distance,
    convex_hull, merge_sort, quick_sort, binary_search, heap_sort,
    set_cover_greedy, bin_packing_first_fit, bin_packing_best_fit,
    matrix_chain_multiplication, longest_increasing_subsequence,
    golden_section_search, newton_raphson, gradient_descent,
)


class TestSimplexMethod(unittest.TestCase):
    def test_basic(self):
        x, val = simplex_method([3, 5], [[1, 0], [0, 1], [1, 1]], [4, 6, 8])
        self.assertAlmostEqual(val, 36.0, places=0)


class TestBranchAndBound(unittest.TestCase):
    def test_basic(self):
        f = lambda x: x[0] + 2 * x[1]
        best, val = branch_and_bound(f, [0, 0], [5, 5])
        self.assertEqual(val, 15)


class TestGeneticAlgorithm(unittest.TestCase):
    def test_finds_near_optimum(self):
        f = lambda x: -(x[0] - 5) ** 2 - (x[1] - 3) ** 2
        best, fit = genetic_algorithm(f, [(0, 10), (0, 10)], 30, 50)
        self.assertLess(abs(best[0] - 5), 2)


class TestSimulatedAnnealing(unittest.TestCase):
    def test_finds_minimum(self):
        import random
        f = lambda x: (x[0] - 5) ** 2 + (x[1] - 3) ** 2
        neigh = lambda x, r: [x[0] + r.gauss(0, 0.5), x[1] + r.gauss(0, 0.5)]
        best, val = simulated_annealing(f, [0, 0], neigh, 500, 100, 0.95)
        self.assertLess(abs(best[0] - 5), 3)


class TestKnapsack01(unittest.TestCase):
    def test_basic(self):
        val, items = knapsack_01_dp([2, 3, 4], [3, 4, 5], 5)
        self.assertEqual(val, 7)


class TestFractionalKnapsack(unittest.TestCase):
    def test_basic(self):
        val, amounts = fractional_knapsack([2, 3, 4], [3, 4, 5], 5)
        self.assertAlmostEqual(val, 7.0)


class TestLCS(unittest.TestCase):
    def test_basic(self):
        result = dynamic_programming_lcs([1, 2, 3, 4], [2, 3, 5])
        self.assertEqual(result, [2, 3])


class TestEditDistance(unittest.TestCase):
    def test_basic(self):
        result = edit_distance('abc', 'abd')
        self.assertEqual(result, 1)


class TestConvexHull(unittest.TestCase):
    def test_basic(self):
        points = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
        hull = convex_hull(points)
        self.assertGreaterEqual(len(hull), 3)


class TestMergeSort(unittest.TestCase):
    def test_basic(self):
        result = merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])


class TestQuickSort(unittest.TestCase):
    def test_basic(self):
        result = quick_sort([3, 1, 4, 1, 5])
        self.assertEqual(result, [1, 1, 3, 4, 5])


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        result = binary_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 2)

    def test_not_found(self):
        result = binary_search([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)


class TestHeapSort(unittest.TestCase):
    def test_basic(self):
        result = heap_sort([3, 1, 4, 1, 5, 9, 2, 6])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])


class TestSetCoverGreedy(unittest.TestCase):
    def test_basic(self):
        universe = {1, 2, 3, 4, 5}
        subsets = {'A': {1, 2}, 'B': {2, 3, 4}, 'C': {4, 5}}
        result = set_cover_greedy(universe, subsets)
        self.assertLessEqual(len(result), 3)


class TestBinPackingFirstFit(unittest.TestCase):
    def test_basic(self):
        bins = bin_packing_first_fit([2, 5, 4, 7, 1, 3, 8], 10)
        self.assertGreater(len(bins), 0)


class TestBinPackingBestFit(unittest.TestCase):
    def test_basic(self):
        bins = bin_packing_best_fit([2, 5, 4, 7, 1, 3, 8], 10)
        self.assertGreater(len(bins), 0)


class TestMatrixChainMultiplication(unittest.TestCase):
    def test_basic(self):
        result = matrix_chain_multiplication([10, 100, 5, 50])
        self.assertEqual(result, 7500)


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_basic(self):
        result = longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        self.assertEqual(result, 4)


class TestGoldenSectionSearch(unittest.TestCase):
    def test_finds_minimum(self):
        f = lambda x: (x - 2) ** 2
        result = golden_section_search(f, 0, 5)
        self.assertAlmostEqual(result, 2.0, places=3)


class TestNewtonRaphson(unittest.TestCase):
    def test_finds_root(self):
        result = newton_raphson(lambda x: x**2 - 4, lambda x: 2*x, 3.0)
        self.assertAlmostEqual(result, 2.0, places=3)


class TestGradientDescent(unittest.TestCase):
    def test_finds_minimum(self):
        f = lambda x: (x[0] - 3) ** 2 + (x[1] - 1) ** 2
        best, val = gradient_descent(f, [0.0, 0.0], 0.1, 100)
        self.assertLess(abs(best[0] - 3), 1)


if __name__ == '__main__':
    unittest.main()
