# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.



user_number = int(input("Insert a number between 1 and 12: "))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


if user_number <= 12 and user_number >= 1:
    for index, x in enumerate(months):
        if (index + 1) == user_number:
            print( x , end=" ")
else:
    print('The selected number does not represent a month')