# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.


# count,award for every unique entry
win_points = 0
loss_point = 0

# store numbers in set
py_set = {8}

while win_points < 10:
    # collect number from user
    while True:
        user_num = input("Insert a number: ")
        if user_num.isdigit():
            break
        else:
            print("Please insert an integer")
    print("Helo")
    # if python set is empty add number first before checking if there is a repeat number

    for num in py_set:
        if num == user_num:
            print("Number already in set")
            loss_point -= 1
        else:
            py_set.add(user_num)
            win_points += 1
        
        

    # if use loses 5 times, game ends
    if loss_point == -5:
        print('I am sorry butit seems you are a perennial loser')
        break


if win_points == 10:
    print('You won congratulations!')



