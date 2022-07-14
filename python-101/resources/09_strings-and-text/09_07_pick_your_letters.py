# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
w = word[1]
e = word[2]
s = word[-2]
t = word[0]
r = word[-3]
space = word[-1]

print( w + e + space + s + e + e + space + t + r + e + e + s)