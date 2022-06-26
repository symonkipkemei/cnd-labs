# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4



message = input("Input your love message to your darling:")
while True:
    letter = input("which letter should I check?: ")
    if letter in message:
        index = message.index(letter)
        print(index)
        break
    else:
        print("Letter not available")

