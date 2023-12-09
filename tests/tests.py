import unittest
from src.ans import custom_exponent


class TestCustomExponent(unittest.TestCase):

    def test_positive_exponent(self):
        self.assertEqual(custom_exponent(2, 3), 8)

    def test_zero_exponent(self):
        self.assertEqual(custom_exponent(5, 0), 1)

    def test_one_exponent(self):
        self.assertEqual(custom_exponent(7, 1), 7)


if __name__ == '__main__':
    unittest.main()
