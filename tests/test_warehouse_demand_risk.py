"""Unit tests for supplycm.warehouse, demand, and risk algorithms."""
import unittest
from supplycm.warehouse import (
    warehouse_slotting_abc, order_picking_wave, traveling_salesman_picking,
    s_shape_routing, pallet_building, cross_dock_scheduling,
    dock_door_assignment, putaway_strategy, warehouse_layout_optimization,
)
from supplycm.demand import (
    demand_aggregation, demand_disaggregation, demand_class_abc_xyz,
    promotional_demand_lift, cannibalization_effect, stockout_demand_loss,
    demand_sensing, seasonality_index,
)
from supplycm.risk import supply_chain_resilience_index


class TestWarehouseSlotting(unittest.TestCase):
    def test_basic(self):
        result = warehouse_slotting_abc([('a', 1000, 1), ('b', 100, 1), ('c', 10, 1)])
        self.assertEqual(result[0][0], 'a')
        self.assertEqual(result[0][1], 0)


class TestOrderPickingWave(unittest.TestCase):
    def test_basic(self):
        waves = order_picking_wave([[1, 2], [3], [4, 5, 6], [7, 8]], 2)
        total = sum(len(w) for w in waves)
        self.assertEqual(total, 4)


class TestTravelingSalesmanPicking(unittest.TestCase):
    def test_basic(self):
        route = traveling_salesman_picking([(1, 1), (2, 2), (3, 3)])
        self.assertEqual(len(route), 3)


class TestSShapeRouting(unittest.TestCase):
    def test_basic(self):
        result = s_shape_routing([1, 3, 5, 7])
        self.assertEqual(len(result), 7)


class TestPalletBuilding(unittest.TestCase):
    def test_basic(self):
        pallets = pallet_building([(1, 1, 1), (2, 2, 2), (1, 1, 1)], 8)
        total = sum(len(p) for p in pallets)
        self.assertEqual(total, 3)


class TestCrossDockScheduling(unittest.TestCase):
    def test_basic(self):
        ib, ob = cross_dock_scheduling([(0, 30), (10, 20)], [(20, 15)], 2)
        self.assertEqual(len(ib), 2)
        self.assertEqual(len(ob), 1)


class TestDockDoorAssignment(unittest.TestCase):
    def test_basic(self):
        result = dock_door_assignment([('T1', 'NYC'), ('T2', 'LA'), ('T3', 'NYC')], 3)
        self.assertLessEqual(len(result), 3)


class TestPutawayStrategy(unittest.TestCase):
    def test_basic(self):
        result = putaway_strategy([('A', 'A', 5, 100), ('B', 'B', 10, 20)],
                                   [('S1', 10), ('S2', 20)])
        self.assertEqual(len(result), 2)


class TestWarehouseLayoutOptimization(unittest.TestCase):
    def test_basic(self):
        result = warehouse_layout_optimization(
            [('A', 100), ('B', 50), ('C', 10)],
            [('S1', 1), ('S2', 5), ('S3', 10)])
        self.assertEqual(result['A'], 'S1')


class TestDemandAggregation(unittest.TestCase):
    def test_basic(self):
        result = demand_aggregation([10, 20, 30, 40, 50, 60], 3)
        self.assertEqual(result, [60.0, 150.0])


class TestDemandDisaggregation(unittest.TestCase):
    def test_basic(self):
        result = demand_disaggregation(1000, {'A': 0.5, 'B': 0.3, 'C': 0.2})
        self.assertEqual(result['A'], 500.0)
        self.assertEqual(result['B'], 300.0)


class TestDemandClassABCXYZ(unittest.TestCase):
    def test_basic(self):
        result = demand_class_abc_xyz([('a', 'A'), ('b', 'B')],
                                       [('a', 'X'), ('b', 'Y')])
        self.assertEqual(result[0], ('a', 'AX'))


class TestPromotionalDemandLift(unittest.TestCase):
    def test_basic(self):
        result = promotional_demand_lift(100, 150)
        self.assertEqual(result, 1.5)


class TestCannibalizationEffect(unittest.TestCase):
    def test_basic(self):
        result = cannibalization_effect(100, 80, 50)
        self.assertAlmostEqual(result, 0.4, places=2)


class TestStockoutDemandLoss(unittest.TestCase):
    def test_basic(self):
        result = stockout_demand_loss(100, 5, 0.5)
        self.assertEqual(result, 50.0)


class TestDemandSensing(unittest.TestCase):
    def test_basic(self):
        result = demand_sensing([100, 100, 100], [110, 105], 2)
        self.assertEqual(len(result), 3)


class TestSeasonalityIndex(unittest.TestCase):
    def test_basic(self):
        result = seasonality_index([10, 20, 30, 40, 50, 60, 70, 80], 4)
        self.assertEqual(len(result), 4)


class TestSupplyChainResilienceIndex(unittest.TestCase):
    def test_basic(self):
        result = supply_chain_resilience_index(
            {'redundancy': 0.8, 'flexibility': 0.7, 'visibility': 0.6},
            {'redundancy': 0.4, 'flexibility': 0.3, 'visibility': 0.3})
        self.assertGreater(result, 0)
        self.assertLess(result, 1)


if __name__ == '__main__':
    unittest.main()
