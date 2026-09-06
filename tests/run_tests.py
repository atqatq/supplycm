"""Test runner for supplycm test suite.

Runs all tests using Python's built-in unittest framework.
No external dependencies required.

Usage:
    python tests/run_tests.py
"""
import unittest
import sys
import os

# Add parent directory to path so we can import supplycm
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def run_all_tests():
    """Discover and run all tests in the tests directory."""
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
