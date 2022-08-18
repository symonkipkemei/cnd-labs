# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# option 1

# change to a set
unique_date  = set(list_)
print(unique_date)

# option 2

#new list
new_list = []
for num in list_:
    # before inserting a number check if number already in new list
    if num not in new_list:
        # append no in original to new list
        new_list.append(num)
    # if it is already there ignore

print(new_list)