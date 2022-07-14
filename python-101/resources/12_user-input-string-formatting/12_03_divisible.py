# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.


while True:
    user_number = int(input("insert a number: "))
    if user_number > 1 and user_number < 1000000000:
        break
    else:
        print("Insert a number between 1 and 1,000,000,000")

answer = (user_number/3)
if user_number%3 == 0:
    print(f"Number is divisible by three.The answer is {answer}")
else:
    print(f"Number is not divisible by three.The answer is {answer}")


