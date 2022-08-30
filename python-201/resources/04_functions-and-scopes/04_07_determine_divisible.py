# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divisible_by_4_or_7(user_number: int)-> bool:
    """Checks if a number is divisble by 4 or 7

    Args:
        user_number (int): Number provided by the user

    Returns:
        bool: if its True or not
    """

    if user_number % 4 == 0 or user_number % 7 == 0:
        return True
    else:
        return False

ans1 = divisible_by_4_or_7(2)
print(ans1)

def divisible_by_4_and_7(user_number: int)-> bool:
    """Checks if a number is divisble by both 4 and 7

    Args:
        user_number (int): Number provided by the user

    Returns:
        bool: if its True or not
    """

    if user_number % 4 == 0 and user_number % 7 == 0:
        return True
    else:
        return False


ans2 = divisible_by_4_or_7(56)
print(ans2)