# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

# standard parameter for dating
dating_age = 24
body_count = 0

# user feedback on parameters
user_age = int(input("what's your age?: "))
user_count = int(input("how many people have you slept with?: "))

# comparison 

if user_age == dating_age  and user_count == body_count:

     print('It seems you fell from heaven, beacause I am just about to date and marry you!')

elif user_age > dating_age or user_count > body_count:
    print("Do you mind if you fall 6 inches deep?")

elif not user_age > dating_age:
    print("Hey pretty sister")

else:
    print("sorry , I am not your type")
