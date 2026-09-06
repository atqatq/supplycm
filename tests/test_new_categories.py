"""Unit tests for new algorithm categories."""
import unittest
from supplycm.quality import (
    x_bar_chart, r_chart, p_chart, process_capability_cp,
    process_capability_cpk, dpmo, sigma_level,
)
from supplycm.lean import takt_time, oee, cycle_time_efficiency, wip_calculation
from supplycm.sop import demand_supply_match, production_chase_strategy, production_level_strategy
from supplycm.sustainability import carbon_footprint_transport, reverse_logistics_cost, energy_consumption_warehouse
from supplycm.contracts import revenue_sharing_contract, buyback_contract, quantity_flexibility_contract
from supplycm.simulation import monte_carlo_inventory, monte_carlo_risk
from supplycm.cost import landed_cost, total_cost_procurement


class TestQuality(unittest.TestCase):
    def test_x_bar_chart(self):
        means, ucl, lcl = x_bar_chart([[10, 12, 11], [11, 13, 10], [10, 11, 12]])
        self.assertEqual(len(means), 3)
        self.assertGreater(ucl, lcl)

    def test_process_capability_cp(self):
        self.assertAlmostEqual(process_capability_cp(10, 2, 1.0), 1.33, places=2)

    def test_process_capability_cpk(self):
        self.assertAlmostEqual(process_capability_cpk(10, 2, 6, 1.0), 1.33, places=2)

    def test_dpmo(self):
        self.assertEqual(dpmo(5, 1000, 10), 500.0)

    def test_sigma_level(self):
        self.assertAlmostEqual(sigma_level(3.4), 6.0, places=1)


class TestLean(unittest.TestCase):
    def test_takt_time(self):
        self.assertEqual(takt_time(480, 240), 2.0)

    def test_oee(self):
        self.assertAlmostEqual(oee(0.9, 0.95, 0.98), 0.8379, places=3)

    def test_cycle_time_efficiency(self):
        self.assertAlmostEqual(cycle_time_efficiency(5, 50), 0.1, places=2)

    def test_wip(self):
        self.assertEqual(wip_calculation(10, 5), 50)


class TestSOP(unittest.TestCase):
    def test_demand_supply_match(self):
        net, gap = demand_supply_match([100, 120, 130], [90, 130, 125])
        self.assertEqual(net[0], 10.0)

    def test_chase(self):
        self.assertEqual(production_chase_strategy([100, 120, 130]), [100, 120, 130])

    def test_level(self):
        result = production_level_strategy([90, 120, 150])
        self.assertTrue(all(r == result[0] for r in result))


class TestSustainability(unittest.TestCase):
    def test_carbon(self):
        self.assertAlmostEqual(carbon_footprint_transport(500, 10), 310.0, places=1)

    def test_reverse_logistics(self):
        self.assertGreater(reverse_logistics_cost(0.1, 100, 5, 2, 30), 0)

    def test_energy(self):
        self.assertEqual(energy_consumption_warehouse(10000, 24, 365), 4380000.0)


class TestContracts(unittest.TestCase):
    def test_revenue_sharing(self):
        result = revenue_sharing_contract(40, 100, 0.2, 1000, 20)
        self.assertGreater(result["supplier_profit"], 0)

    def test_buyback(self):
        result = buyback_contract(50, 100, 30, 800, 20, 10)
        self.assertIsInstance(result["supplier_profit"], float)

    def test_quantity_flexibility(self):
        result = quantity_flexibility_contract(50, 100, 1000, 900, 20, 0.2)
        self.assertLessEqual(result["final_quantity"], 1000)


class TestSimulation(unittest.TestCase):
    def test_monte_carlo_inventory(self):
        result = monte_carlo_inventory(100, 20, 250, 2, 1000)
        self.assertGreaterEqual(result["stockout_probability"], 0)
        self.assertLessEqual(result["stockout_probability"], 1)

    def test_monte_carlo_risk(self):
        result = monte_carlo_risk([
            {"cost_mean": 1000, "cost_std": 100, "probability": 0.7},
            {"cost_mean": 5000, "cost_std": 500, "probability": 0.3},
        ], 1000)
        self.assertGreater(result["expected_cost"], 0)


class TestCost(unittest.TestCase):
    def test_landed_cost(self):
        self.assertAlmostEqual(landed_cost(100, 500, 0.05, 0.01, 100, 50, 10), 171.0, places=1)

    def test_total_procurement(self):
        self.assertEqual(total_cost_procurement(100000, 5000, 8000, 2000, 1000, 3000), 119000)


if __name__ == '__main__':
    unittest.main()
