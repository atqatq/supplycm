# Migration Guide

This document helps you upgrade between versions of supplycm.

## Upgrading to 0.1.0

Version 0.1.0 is the initial public release. If you were using a pre-release version:

### Changes

- All algorithms are now in their own modules (one file per algorithm)
- Import paths have changed:

```python
# Before (pre-release)
from supplycm import eoq

# After (0.1.0)
from supplycm.inventory import economic_order_quantity
```

- Function names have been standardized to snake_case
- All functions now have type hints and docstrings

### New Features

- 360 algorithms across 12 categories
- Comprehensive test suite
- Usage examples and tutorials
- Contributing guide

## Upgrading to 1.0.0 (planned)

Version 1.0.0 will be the first stable release with:

- Guaranteed backward compatibility
- Full test coverage
- Performance optimizations
- Additional algorithms

### Breaking Changes Planned

None. The API is stable from 0.1.0 onwards.

## Versioning Policy

supplycm follows [Semantic Versioning](https://semver.org/):

- **Major** (1.x.x): Breaking changes
- **Minor** (0.1.x): New features, backward compatible
- **Patch** (0.1.0): Bug fixes, backward compatible
