# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


user_number  = int(input("Insert a number between 0 and 1,000,000: "))
while True:
    for x in range(0, 1000000):
        print(x)
        if user_number == x:
            break
    break
    