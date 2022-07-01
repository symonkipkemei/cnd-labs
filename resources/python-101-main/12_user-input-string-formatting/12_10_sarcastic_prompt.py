# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

honest_opinion = str.lower(input("Insert your honest opinion: "))

inverted_honest_opinion = honest_opinion[:: -1]
print(inverted_honest_opinion)
word = ""
for index, letter in enumerate(inverted_honest_opinion):
    if (index %2) != 0:
        letter = str.upper(letter)
        word += letter
    else:
        word += letter
    

print(word)
