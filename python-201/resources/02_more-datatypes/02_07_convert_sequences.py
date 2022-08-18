# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tuple_string = tuple(string)
print(tuple_string)

string_list = list(string)
print(string_list)

string_list[0] = "k"
back_to_tuple = tuple(string_list)
print(back_to_tuple)
