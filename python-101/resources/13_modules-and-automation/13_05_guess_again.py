# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random


# create a welcome message to the user( give how,rules of the game)
print(""" Welcome to the GUESS NO GAME
hint * The number ranges between 0 and 10
you have a few attempts to get the answer right!
All the best!\n""")

# establish the number of counts the user want's to set
count_check = int(input("How many times do you want to attempt this game: "))
count = 0
# computer choice (changes everythime the script is run)
selection = []
for x in range(0,count_check):
    no = random.randint(1,11)
    selection.append(no)
random_comp_choice = random.choice(selection)

while count != count_check:
    # user choice (user has a choice between certain ranges of numbers 1 to 10)
    user_choice = int(input("insert your guess: "))
    
    # check if user choice matches computer choice
    if user_choice == random_comp_choice:
        # if it matches he wins
        print("Congratulations!, you have won")
        break
    else:
        # if he/she loses the count reduces
        count += 1
        # if he/she loses the count reduces
        print(f"You have {count_check - count} tries remaining")

# if the count reaches 0 ,the game ends
if count == count_check:
    print("\nWhen you lose all that matters is that you win next time")









