"""Unit tests for supplycm.statistics algorithms."""
import unittest
from supplycm.statistics import (
    mape, smape, rmse, mse, mae, mase, r_squared, adjusted_r_squared,
    bias, mean_percentage_error, tracking_signal_threshold,
    forecast_value_added, percent_bias, coefficient_of_variation,
    confidence_interval_mean, descriptive_stats, correlation,
    spearman_correlation, outlier_detection_iqr, zscore, minmax_scale,
    moving_average_smooth, exponential_smooth, diebold_mariano_test,
    kurtosis, skewness, jarque_bera_test, chi_square_goodness_of_fit,
    t_test_one_sample, t_test_two_sample, f_test_variance, anova_one_way,
    mann_whitney_u, wilcoxon_signed_rank, kolmogorov_smirnov_two_sample,
    bootstrap_confidence_interval,
)


class TestMAPE(unittest.TestCase):
    def test_perfect_forecast(self):
        result = mape([100, 200, 300], [100, 200, 300])
        self.assertAlmostEqual(result, 0.0)

    def test_known_error(self):
        result = mape([100, 200, 300], [110, 190, 310])
        self.assertGreater(result, 0)


class TestSMAPE(unittest.TestCase):
    def test_perfect_forecast(self):
        result = smape([100, 200], [100, 200])
        self.assertAlmostEqual(result, 0.0)


class TestRMSE(unittest.TestCase):
    def test_perfect_forecast(self):
        result = rmse([1, 2, 3], [1, 2, 3])
        self.assertAlmostEqual(result, 0.0)

    def test_known_value(self):
        result = rmse([1, 2, 3], [1, 2, 4])
        self.assertAlmostEqual(result, 0.5774, places=3)


class TestMSE(unittest.TestCase):
    def test_perfect_forecast(self):
        result = mse([1, 2, 3], [1, 2, 3])
        self.assertAlmostEqual(result, 0.0)


class TestMAE(unittest.TestCase):
    def test_perfect_forecast(self):
        result = mae([1, 2, 3], [1, 2, 3])
        self.assertAlmostEqual(result, 0.0)


class TestMASE(unittest.TestCase):
    def test_basic(self):
        result = mase([10, 20, 30, 40, 50], [11, 19, 32, 41, 49])
        self.assertGreaterEqual(result, 0)


class TestRSquared(unittest.TestCase):
    def test_perfect_fit(self):
        result = r_squared([1, 2, 3, 4], [1, 2, 3, 4])
        self.assertAlmostEqual(result, 1.0)


class TestAdjustedRSquared(unittest.TestCase):
    def test_basic(self):
        result = adjusted_r_squared(0.9, 100, 5)
        self.assertAlmostEqual(result, 0.8947, places=3)


class TestBias(unittest.TestCase):
    def test_zero_bias(self):
        result = bias([10, 20, 30], [10, 20, 30])
        self.assertAlmostEqual(result, 0.0)


class TestMeanPercentageError(unittest.TestCase):
    def test_zero_error(self):
        result = mean_percentage_error([100, 200], [100, 200])
        self.assertAlmostEqual(result, 0.0)


class TestTrackingSignalThreshold(unittest.TestCase):
    def test_in_control(self):
        self.assertFalse(tracking_signal_threshold(2.0))

    def test_out_of_control(self):
        self.assertTrue(tracking_signal_threshold(5.0))


class TestForecastValueAdded(unittest.TestCase):
    def test_positive_fva(self):
        result = forecast_value_added([10, 20, 30], [11, 19, 30], [10, 10, 10])
        self.assertGreater(result, 0)


class TestPercentBias(unittest.TestCase):
    def test_zero_bias(self):
        result = percent_bias([10, 20, 30], [10, 20, 30])
        self.assertAlmostEqual(result, 0.0)


class TestCoefficientOfVariation(unittest.TestCase):
    def test_basic(self):
        result = coefficient_of_variation([10, 20, 30])
        self.assertAlmostEqual(result, 0.4082, places=3)


class TestConfidenceInterval(unittest.TestCase):
    def test_contains_mean(self):
        lo, hi = confidence_interval_mean([10, 20, 30, 40, 50])
        self.assertLess(lo, 30)
        self.assertGreater(hi, 30)


class TestDescriptiveStats(unittest.TestCase):
    def test_basic(self):
        stats = descriptive_stats([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(stats['mean'], 5.5)
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 10)
        self.assertEqual(stats['count'], 10)


class TestCorrelation(unittest.TestCase):
    def test_perfect_positive(self):
        result = correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        self.assertAlmostEqual(result, 1.0)

    def test_perfect_negative(self):
        result = correlation([1, 2, 3, 4, 5], [10, 8, 6, 4, 2])
        self.assertAlmostEqual(result, -1.0)


class TestSpearmanCorrelation(unittest.TestCase):
    def test_perfect(self):
        result = spearman_correlation([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
        self.assertAlmostEqual(result, 1.0)


class TestOutlierDetectionIQR(unittest.TestCase):
    def test_finds_outlier(self):
        lower, upper = outlier_detection_iqr([1, 2, 3, 4, 100])
        self.assertIn(100, upper)


class TestZScore(unittest.TestCase):
    def test_standardized(self):
        result = zscore([1, 2, 3, 4, 5])
        self.assertAlmostEqual(sum(result) / len(result), 0.0, places=5)


class TestMinMaxScale(unittest.TestCase):
    def test_basic(self):
        result = minmax_scale([1, 2, 3, 4, 5])
        self.assertEqual(result[0], 0.0)
        self.assertEqual(result[-1], 1.0)


class TestMovingAverageSmooth(unittest.TestCase):
    def test_basic(self):
        result = moving_average_smooth([1, 2, 3, 4, 5], 3)
        self.assertEqual(len(result), 5)


class TestExponentialSmooth(unittest.TestCase):
    def test_basic(self):
        result = exponential_smooth([10, 20, 30], 0.5)
        self.assertAlmostEqual(result[1], 15.0)


class TestDieboldMariano(unittest.TestCase):
    def test_basic(self):
        result = diebold_mariano_test([10, 20, 30, 40], [11, 19, 31, 39], [12, 18, 32, 38])
        self.assertIsInstance(result, float)


class TestKurtosis(unittest.TestCase):
    def test_basic(self):
        result = kurtosis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertIsInstance(result, float)


class TestSkewness(unittest.TestCase):
    def test_positive_skew(self):
        result = skewness([1, 2, 2, 3, 4, 100])
        self.assertGreater(result, 0)


class TestJarqueBera(unittest.TestCase):
    def test_basic(self):
        result = jarque_bera_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertGreaterEqual(result, 0)


class TestChiSquare(unittest.TestCase):
    def test_basic(self):
        result = chi_square_goodness_of_fit([10, 20, 30], [15, 15, 30])
        self.assertGreater(result, 0)


class TestTTestOneSample(unittest.TestCase):
    def test_basic(self):
        result = t_test_one_sample([10, 20, 30, 40, 50], 25)
        self.assertIsInstance(result, float)


class TestTTestTwoSample(unittest.TestCase):
    def test_basic(self):
        result = t_test_two_sample([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        self.assertIsInstance(result, float)


class TestFTestVariance(unittest.TestCase):
    def test_basic(self):
        result = f_test_variance([1, 2, 3, 4, 5], [1, 2, 3, 4, 6])
        self.assertGreater(result, 0)


class TestANOVA(unittest.TestCase):
    def test_basic(self):
        result = anova_one_way([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertGreater(result, 0)


class TestMannWhitneyU(unittest.TestCase):
    def test_separated_groups(self):
        u1, u2 = mann_whitney_u([1, 2, 3], [4, 5, 6])
        self.assertEqual(u1, 0)
        self.assertEqual(u2, 9)


class TestWilcoxonSignedRank(unittest.TestCase):
    def test_basic(self):
        result = wilcoxon_signed_rank([1, -2, 3, -4, 5])
        self.assertGreater(result, 0)


class TestKSTwoSample(unittest.TestCase):
    def test_identical_distributions(self):
        result = kolmogorov_smirnov_two_sample([1, 2, 3], [1, 2, 3])
        self.assertAlmostEqual(result, 0.0)


class TestBootstrapCI(unittest.TestCase):
    def test_contains_mean(self):
        lo, hi = bootstrap_confidence_interval([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertLess(lo, 5.5)
        self.assertGreater(hi, 5.5)


if __name__ == '__main__':
    unittest.main()
