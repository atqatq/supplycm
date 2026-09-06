"""Property-based tests for supplycm algorithms.

Tests mathematical properties that should hold for all inputs,
using randomly generated test cases.
"""
import unittest
import random
import math
from supplycm.inventory import (
    economic_order_quantity,
    abc_analysis,
    inventory_turnover_ratio,
    weighted_average_cost,
)
from supplycm.forecasting import (
    simple_moving_average,
    single_exponential_smoothing,
    naive_forecast,
)
from supplycm.statistics import correlation, coefficient_of_variation
from supplycm.optimization import merge_sort, quick_sort, binary_search


class TestEOQProperties(unittest.TestCase):
    """Properties of Economic Order Quantity (EOQ)."""

    def test_eoq_always_positive(self):
        """EOQ should always be positive for valid inputs."""
        rng = random.Random(42)
        for _ in range(100):
            d = rng.uniform(1, 100000)
            s = rng.uniform(1, 1000)
            h = rng.uniform(0.1, 100)
            q = economic_order_quantity(d, s, h)
            self.assertGreater(q, 0)

    def test_eoq_doubles_when_demand_quadruples(self):
        """EOQ scales with square root of demand."""
        q1 = economic_order_quantity(1000, 100, 5)
        q2 = economic_order_quantity(4000, 100, 5)
        self.assertAlmostEqual(q2 / q1, 2.0, places=2)

    def test_eoq_halves_when_holding_cost_quadruples(self):
        """EOQ inversely scales with square root of holding cost."""
        q1 = economic_order_quantity(1000, 100, 5)
        q2 = economic_order_quantity(1000, 100, 20)
        self.assertAlmostEqual(q1 / q2, 2.0, places=2)


class TestABCAnalysisProperties(unittest.TestCase):
    """Properties of ABC analysis."""

    def test_all_items_classified(self):
        """Every item should receive a classification."""
        rng = random.Random(42)
        for _ in range(20):
            n = rng.randint(1, 50)
            items = [(f'item_{i}', rng.uniform(1, 1000)) for i in range(n)]
            result = abc_analysis(items)
            self.assertEqual(len(result), n)

    def test_class_a_has_highest_value(self):
        """Class A items should have higher value than Class C."""
        items = [('a', 1000), ('b', 900), ('c', 100), ('d', 50), ('e', 10)]
        result = abc_analysis(items)
        # Get value of first A item and last C item
        a_vals = [dict(items)[r[0]] for r in result if r[1] == 'A']
        c_vals = [dict(items)[r[0]] for r in result if r[1] == 'C']
        if a_vals and c_vals:
            self.assertGreater(max(a_vals), max(c_vals))


class TestForecastingProperties(unittest.TestCase):
    """Properties of forecasting algorithms."""

    def test_sma_window_equals_data(self):
        """SMA with window equal to data length gives one value."""
        data = [10, 20, 30]
        result = simple_moving_average(data, 3)
        self.assertIsNotNone(result[-1])
        self.assertAlmostEqual(result[-1], 20.0)

    def test_ses_first_value_equals_data(self):
        """SES first forecast equals first data point."""
        rng = random.Random(42)
        for _ in range(50):
            data = [rng.uniform(0, 100) for _ in range(rng.randint(1, 20))]
            result = single_exponential_smoothing(data, 0.3)
            self.assertEqual(result[0], data[0])

    def test_naive_forecast_lags_by_one(self):
        """Naive forecast at time t equals actual at time t-1."""
        data = [10, 20, 30, 40, 50]
        result = naive_forecast(data)
        for i in range(1, len(data)):
            self.assertEqual(result[i], float(data[i - 1]))


class TestSortingProperties(unittest.TestCase):
    """Properties of sorting algorithms."""

    def test_merge_sort_correctness(self):
        """Merge sort should produce sorted output."""
        rng = random.Random(42)
        for _ in range(50):
            data = [rng.randint(-100, 100) for _ in range(rng.randint(0, 50))]
            result = merge_sort(data)
            self.assertEqual(result, sorted(data))

    def test_quick_sort_correctness(self):
        """Quick sort should produce sorted output."""
        rng = random.Random(42)
        for _ in range(50):
            data = [rng.randint(-100, 100) for _ in range(rng.randint(0, 50))]
            result = quick_sort(data)
            self.assertEqual(result, sorted(data))


class TestStatisticsProperties(unittest.TestCase):
    """Properties of statistics algorithms."""

    def test_correlation_range(self):
        """Correlation should be between -1 and 1."""
        rng = random.Random(42)
        for _ in range(50):
            x = [rng.uniform(0, 100) for _ in range(20)]
            y = [rng.uniform(0, 100) for _ in range(20)]
            r = correlation(x, y)
            self.assertGreaterEqual(r, -1.01)
            self.assertLessEqual(r, 1.01)

    def test_cv_positive_for_positive_data(self):
        """Coefficient of Variation (CV) should be positive for positive data."""
        data = [10, 20, 30, 40, 50]
        cv = coefficient_of_variation(data)
        self.assertGreater(cv, 0)


class TestBinarySearchProperties(unittest.TestCase):
    """Properties of binary search."""

    def test_finds_all_elements(self):
        """Binary search should find any element in a sorted list."""
        rng = random.Random(42)
        for _ in range(50):
            data = sorted([rng.randint(0, 100) for _ in range(rng.randint(1, 30))])
            target = rng.choice(data)
            idx = binary_search(data, target)
            self.assertNotEqual(idx, -1)
            self.assertEqual(data[idx], target)


if __name__ == '__main__':
    unittest.main()
