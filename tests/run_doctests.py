"""Run doctests for all supplycm modules.

Executes the example code in every module's docstrings to verify
they produce the expected output.

Usage:
    python tests/run_doctests.py
"""
import doctest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import all modules
from supplycm import (
    inventory, forecasting, statistics, routing, network,
    scheduling, mrp, optimization, supplier, warehouse, demand, risk,
)

ALL_MODULES = [
    inventory, forecasting, statistics, routing, network,
    scheduling, mrp, optimization, supplier, warehouse, demand, risk,
]


def run_all_doctests():
    """Run doctests in all modules and report results."""
    total_tests = 0
    total_failures = 0
    total_errors = 0

    print("Running doctests for all supplycm modules...")
    print("=" * 60)

    for mod in ALL_MODULES:
        results = doctest.testmod(mod, verbose=False, report=False)
        total_tests += results.attempted
        total_failures += results.failed
        if results.failed > 0:
            print(f"  FAIL: {mod.__name__} - {results.failed}/{results.attempted} tests failed")
        else:
            print(f"  OK:   {mod.__name__} - {results.attempted} tests passed")

    print("=" * 60)
    print(f"Total: {total_tests} tests, {total_failures} failures")

    return total_failures == 0


if __name__ == '__main__':
    success = run_all_doctests()
    sys.exit(0 if success else 1)
