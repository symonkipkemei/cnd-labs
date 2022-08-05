set = {8, 9, 1, 2, 3, 2, 5, 6, 3}
print(set)

set_2 = {"mango", "apple", "banana", "quava", "banana"}
print(set_2)

set_1 = {8, 9, 1, 2, 3, 2, 5, 6, 3}
set_2 = {"mango", "apple", "banana", "quava", "banana"}

set = set_1.union(set_2)
print(set)

set = set_1.update(set_2)
print(set_1)