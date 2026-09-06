"""Unit tests for supplycm.inventory algorithms."""
import unittest
import math
from supplycm.inventory import (
    economic_order_quantity,
    economic_production_quantity,
    eoq_with_backorders,
    abc_analysis,
    xyz_analysis,
    safety_stock_normal,
    reorder_point,
    inventory_turnover_ratio,
    days_of_supply,
    newsvendor_model,
    wagner_whitin,
    silver_meal,
    lot_for_lot,
    fifo_valuation,
    lifo_valuation,
    weighted_average_cost,
    fill_rate_calculation,
    cycle_service_level,
    gmroi,
    bullwhip_effect,
)


class TestEconomicOrderQuantity(unittest.TestCase):
    def test_basic(self):
        result = economic_order_quantity(1000, 100, 5)
        self.assertAlmostEqual(result, 200.0, places=2)

    def test_large_demand(self):
        result = economic_order_quantity(100000, 50, 2)
        self.assertGreater(result, 0)

    def test_zero_demand_raises(self):
        with self.assertRaises(ValueError):
            economic_order_quantity(0, 100, 5)

    def test_negative_cost_raises(self):
        with self.assertRaises(ValueError):
            economic_order_quantity(1000, -100, 5)


class TestEconomicProductionQuantity(unittest.TestCase):
    def test_basic(self):
        result = economic_production_quantity(1000, 2000, 100, 5)
        self.assertAlmostEqual(result, 282.84, places=1)

    def test_production_must_exceed_demand(self):
        with self.assertRaises(ValueError):
            economic_production_quantity(2000, 1000, 100, 5)


class TestEOQWithBackorders(unittest.TestCase):
    def test_basic(self):
        result = eoq_with_backorders(1000, 100, 5, 10)
        self.assertGreater(result, 200)

    def test_high_shortage_cost_approaches_eoq(self):
        result = eoq_with_backorders(1000, 100, 5, 10000)
        self.assertAlmostEqual(result, 200.0, places=0)


class TestABCAnalysis(unittest.TestCase):
    def test_classification(self):
        items = [('a', 100), ('b', 50), ('c', 10)]
        result = abc_analysis(items)
        self.assertEqual(result[0][1], 'A')
        self.assertEqual(result[-1][1], 'C')

    def test_empty_list(self):
        result = abc_analysis([])
        self.assertEqual(result, [])


class TestXYZAnalysis(unittest.TestCase):
    def test_stable_demand(self):
        result = xyz_analysis([('a', [100, 100, 100])])
        self.assertEqual(result[0][1], 'X')

    def test_erratic_demand(self):
        result = xyz_analysis([('a', [100, 0, 300, 0])])
        self.assertEqual(result[0][1], 'Z')


class TestSafetyStock(unittest.TestCase):
    def test_basic(self):
        result = safety_stock_normal(1.96, 10, 4)
        self.assertAlmostEqual(result, 39.2, places=1)

    def test_zero_std(self):
        result = safety_stock_normal(1.96, 0, 4)
        self.assertEqual(result, 0)


class TestReorderPoint(unittest.TestCase):
    def test_basic(self):
        result = reorder_point(100, 2, 50)
        self.assertEqual(result, 250)

    def test_no_safety_stock(self):
        result = reorder_point(100, 2)
        self.assertEqual(result, 200)


class TestInventoryTurnover(unittest.TestCase):
    def test_basic(self):
        result = inventory_turnover_ratio(1000000, 200000)
        self.assertEqual(result, 5.0)

    def test_zero_inventory_raises(self):
        with self.assertRaises(ValueError):
            inventory_turnover_ratio(1000, 0)


class TestDaysOfSupply(unittest.TestCase):
    def test_basic(self):
        result = days_of_supply(1000, 36500)
        self.assertAlmostEqual(result, 10.0, places=1)


class TestNewsvendor(unittest.TestCase):
    def test_critical_ratio(self):
        from math import erf, sqrt
        def cdf(x):
            return 0.5 * (1 + erf((x - 100) / sqrt(2) / 20))
        q = newsvendor_model(5, 10, 2, cdf)
        self.assertGreater(q, 90)
        self.assertLess(q, 110)


class TestWagnerWhitin(unittest.TestCase):
    def test_basic(self):
        periods, cost = wagner_whitin([10, 20, 30, 40], 100, 1)
        self.assertGreater(cost, 0)
        self.assertGreater(len(periods), 0)


class TestSilverMeal(unittest.TestCase):
    def test_basic(self):
        periods, cost = silver_meal([10, 20, 30, 40], 100, 1)
        self.assertGreater(cost, 0)


class TestLotForLot(unittest.TestCase):
    def test_basic(self):
        periods, cost = lot_for_lot([10, 20, 30], 50, 1)
        self.assertEqual(len(periods), 3)
        self.assertEqual(cost, 150)


class TestFIFOValuation(unittest.TestCase):
    def test_basic(self):
        cogs, remaining = fifo_valuation([(10, 5), (20, 6)], 15)
        self.assertAlmostEqual(cogs, 80.0, places=2)
        self.assertEqual(remaining[0][0], 15)


class TestLIFOValuation(unittest.TestCase):
    def test_basic(self):
        cogs, remaining = lifo_valuation([(10, 5), (20, 6)], 15)
        self.assertAlmostEqual(cogs, 90.0, places=2)


class TestWeightedAverageCost(unittest.TestCase):
    def test_basic(self):
        result = weighted_average_cost([(10, 5), (20, 6)])
        self.assertAlmostEqual(result, 5.667, places=2)


class TestFillRate(unittest.TestCase):
    def test_high_safety_stock(self):
        result = fill_rate_calculation(100, 10, 4, 200)
        self.assertGreater(result, 0.9)


class TestCycleServiceLevel(unittest.TestCase):
    def test_basic(self):
        result = cycle_service_level(40, 10, 4)
        self.assertGreater(result, 0.9)
        self.assertLessEqual(result, 1.0)


class TestGMROI(unittest.TestCase):
    def test_basic(self):
        result = gmroi(50000, 25000)
        self.assertEqual(result, 2.0)


class TestBullwhipEffect(unittest.TestCase):
    def test_amplification(self):
        result = bullwhip_effect([100, 110, 90, 100], [100, 130, 60, 100])
        self.assertGreater(result, 1.0)


if __name__ == '__main__':
    unittest.main()
