import unittest
import main
import math


#inherit from the unitest.testcase

class TestMain(unittest.TestCase):
    def test_if_welcome_msg_is_string(self):
        self.assertEqual(str(type(main.welcome("hello"))),"<class 'str'>")
    def test_math_power(self):
        self.assertEqual(math.pow(4,2), 15)


if __name__ == "__main__":
    unittest.main()