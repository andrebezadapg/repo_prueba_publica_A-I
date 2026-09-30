import unittest

from sales import calculate_discount, calculate_subtotal, calculate_total


class SalesTests(unittest.TestCase):
    def test_calculate_subtotal(self):
        self.assertEqual(calculate_subtotal([12.5, 7.5]), 20)
        self.assertEqual(calculate_subtotal([]), 0)

    def test_calculate_subtotal_rejects_invalid_prices(self):
        for price in (-1, float("inf"), float("nan")):
            with self.subTest(price=price), self.assertRaises(ValueError):
                calculate_subtotal([price])

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(80, 25), 20)
        self.assertEqual(calculate_discount(80, 0), 0)

    def test_calculate_discount_rejects_invalid_inputs(self):
        for amount, percentage in ((-1, 10), (float("inf"), 10), (10, -1), (10, 101)):
            with self.subTest(amount=amount, percentage=percentage):
                with self.assertRaises(ValueError):
                    calculate_discount(amount, percentage)

    def test_calculate_total(self):
        self.assertEqual(calculate_total([12.5, 7.5]), 20)
        self.assertEqual(calculate_total([12.5, 7.5], 25), 15)


if __name__ == "__main__":
    unittest.main()
