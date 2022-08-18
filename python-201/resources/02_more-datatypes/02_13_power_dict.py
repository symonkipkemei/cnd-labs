# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}


# numbers
num_dict = {}

# select a number between 1 and 10
for num in range(1, 11):
    key = num
    value = num * num
    # store num and key in dictionary
    num_dict[key] = value


print(num_dict)