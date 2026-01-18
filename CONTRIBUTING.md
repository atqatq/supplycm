# Contributing to supplycm

Thank you for your interest in contributing to supplycm. This document explains how to contribute.

## Ways to Contribute

1. **Report bugs** - Open an issue describing the problem with a minimal example.
2. **Suggest features** - Open an issue describing the use case and proposed solution.
3. **Improve documentation** - Fix typos, add examples, clarify explanations.
4. **Add algorithms** - Implement new supply chain algorithms following the style guide below.
5. **Write tests** - Add or improve test coverage for existing algorithms.

## Style Guide

### Algorithm Module Structure

Each algorithm lives in its own file under the appropriate category directory:

```
supplycm/
  inventory/
    economic_order_quantity.py
```

### File Template

```python
"""Short one-line description."""
from typing import List, Optional


def algorithm_name(param1: float, param2: int = 3) -> float:
    """One-line summary.

    Longer description explaining the formula or logic.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Example:
        >>> algorithm_name(100, 5)
        42.0
    """
    if param1 <= 0:
        raise ValueError("param1 must be positive")
    return param1 * 0.42
```

### Rules

1. **No external dependencies** - only the Python standard library.
2. **Type hints** - all function parameters and return types must have type hints.
3. **Docstrings** - every public function must have a docstring with at least one example.
4. **Pure functions** - algorithms should not have side effects.
5. **Error handling** - validate inputs and raise ValueError for invalid parameters.

## Development Workflow

1. Fork the repository.
2. Create a feature branch: `git checkout -b add-new-algorithm`.
3. Write your code following the style guide.
4. Add tests in `tests/test_<category>.py`.
5. Run tests: `python tests/run_tests.py`.
6. Commit with a clear message: `Add <algorithm_name> to <category> module`.
7. Open a Pull Request (PR).

## Pull Request Checklist

- [ ] Code follows the style guide
- [ ] Tests pass locally
- [ ] Docstring includes at least one example
- [ ] No external dependencies added
- [ ] Commit message is clear and descriptive

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
