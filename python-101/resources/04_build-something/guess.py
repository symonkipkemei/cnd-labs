# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random

comp_num = int(random.randint(1,10))

guess_num = None

while guess_num != comp_num:
    guess_num = int(input("Guess a number BETWEEN 1 and 10: "))
    if guess_num == comp_num:
        print("you got it correct!")

    else:
        print("you got it wrong, try again")
    



    
