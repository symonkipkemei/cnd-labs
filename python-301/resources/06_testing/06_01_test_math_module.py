# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class TestMath(unittest.TestCase):
    def test_math_gcd(self):
        self.assertEqual(math.gcd(7,9),1)

    def test_math_truncate(self):
        self.assertEqual(math.trunc(8.89864), 8)


if __name__ == "__main__":
    unittest.main()