# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)



import unittest

class SuccessError(Exception):
    pass
    
def success(income):
    ans = None

    try:
        if income >= 1000:
            ans = True
        elif income == 0:
            raise SuccessError 
        elif income.isalpha():
            raise ValueError
        else:
            ans= False
    except SuccessError:
        print(("0 income and success cannot be in the same sentence"))
    except ValueError:
        print("input should only be an integer")
    except Exception as e:
        print(f"{e} occurred")
    finally:
        return ans

  


class TestSuccess(unittest.TestCase):
    def test_success_ful(self):
        
        self.assertEqual(success(1200), True)
        self.assertEqual(success(1000), True)
        self.assertEqual(success(800), False)

        with self.assertRaises(SuccessError) as context:
            success(0)
        with self.assertRaises(ValueError):
            success("income")
        
        
if __name__ == "__main__":
    unittest.main()