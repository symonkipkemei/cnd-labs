# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.


while True:
    try:
        user_num1 = int(input("insert a  dividend: "))
        user_num2 = int(input("insert a  divider: "))

        result = user_num1/user_num2

        print(f"The quotient is : {result}")
        
    except ZeroDivisionError:
        print('you need to go back to primary school')

    except ValueError:
        print("Only numbers are accepted")
    
    else:
        print("\nGood job!")
        break

