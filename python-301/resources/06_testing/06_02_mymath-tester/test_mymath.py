# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.


import unittest
import mymath

class test_mymath(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(mymath.subtract_divide(8,6,4), 4)
        with self.assertRaises(mymath.CustomZeroDivsionError) as context:
            mymath.subtract_divide(8,7,7)


if __name__ == "__main__":
    unittest.main()

