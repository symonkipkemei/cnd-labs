import unittest

class MyExcept(Exception):
    pass

class SecondExcept(Exception):
    pass


def throw_ex(var):
    if var== 100:
        raise MyExcept("NOT A VALID NUMBER")
    
    elif var == 200:
        raise SecondExcept("NOT A VALID ______________")
    else:
        return True


class LearnUniTest(unittest.TestCase):
    def test_sample(self):
        with self.assertRaises(MyExcept) as context:
            throw_ex(100)

        self.assertRaises((MyExcept,SecondExcept), throw_ex, 100)


if __name__ == "__main__":
    unittest.main()