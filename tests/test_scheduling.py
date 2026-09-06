"""Unit tests for supplycm.scheduling algorithms."""
import unittest
from supplycm.scheduling import (
    johnsons_rule, spt_rule, edd_rule, wspt_rule, moore_hodgson,
    neh_heuristic, critical_ratio, least_slack, fcfs_rule,
    cmax_calculation, tardiness_calculation, total_completion_time,
    list_scheduling, lpt_rule, machine_utilization,
    critical_path_method, pert_expected_duration,
)


class TestJohnsonsRule(unittest.TestCase):
    def test_three_jobs(self):
        result = johnsons_rule([(3, 5), (1, 2), (4, 1)])
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), {0, 1, 2})


class TestSPTRule(unittest.TestCase):
    def test_ordering(self):
        result = spt_rule([5, 2, 8, 1])
        self.assertEqual(result, [3, 1, 0, 2])


class TestEDDRule(unittest.TestCase):
    def test_ordering(self):
        result = edd_rule([10, 5, 8, 2])
        self.assertEqual(result, [3, 1, 2, 0])


class TestWSPTRule(unittest.TestCase):
    def test_ordering(self):
        result = wspt_rule([5, 2, 8], [1, 1, 4])
        self.assertIn(result[0], [1, 2])


class TestMooreHodgson(unittest.TestCase):
    def test_basic(self):
        result = moore_hodgson([3, 1, 2], [5, 1, 6])
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), {0, 1, 2})


class TestNEHHeuristic(unittest.TestCase):
    def test_basic(self):
        result = neh_heuristic([[3, 5], [1, 2], [4, 1]])
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), {0, 1, 2})


class TestCriticalRatio(unittest.TestCase):
    def test_basic(self):
        result = critical_ratio([5, 10, 2], [10, 30, 5])
        self.assertEqual(len(result), 3)


class TestLeastSlack(unittest.TestCase):
    def test_basic(self):
        result = least_slack([5, 10, 2], [10, 30, 5])
        self.assertEqual(len(result), 3)


class TestFCFSRule(unittest.TestCase):
    def test_ordering(self):
        result = fcfs_rule([3, 1, 2])
        self.assertEqual(result, [1, 2, 0])


class TestCmaxCalculation(unittest.TestCase):
    def test_basic(self):
        result = cmax_calculation([0, 1, 2], [[3, 5], [1, 2], [4, 1]])
        self.assertAlmostEqual(result, 11.0, places=1)


class TestTardinessCalculation(unittest.TestCase):
    def test_basic(self):
        result = tardiness_calculation([0, 1, 2], [3, 2, 4], [5, 10, 12])
        self.assertAlmostEqual(result, 0.0, places=1)


class TestTotalCompletionTime(unittest.TestCase):
    def test_basic(self):
        result = total_completion_time([0, 1, 2], [3, 2, 4])
        self.assertAlmostEqual(result, 17.0, places=1)


class TestListScheduling(unittest.TestCase):
    def test_basic(self):
        result = list_scheduling([3, 5, 2, 4, 1], 2)
        total_jobs = sum(len(s) for s in result)
        self.assertEqual(total_jobs, 5)


class TestLPTRule(unittest.TestCase):
    def test_basic(self):
        result = lpt_rule([3, 5, 2, 4, 1], 2)
        total_jobs = sum(len(s) for s in result)
        self.assertEqual(total_jobs, 5)


class TestMachineUtilization(unittest.TestCase):
    def test_basic(self):
        result = machine_utilization([8, 6, 10], 10)
        self.assertEqual(result[0], 0.8)
        self.assertEqual(result[2], 1.0)


class TestCriticalPathMethod(unittest.TestCase):
    def test_basic(self):
        cpm = critical_path_method([0, 3, 5, 2, 0], [[1, 2], [3], [3], [4], []])
        self.assertIn(0, cpm)
        self.assertIn(4, cpm)


class TestPERT(unittest.TestCase):
    def test_basic(self):
        result = pert_expected_duration([1, 2], [3, 4], [5, 6])
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0][0], 3.0)


if __name__ == '__main__':
    unittest.main()
