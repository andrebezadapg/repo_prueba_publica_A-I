# repo_prueba_publica_A-I

Basic sales calculation functions in Python.

`sales.py` provides `calculate_subtotal`, `calculate_discount`, and
`calculate_total`. Prices and amounts must be finite and non-negative;
discount percentages must be between 0 and 100.

```python
from sales import calculate_total

total = calculate_total([25.0, 15.0], discount_percentage=10)
```

Run the tests with `python -m unittest`.
