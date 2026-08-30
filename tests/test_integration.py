"""Integration tests for supplycm.

Tests end-to-end workflows that combine multiple algorithms
across different modules.
"""
import unittest
from supplycm.forecasting import single_exponential_smoothing, simple_moving_average
from supplycm.inventory import economic_order_quantity, safety_stock_normal, reorder_point
from supplycm.statistics import mape, rmse
from supplycm.routing import tsp_nearest_neighbor
from supplycm.optimization import knapsack_01_dp
from supplycm.supplier import topsis, ahp_supplier_selection


class TestForecastToInventoryWorkflow(unittest.TestCase):
    """Test forecasting demand then computing inventory parameters."""

    def test_forecast_then_eoq(self):
        # Step 1: Forecast demand
        historical = [100, 110, 105, 115, 120, 125, 130, 128, 135, 140]
        forecast = single_exponential_smoothing(historical, alpha=0.3)
        annual_demand = forecast[-1] * 12

        # Step 2: Compute EOQ based on forecast
        eoq = economic_order_quantity(annual_demand, 100, 5)
        self.assertGreater(eoq, 0)

    def test_forecast_accuracy_then_reorder(self):
        # Step 1: Generate forecast
        actual = [100, 120, 115, 130, 125]
        forecast = simple_moving_average(actual, 3)

        # Step 2: Measure accuracy
        valid_actual = actual[2:]
        valid_forecast = [f for f in forecast[2:] if f is not None]
        error = mape(valid_actual, valid_forecast)
        self.assertGreaterEqual(error, 0)

        # Step 3: Compute reorder point
        ss = safety_stock_normal(1.96, 10, 2)
        rop = reorder_point(120, 2, ss)
        self.assertGreater(rop, 200)


class TestSupplierSelectionWorkflow(unittest.TestCase):
    """Test multi-criteria supplier selection."""

    def test_ahp_then_topsis(self):
        # Step 1: Get criteria weights from AHP
        pairwise = [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]]
        weights = ahp_supplier_selection(pairwise)
        self.assertAlmostEqual(sum(weights), 1.0, places=1)

        # Step 2: Rank suppliers using TOPSIS
        decision_matrix = [[80, 90, 85], [70, 85, 90], [85, 80, 70]]
        ranking = topsis(decision_matrix, weights,
                        ['benefit', 'benefit', 'benefit'])
        self.assertEqual(len(ranking), 3)
        self.assertEqual(len(set(ranking)), 3)


class TestRoutingOptimizationWorkflow(unittest.TestCase):
    """Test route optimization pipeline."""

    def test_tsp_then_knapsack(self):
        # Step 1: Solve TSP for delivery route
        distances = [[0, 10, 20, 30], [10, 0, 15, 25],
                     [20, 15, 0, 12], [30, 25, 12, 0]]
        route, total_dist = tsp_nearest_neighbor(distances)
        self.assertEqual(len(route), 5)

        # Step 2: Select items to load using knapsack
        weights = [5, 10, 15, 20]
        values = [10, 30, 40, 50]
        val, items = knapsack_01_dp(weights, values, 30)
        self.assertGreater(val, 0)


class TestForecastAccuracyWorkflow(unittest.TestCase):
    """Test forecast generation and accuracy evaluation."""

    def test_multiple_metrics(self):
        actual = [100, 200, 300, 400, 500]
        forecast = [110, 190, 310, 395, 505]

        mape_val = mape(actual, forecast)
        rmse_val = rmse(actual, forecast)

        self.assertGreater(mape_val, 0)
        self.assertGreater(rmse_val, 0)
        self.assertLess(mape_val, 10)  # Less than 10% error


if __name__ == '__main__':
    unittest.main()
