"""Unit tests for supplycm.forecasting algorithms."""
import unittest
from supplycm.forecasting import (
    simple_moving_average,
    weighted_moving_average,
    single_exponential_smoothing,
    holt_linear_trend,
    naive_forecast,
    seasonal_naive_forecast,
    drift_method,
    average_method,
    crostons_method,
    sba_method,
    tsb_method,
    linear_regression_forecast,
    exponential_trend_forecast,
    theils_u,
    tracking_signal,
    brier_score,
    autocorrelation,
    partial_autocorrelation,
    ar_model,
    theta_method,
    box_cox_transform,
    inverse_box_cox,
    hurst_exponent,
    seasonal_indices,
    moving_median_filter,
)


class TestSimpleMovingAverage(unittest.TestCase):
    def test_basic(self):
        result = simple_moving_average([10, 20, 30, 40], 2)
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], 15.0)
        self.assertEqual(result[2], 25.0)

    def test_window_larger_than_data(self):
        result = simple_moving_average([10, 20], 5)
        self.assertTrue(all(x is None for x in result))

    def test_invalid_window(self):
        with self.assertRaises(ValueError):
            simple_moving_average([10, 20], 0)


class TestWeightedMovingAverage(unittest.TestCase):
    def test_basic(self):
        result = weighted_moving_average([10, 20, 30, 40], [1, 2, 3])
        self.assertIsNotNone(result[2])


class TestSingleExponentialSmoothing(unittest.TestCase):
    def test_basic(self):
        result = single_exponential_smoothing([10, 20, 30], 0.5)
        self.assertEqual(result[0], 10.0)
        self.assertAlmostEqual(result[1], 15.0)
        self.assertAlmostEqual(result[2], 22.5)

    def test_invalid_alpha(self):
        with self.assertRaises(ValueError):
            single_exponential_smoothing([10, 20], 1.5)

    def test_empty_data(self):
        result = single_exponential_smoothing([], 0.3)
        self.assertEqual(result, [])


class TestHoltLinearTrend(unittest.TestCase):
    def test_basic(self):
        level, trend = holt_linear_trend([1, 2, 3, 4])
        self.assertEqual(len(level), 4)
        self.assertEqual(len(trend), 4)

    def test_insufficient_data(self):
        with self.assertRaises(ValueError):
            holt_linear_trend([1])


class TestNaiveForecast(unittest.TestCase):
    def test_basic(self):
        result = naive_forecast([1, 2, 3, 4])
        self.assertEqual(result[0], None)
        self.assertEqual(result[1], 1.0)
        self.assertEqual(result[2], 2.0)

    def test_empty(self):
        result = naive_forecast([])
        self.assertEqual(result, [])


class TestSeasonalNaiveForecast(unittest.TestCase):
    def test_basic(self):
        result = seasonal_naive_forecast([10, 20, 30, 40, 50, 60], 4)
        self.assertEqual(result[0], None)
        self.assertEqual(result[4], 10.0)
        self.assertEqual(result[5], 20.0)


class TestDriftMethod(unittest.TestCase):
    def test_basic(self):
        result = drift_method([10, 20, 30], horizon=2)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 40.0)
        self.assertAlmostEqual(result[1], 50.0)


class TestAverageMethod(unittest.TestCase):
    def test_basic(self):
        result = average_method([10, 20, 30], horizon=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 20.0)


class TestCrostonMethod(unittest.TestCase):
    def test_intermittent_demand(self):
        z, p = crostons_method([0, 10, 0, 0, 20, 0, 5])
        self.assertEqual(len(z), 7)
        self.assertEqual(len(p), 7)


class TestSBAMethod(unittest.TestCase):
    def test_basic(self):
        result = sba_method([0, 10, 0, 0, 20, 0, 5])
        self.assertEqual(len(result), 7)


class TestTSBMethod(unittest.TestCase):
    def test_basic(self):
        result = tsb_method([0, 10, 0, 0, 20, 0, 5])
        self.assertEqual(len(result), 7)


class TestLinearRegressionForecast(unittest.TestCase):
    def test_perfect_fit(self):
        a, b, f = linear_regression_forecast([1, 2, 3, 4], horizon=2)
        self.assertAlmostEqual(a, 1.0)
        self.assertAlmostEqual(b, 1.0)
        self.assertEqual(len(f), 2)


class TestExponentialTrendForecast(unittest.TestCase):
    def test_basic(self):
        a, b, f = exponential_trend_forecast([1, 2, 4, 8], horizon=1)
        self.assertAlmostEqual(b, 2.0)
        self.assertAlmostEqual(f[0], 16.0, places=2)


class TestTheilsU(unittest.TestCase):
    def test_perfect_forecast(self):
        result = theils_u([10, 20, 30], [10, 20, 30])
        self.assertAlmostEqual(result, 0.0)

    def test_bad_forecast(self):
        result = theils_u([10, 20, 30], [100, 200, 300])
        self.assertGreater(result, 1.0)


class TestTrackingSignal(unittest.TestCase):
    def test_balanced_forecast(self):
        result = tracking_signal([10, 20, 30], [12, 18, 30])
        self.assertEqual(len(result), 3)


class TestBrierScore(unittest.TestCase):
    def test_perfect_forecast(self):
        result = brier_score([1.0, 0.0, 1.0], [1, 0, 1])
        self.assertAlmostEqual(result, 0.0)

    def test_worst_forecast(self):
        result = brier_score([0.0, 1.0], [1, 0])
        self.assertAlmostEqual(result, 1.0)


class TestAutocorrelation(unittest.TestCase):
    def test_lag_zero(self):
        result = autocorrelation([1, 2, 3, 4, 5, 6, 7, 8], 3)
        self.assertAlmostEqual(result[0], 1.0)


class TestPartialAutocorrelation(unittest.TestCase):
    def test_basic(self):
        result = partial_autocorrelation([1, 2, 3, 4, 5, 6, 7, 8], 3)
        self.assertAlmostEqual(result[0], 1.0)


class TestARModel(unittest.TestCase):
    def test_ar1(self):
        phi, mu = ar_model([1, 2, 3, 4, 5, 6, 7, 8], order=1)
        self.assertAlmostEqual(phi[0], 0.625, places=2)


class TestThetaMethod(unittest.TestCase):
    def test_basic(self):
        result = theta_method([1, 2, 3, 4, 5], theta=2.0, horizon=2)
        self.assertEqual(len(result), 2)


class TestBoxCoxTransform(unittest.TestCase):
    def test_log_transform(self):
        import math
        result = box_cox_transform([1.0, math.e, math.e**2], 0.0)
        self.assertAlmostEqual(result[1], 1.0)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            box_cox_transform([-1, 0, 1], 0.5)


class TestInverseBoxCox(unittest.TestCase):
    def test_log_inverse(self):
        result = inverse_box_cox([0.0, 1.0], 0.0)
        self.assertAlmostEqual(result[1], 2.7183, places=3)


class TestHurstExponent(unittest.TestCase):
    def test_trending_series(self):
        result = hurst_exponent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 1.0)


class TestSeasonalIndices(unittest.TestCase):
    def test_basic(self):
        result = seasonal_indices([10, 20, 30, 40, 12, 22, 32, 42], 4)
        self.assertEqual(len(result), 4)


class TestMovingMedianFilter(unittest.TestCase):
    def test_outlier_removal(self):
        result = moving_median_filter([1, 2, 100, 4, 5], 3)
        self.assertEqual(result[2], 4.0)


if __name__ == '__main__':
    unittest.main()
