# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"

month = "december"
#month = tuple(month)
print(month)
code = tuple(string)
print(type(code))
print(code)

for x in code:
    print(x)


for y in month:
    print(y)