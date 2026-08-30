"""Edge case tests for supplycm algorithms.

Tests boundary conditions, empty inputs, and extreme values.
"""
import unittest
from supplycm.forecasting import (
    simple_moving_average, single_exponential_smoothing, naive_forecast,
    linear_regression_forecast, holt_winters,
)
from supplycm.inventory import (
    economic_order_quantity, abc_analysis, safety_stock_normal,
)


class TestForecastingEdgeCases(unittest.TestCase):
    def test_empty_data_sma(self):
        result = simple_moving_average([], 3)
        self.assertEqual(result, [])

    def test_single_point_sma(self):
        result = simple_moving_average([10], 3)
        self.assertEqual(result, [None])

    def test_empty_data_ses(self):
        result = single_exponential_smoothing([], 0.3)
        self.assertEqual(result, [])

    def test_single_point_ses(self):
        result = single_exponential_smoothing([10], 0.3)
        self.assertEqual(result, [10.0])

    def test_empty_naive(self):
        result = naive_forecast([])
        self.assertEqual(result, [])

    def test_single_point_naive(self):
        result = naive_forecast([10])
        self.assertEqual(result, [None])

    def test_linear_regression_two_points(self):
        a, b, f = linear_regression_forecast([1, 2], horizon=1)
        self.assertAlmostEqual(b, 1.0)

    def test_linear_regression_single_point_raises(self):
        with self.assertRaises(ValueError):
            linear_regression_forecast([1])

    def test_holt_winters_insufficient_data(self):
        with self.assertRaises(ValueError):
            holt_winters([10, 20], season_length=4)

    def test_holt_winters_zero_alpha_raises(self):
        with self.assertRaises(ValueError):
            holt_winters([10]*8, alpha=0, beta=0.1, gamma=0.1, season_length=4)


class TestInventoryEdgeCases(unittest.TestCase):
    def test_eoq_zero_demand(self):
        with self.assertRaises(ValueError):
            economic_order_quantity(0, 100, 5)

    def test_eoq_negative_ordering_cost(self):
        with self.assertRaises(ValueError):
            economic_order_quantity(1000, -100, 5)

    def test_eoq_zero_holding_cost(self):
        with self.assertRaises(ValueError):
            economic_order_quantity(1000, 100, 0)

    def test_abc_empty_list(self):
        result = abc_analysis([])
        self.assertEqual(result, [])

    def test_abc_single_item(self):
        result = abc_analysis([('a', 100)])
        self.assertEqual(len(result), 1)

    def test_safety_stock_zero_std(self):
        result = safety_stock_normal(1.96, 0, 4)
        self.assertEqual(result, 0)

    def test_safety_stock_zero_lead_time(self):
        result = safety_stock_normal(1.96, 10, 0)
        self.assertEqual(result, 0)


class TestNumericalStability(unittest.TestCase):
    def test_very_large_numbers(self):
        result = economic_order_quantity(1e12, 1e6, 1e6)
        self.assertGreater(result, 0)
        self.assertFalse(float('inf') == result)

    def test_very_small_numbers(self):
        result = economic_order_quantity(0.001, 0.001, 0.001)
        self.assertGreater(result, 0)

    def test_constant_series(self):
        result = single_exponential_smoothing([50, 50, 50, 50], 0.3)
        for val in result:
            self.assertAlmostEqual(val, 50.0)


if __name__ == '__main__':
    unittest.main()
