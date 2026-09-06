"""Unit tests for network design, IoT, and blockchain algorithms."""
import unittest
from supplycm.network_design import (
    center_of_gravity, facility_location_fixed_cost, single_source_allocation,
    break_even_analysis, network_reliability,
)
from supplycm.iot import (
    anomaly_detection, sensor_data_smoothing,
    realtime_inventory_monitor, iot_data_aggregation,
)
from supplycm.blockchain import (
    hash_chain, verify_chain, provenance_tracking, smart_contract_check,
)


class TestNetworkDesign(unittest.TestCase):
    def test_center_of_gravity(self):
        x, y = center_of_gravity([(0, 0, 10), (10, 0, 20), (5, 10, 15)])
        self.assertAlmostEqual(x, 6.11, places=1)
        self.assertAlmostEqual(y, 3.33, places=1)

    def test_facility_location(self):
        facs, cost = facility_location_fixed_cost(
            [10, 20, 30], [[1, 5, 3], [5, 1, 2], [3, 2, 1]], [100, 120, 80], 1)
        self.assertEqual(len(facs), 1)
        self.assertGreater(cost, 0)

    def test_single_source_allocation(self):
        alloc = single_source_allocation([5, 10, 8],
            [[1, 5], [5, 1], [3, 2]], [15, 10])
        self.assertEqual(len(alloc), 3)

    def test_break_even(self):
        self.assertEqual(break_even_analysis(10000, 5, 10), 2000.0)

    def test_network_reliability(self):
        result = network_reliability({0: 0.9, 1: 0.95, 2: 0.85}, [(0, 1), (1, 2)])
        self.assertGreater(result, 0)
        self.assertLess(result, 1)


class TestIoT(unittest.TestCase):
    def test_anomaly_detection(self):
        data = [10, 10, 11, 10, 50, 10, 11, 10]
        anomalies = anomaly_detection(data, window=4, threshold=2.0)
        self.assertGreaterEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0][1], 50)

    def test_sensor_smoothing(self):
        result = sensor_data_smoothing([10, 15, 12, 18, 11], 0.5)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 10.0)

    def test_realtime_monitor(self):
        alerts = realtime_inventory_monitor(
            {'A': 50, 'B': 20}, {'A': 40, 'B': 30}, {'A': 20, 'B': 15})
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]['item'], 'B')

    def test_iot_aggregation(self):
        result = iot_data_aggregation(
            [1, 2, 3, 4, 5], [10, 20, 30, 40, 50], window_size=2)
        self.assertGreaterEqual(len(result), 2)


class TestBlockchain(unittest.TestCase):
    def test_hash_chain(self):
        records = [{'event': 'created'}, {'event': 'shipped'}]
        hashes = hash_chain(records)
        self.assertEqual(len(hashes), 2)
        self.assertTrue(all(len(h) == 64 for h in hashes))

    def test_verify_chain_valid(self):
        records = [{'event': 'created'}, {'event': 'shipped'}]
        hashes = hash_chain(records)
        self.assertTrue(verify_chain(records, hashes))

    def test_verify_chain_tampered(self):
        records = [{'event': 'created'}, {'event': 'shipped'}]
        hashes = hash_chain(records)
        records[0]['event'] = 'modified'
        self.assertFalse(verify_chain(records, hashes))

    def test_provenance_tracking(self):
        events = [
            {'product': 'A', 'event': 'made', 'time': 1},
            {'product': 'B', 'event': 'made', 'time': 2},
            {'product': 'A', 'event': 'shipped', 'time': 3},
        ]
        history = provenance_tracking(events, 'A')
        self.assertEqual(len(history), 2)

    def test_smart_contract_valid(self):
        result = smart_contract_check(
            {'temperature': 5, 'humidity': 60},
            [{'field': 'temperature', 'operator': '<=', 'value': 8},
             {'field': 'humidity', 'operator': '>=', 'value': 40}])
        self.assertTrue(result['valid'])

    def test_smart_contract_violation(self):
        result = smart_contract_check(
            {'temperature': 10},
            [{'field': 'temperature', 'operator': '<=', 'value': 8}])
        self.assertFalse(result['valid'])
        self.assertGreater(len(result['violations']), 0)


if __name__ == '__main__':
    unittest.main()
