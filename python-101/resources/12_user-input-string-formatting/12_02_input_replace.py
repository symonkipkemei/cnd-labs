# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


message = str.lower(input("write your message champ: "))
symbol = input("insert you symbol: ")

first_letter = message[0]

new_message = message.replace(first_letter,symbol)
print(new_message)


print("\nDifferent verison\n")
# identify the first letter
for letter in message:
    if letter == message[0]:
        key_letter = letter
print(key_letter)
# replace alloccurencies with the letter identified
word = ""
for letter in message:
    if letter == str.upper(key_letter) or letter == str.lower(key_letter):
        letter = symbol
        word += letter
    else:
        word += letter

print(word)