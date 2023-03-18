# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

# determine the index of the characters in variable s
for index, x in enumerate(s):
    print (index, x)

# pick them out

apple = s[7:12]
egg = s[26:29]
butter = s[57:63]
floor = s[68:73]

print(apple, egg, butter, floor)


print(s[::-1])
