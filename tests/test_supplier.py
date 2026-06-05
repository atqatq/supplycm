"""Unit tests for supplycm.supplier algorithms."""
import unittest
from supplycm.supplier import (
    ahp_supplier_selection, topsis, data_envelopment_analysis,
    weighted_point_method, supplier_risk_score, supplier_segmentation,
    total_cost_of_ownership, should_cost_analysis, price_analysis,
    competitive_bidding, negotiation_zone, supplier_rating,
    vendor_scorecard, on_time_delivery_rate, supplier_consolidation,
    purchase_price_variance, spend_analysis, maverick_spend_detection,
    supplier_diversity_index, preferred_supplier_index,
)


class TestAHP(unittest.TestCase):
    def test_priorities_sum_to_one(self):
        matrix = [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]]
        priorities = ahp_supplier_selection(matrix)
        self.assertAlmostEqual(sum(priorities), 1.0, places=1)


class TestTOPSIS(unittest.TestCase):
    def test_ranking(self):
        ranking = topsis([[3, 5], [4, 4], [2, 6]], [0.5, 0.5],
                        ['benefit', 'benefit'])
        self.assertEqual(len(ranking), 3)
        self.assertEqual(len(set(ranking)), 3)


class TestDataEnvelopmentAnalysis(unittest.TestCase):
    def test_basic(self):
        scores = data_envelopment_analysis([[2, 3], [4, 5]], [[5, 3], [8, 7]])
        self.assertEqual(len(scores), 2)
        for s in scores:
            self.assertGreaterEqual(s, 0)
            self.assertLessEqual(s, 1.01)


class TestWeightedPointMethod(unittest.TestCase):
    def test_basic(self):
        result = weighted_point_method([[80, 90], [70, 85]], [0.6, 0.4])
        self.assertEqual(result[0], 84.0)
        self.assertEqual(result[1], 76.0)


class TestSupplierRiskScore(unittest.TestCase):
    def test_basic(self):
        score = supplier_risk_score({'financial': 30, 'operational': 40},
                                     {'financial': 0.6, 'operational': 0.4})
        self.assertGreater(score, 0)
        self.assertLess(score, 100)


class TestSupplierSegmentation(unittest.TestCase):
    def test_strategic(self):
        result = supplier_segmentation([('A', 0.8, 0.7), ('B', 0.3, 0.3)])
        self.assertEqual(result[0][1], 'Strategic')
        self.assertEqual(result[1][1], 'Routine')


class TestTotalCostOfOwnership(unittest.TestCase):
    def test_basic(self):
        result = total_cost_of_ownership(10000, 500, 5000, 2000)
        self.assertEqual(result, 17500.0)


class TestShouldCostAnalysis(unittest.TestCase):
    def test_basic(self):
        result = should_cost_analysis({'steel': 50, 'plastic': 20}, 2, 30, 1.5, 0.1)
        self.assertAlmostEqual(result, 173.5, places=1)


class TestPriceAnalysis(unittest.TestCase):
    def test_basic(self):
        mn, mean, median, std = price_analysis([100, 110, 105, 95])
        self.assertEqual(mn, 95)
        self.assertGreater(mean, 0)


class TestCompetitiveBidding(unittest.TestCase):
    def test_basic(self):
        winner, score = competitive_bidding([('A', 100, 80), ('B', 110, 95)])
        self.assertIn(winner, ['A', 'B'])


class TestNegotiationZone(unittest.TestCase):
    def test_agreement_possible(self):
        lo, hi, ok = negotiation_zone(100, 80)
        self.assertTrue(ok)
        self.assertLessEqual(lo, hi)


class TestSupplierRating(unittest.TestCase):
    def test_basic(self):
        result = supplier_rating({'quality': 90, 'delivery': 85, 'price': 80},
                                  {'quality': 0.4, 'delivery': 0.3, 'price': 0.3})
        self.assertGreater(result, 0)


class TestVendorScorecard(unittest.TestCase):
    def test_basic(self):
        sc = vendor_scorecard(['A', 'B'], ['quality', 'delivery'],
                              [[90, 85], [80, 95]], [0.6, 0.4])
        self.assertEqual(sc['A']['total'], 88.0)
        self.assertEqual(sc['A']['rank'], 1)


class TestOnTimeDeliveryRate(unittest.TestCase):
    def test_basic(self):
        result = on_time_delivery_rate([(10, 9), (15, 15), (20, 22)])
        self.assertAlmostEqual(result, 2/3, places=2)


class TestSupplierConsolidation(unittest.TestCase):
    def test_basic(self):
        savings, count = supplier_consolidation([100, 200, 300, 400])
        self.assertGreater(savings, 0)
        self.assertGreater(count, 0)


class TestPurchasePriceVariance(unittest.TestCase):
    def test_basic(self):
        result = purchase_price_variance(11, 10, 1000)
        self.assertEqual(result, 1000.0)


class TestSpendAnalysis(unittest.TestCase):
    def test_basic(self):
        result = spend_analysis([('IT', 'A', 100), ('IT', 'B', 200), ('HR', 'A', 50)])
        self.assertEqual(result['IT']['total'], 300)
        self.assertEqual(result['HR']['total'], 50)


class TestMaverickSpendDetection(unittest.TestCase):
    def test_basic(self):
        result = maverick_spend_detection([('a', 'A', 100), ('b', 'X', 200)],
                                           {'A', 'B'})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 200)


class TestSupplierDiversityIndex(unittest.TestCase):
    def test_basic(self):
        result = supplier_diversity_index([100, 100, 100])
        self.assertGreater(result, 0.9)


class TestPreferredSupplierIndex(unittest.TestCase):
    def test_basic(self):
        result = preferred_supplier_index(
            [{'name': 'A', 'quality': 80, 'delivery': 90},
             {'name': 'B', 'quality': 60, 'delivery': 65}],
            {'quality': 0.5, 'delivery': 0.5}, 70)
        self.assertEqual(result, ['A'])


if __name__ == '__main__':
    unittest.main()
