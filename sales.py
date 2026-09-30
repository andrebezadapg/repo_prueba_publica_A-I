"""Utilities for basic sales calculations."""

import math
from collections.abc import Iterable


def calculate_subtotal(prices: Iterable[float]) -> float:
    """Return the sum of item prices."""
    subtotal = 0.0
    for price in prices:
        if not math.isfinite(price) or price < 0:
            raise ValueError("prices must be finite and non-negative")
        subtotal += price
    return subtotal


def calculate_discount(amount: float, percentage: float) -> float:
    """Return a percentage discount for an amount."""
    if not math.isfinite(amount) or amount < 0:
        raise ValueError("amount must be finite and non-negative")
    if not math.isfinite(percentage) or not 0 <= percentage <= 100:
        raise ValueError("percentage must be between 0 and 100")
    return amount * percentage / 100


def calculate_total(
    prices: Iterable[float], discount_percentage: float = 0
) -> float:
    """Return the item total after applying a percentage discount."""
    subtotal = calculate_subtotal(prices)
    return subtotal - calculate_discount(subtotal, discount_percentage)
