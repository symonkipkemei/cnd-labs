# With the given sets `s` and `t`, demonstrate how you can:
# - Create an intersection of both sets
# - Create a union of both sets

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}


# two different lists
list_A = ["a", "b", 1, 5, 7, 9]
list_B = [4, 3,"d", 5, 8, 9, "l", "g"]


# convert to sets
set_A = set(list_A)
set_B = set(list_B)


# if sets difference is empty , then the list have same items
set_difference = set_A - set_B

if len(set_difference) == 0:
    print("The lists has same value")
else:
    print("The lists are different")