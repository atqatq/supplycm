"""Unit tests for supplycm.mrp algorithms."""
import unittest
from supplycm.mrp import (
    bom_explosion, mrp_calculation, low_level_coding, where_used_query,
    available_to_promise, master_production_schedule,
    demand_time_fence, lead_time_offsetting, safety_lead_time,
    shrinkage_factor, lot_size_rule_l4l, lot_size_rule_foq,
    lot_size_rule_poq, cycle_counting, backflush, kaban_sizing,
)


class TestBOMExplosion(unittest.TestCase):
    def test_basic(self):
        bom = {0: [(1, 2), (2, 3)], 1: [(3, 1)], 2: [], 3: []}
        req = bom_explosion(10, bom, 0)
        self.assertEqual(req[1], 20)
        self.assertEqual(req[2], 30)
        self.assertEqual(req[3], 20)


class TestMRPCalculation(unittest.TestCase):
    def test_basic(self):
        result = mrp_calculation([10, 20, 30, 40], [0, 0, 0, 0], 5, 1, lot_size=50)
        self.assertEqual(len(result['planned_orders']), 4)
        self.assertEqual(len(result['projected_on_hand']), 4)


class TestLowLevelCoding(unittest.TestCase):
    def test_basic(self):
        bom = {0: [1, 2], 1: [3], 2: [3], 3: []}
        llc = low_level_coding(bom)
        self.assertGreaterEqual(llc[3], 2)
        self.assertEqual(llc[0], 0)


class TestWhereUsedQuery(unittest.TestCase):
    def test_basic(self):
        bom = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = where_used_query(bom, 3)
        self.assertIn(0, result)
        self.assertIn(1, result)
        self.assertIn(2, result)


class TestAvailableToPromise(unittest.TestCase):
    def test_basic(self):
        atp = available_to_promise(100, [50, 0, 50], [30, 20, 10])
        self.assertEqual(len(atp), 3)
        self.assertEqual(atp[0], 120)


class TestMasterProductionSchedule(unittest.TestCase):
    def test_basic(self):
        mps = master_production_schedule([10, 20, 30, 40], [5, 10, 15, 20], 10, 50, 4)
        self.assertEqual(len(mps), 4)


class TestDemandTimeFence(unittest.TestCase):
    def test_basic(self):
        result = demand_time_fence([100, 100, 100, 100], [50, 60, 0, 0], 2)
        self.assertEqual(result[0], 50)
        self.assertEqual(result[2], 100)


class TestLeadTimeOffsetting(unittest.TestCase):
    def test_basic(self):
        result = lead_time_offsetting([0, 0, 100, 0, 200], 2)
        self.assertEqual(len(result), 5)


class TestSafetyLeadTime(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(safety_lead_time(5, 2), 7)


class TestShrinkageFactor(unittest.TestCase):
    def test_basic(self):
        result = shrinkage_factor(100, 0.05)
        self.assertAlmostEqual(result, 105.263, places=2)


class TestLotSizeL4L(unittest.TestCase):
    def test_basic(self):
        result = lot_size_rule_l4l([10, 0, 20, 30])
        self.assertEqual(result, [10, 0, 20, 30])


class TestLotSizeFOQ(unittest.TestCase):
    def test_basic(self):
        result = lot_size_rule_foq([10, 20, 5, 0], 25)
        self.assertEqual(result[0], 25)


class TestLotSizePOQ(unittest.TestCase):
    def test_basic(self):
        result = lot_size_rule_poq([10, 20, 30, 40, 50], 2)
        self.assertEqual(result[0], 30)
        self.assertEqual(result[1], 0)


class TestCycleCounting(unittest.TestCase):
    def test_basic(self):
        plan = cycle_counting([('a', 'A'), ('b', 'B'), ('c', 'C')],
                              {'A': 12, 'B': 4, 'C': 1})
        self.assertEqual(len(plan), 12)


class TestBackflush(unittest.TestCase):
    def test_basic(self):
        result = backflush(10, {0: [(1, 2), (2, 3)]})
        self.assertEqual(result[1], 20)
        self.assertEqual(result[2], 30)


class TestKanbanSizing(unittest.TestCase):
    def test_basic(self):
        result = kaban_sizing(100, 2, 50, 1.1)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
