while True:
    try:
        dividend = int(input("Please enter the number to be divided: "))
        divisor = int(input("Please enter the divisor: "))
        result = dividend / divisor
        print(f"The result of {dividend} divided by {divisor} is {result}")
    except ZeroDivisionError:
        print("My most sincere apologies, but you can't divide by zero.")
    except ValueError:
        print("I am reminding you again please use numbers only")
    except Exception as e:
        print(f"remain calm_____________, this error has occured {e}")