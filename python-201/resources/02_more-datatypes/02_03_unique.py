# Write code that creates a list of all unique values in a list.
# For example:
#
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

# convert list to a set
unique_list = set(list_)
print(unique_list)

# convert the set back to list via list compression

items = [items for items in unique_list]
print(items)
