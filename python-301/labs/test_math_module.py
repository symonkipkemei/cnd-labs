import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
    def test_gcd(self):
        self.assertEqual(math.gcd(8,12),4)


if __name__ == "__main__":
    unittest.main()