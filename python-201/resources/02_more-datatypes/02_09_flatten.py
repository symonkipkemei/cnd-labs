# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?


starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]


# brute force
#declare flatten list
flatten_list = []

#loop through the outer list
for item in starter_list:
    #check if item is a list
    if type(item) is list:
        #iterate through the list
        for element in item:
            flatten_list.append(element)

print(flatten_list)


# list comprehension
flat_list = [ item for sublist in starter_list for item in sublist]
print(flat_list)

