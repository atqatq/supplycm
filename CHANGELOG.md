# Changelog

All notable changes to supplycm will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Interactive learning notebooks
- Video tutorials
- Certification program
## [1.1.0] - 2026-09-06

### Added
- 24 new algorithms across 7 new categories:
  - Quality / Six Sigma (7): X-bar chart, R chart, P-chart, Cp, Cpk, DPMO, sigma level
  - Lean (4): takt time, OEE, cycle efficiency, WIP calculation
  - S&OP (3): demand-supply match, chase and level production strategies
  - Sustainability (3): carbon footprint, reverse logistics, energy consumption
  - Contracts (3): revenue sharing, buyback, quantity flexibility
  - Simulation (2): Monte Carlo inventory and risk
  - Cost (2): landed cost, total procurement cost
- Comprehensive education framework:
  - Learning paths (beginner to advanced)
  - Concept map showing algorithm relationships
  - Data sources guide per algorithm
  - Flashcards for exam preparation
  - Plain English guides per category
- Unit tests for all new algorithms

### Changed
- Total algorithm count increased from 360 to 384
- README updated with education section



### Planned
- Additional algorithms for sustainability and green supply chain
- Performance optimizations for large datasets
- Integration with popular data formats

## [1.0.0] - 2026-12-15

### Added
- Comprehensive test suite with 200+ unit tests using unittest framework
- Property-based tests for mathematical invariants
- Edge case tests for boundary conditions
- Integration tests for end-to-end workflows
- Doctest runner for docstring examples
- Benchmark script for performance measurement
- Type hints validation script
- Contributing guide for new contributors
- Code of Conduct based on Contributor Covenant
- Security policy for vulnerability reporting
- Frequently Asked Questions (FAQ) document
- API reference documentation
- Migration guide for version updates
- Usage tutorials for inventory, forecasting, routing, optimization, and supplier selection
- GitHub Actions Continuous Integration (CI) for Python 3.8-3.12
- Issue templates for bug reports and feature requests
- Pull Request (PR) template
- Python version compatibility matrix in README
- Badges for Python version, license, test status, and dependencies

### Changed
- README updated with quick start guide and badges
- All algorithm modules follow consistent style guide
- Documentation reorganized into docs/ directory

### Fixed
- Repository URL corrected to point to atqatq/supplycm

## [0.1.0] - 2025-12-15

### Added
- 360 supply chain management algorithms across 12 categories:
  - Forecasting (50 algorithms)
  - Inventory (60 algorithms)
  - Statistics (40 algorithms)
  - Routing (30 algorithms)
  - Network (30 algorithms)
  - Scheduling (40 algorithms)
  - Material Requirements Planning (MRP) (30 algorithms)
  - Optimization (30 algorithms)
  - Supplier Management (30 algorithms)
  - Warehouse (10 algorithms)
  - Demand Planning (9 algorithms)
  - Risk Assessment (1 algorithm)
- Pure Python implementation with zero external dependencies
- MIT License
- Setup scripts for pip installation

### Notes
- Algorithms span classic operations research methods and modern heuristics
- Each algorithm is self-contained in its own module
- All functions include docstrings with usage examples
