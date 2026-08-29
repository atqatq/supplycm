# Frequently Asked Questions (FAQ)

## General

### What is supplycm?

supplycm is a pure-Python library containing 360 supply chain management algorithms. It covers forecasting, inventory, routing, scheduling, optimization, and more.

### Why no external dependencies?

The library uses only the Python standard library. This makes it easy to install, portable across systems, and suitable for environments where installing packages is restricted.

### Is supplycm free to use?

Yes, supplycm is released under the MIT License. You can use it freely for personal and commercial projects.

### Are these algorithms patented?

The implementations in supplycm are original code based on well-known, public-domain algorithms. The library does not include any patented or copyrighted material.

## Installation

### How do I install supplycm?

```bash
pip install supplycm
```

Or from source:

```bash
git clone https://github.com/atqatq/supplycm.git
cd supplycm
pip install .
```

### Which Python versions are supported?

supplycm supports Python 3.6 and later. It has been tested on Python 3.8 through 3.12.

### Can I use supplycm without installing it?

Yes, simply add the supplycm directory to your Python path:

```python
import sys
sys.path.insert(0, '/path/to/supplycm')
import supplycm
```

## Usage

### How do I find a specific algorithm?

Browse the README for the full algorithm index, organized by category. Each algorithm lives in its own module under the appropriate category directory.

### Can I use multiple algorithms together?

Yes, algorithms are designed to be composable. For example:

```python
from supplycm.inventory import economic_order_quantity, safety_stock_normal
from supplycm.forecasting import single_exponential_smoothing

# Forecast demand
forecast = single_exponential_smoothing([100, 110, 105, 120])

# Calculate optimal order quantity using forecasted demand
eoq = economic_order_quantity(forecast[-1] * 12, 100, 5)
```

### How accurate are the algorithms?

All algorithms implement standard, well-established methods. Accuracy depends on the quality of input data and appropriateness of the method for your use case.

## Testing

### How do I run the tests?

```bash
python tests/run_tests.py
```

Or run doctests:

```bash
python tests/run_doctests.py
```

### What test framework is used?

supplycm uses Python's built-in `unittest` framework. No external testing dependencies are required.

## Contributing

### How can I contribute?

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines. You can report bugs, suggest features, add algorithms, improve documentation, or write tests.

### Can I add a new algorithm?

Yes, please do. Follow the style guide in CONTRIBUTING.md, add tests, and open a Pull Request (PR).

## Performance

### How fast is supplycm?

Since supplycm uses pure Python without NumPy or similar libraries, performance is suitable for educational purposes, prototyping, and small to medium datasets. For large-scale production use, consider rewriting critical paths in a compiled language.

### Can I use supplycm in production?

supplycm is suitable for prototyping, education, and small-scale applications. For mission-critical production systems, thoroughly test all algorithms against your specific use case.
