# Python 3.14 Preparation

This document tracks preparation for Python 3.14 (scheduled October 2026).

## Checklist

- [ ] Add Python 3.14 to CI test matrix once beta is available
- [ ] Update setup.py classifiers
- [ ] Test all 360 algorithms on 3.14 beta
- [ ] Update docs/PYTHON_VERSIONS.md
- [ ] Verify no deprecated APIs are used

## Known Changes in Python 3.14

1. Improved error messages for deferred evaluation of annotations
2. Potential stabilization of the JIT (Just-In-Time) compiler from 3.13
3. New __static_attributes__ for classes

## Testing Plan

1. Run python tests/run_tests.py on 3.14 beta
2. Run python tests/run_doctests.py on 3.14 beta
3. Run python tests/benchmark.py to compare performance
4. Verify identical results with 3.13

## References

- Issue #1: Add support for Python 3.14
- Python 3.14 release schedule: https://devguide.python.org/
