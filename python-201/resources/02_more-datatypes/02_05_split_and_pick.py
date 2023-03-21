# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

#user word

user_string = input("Write a sentence of your choice: ")

#split sentence into words via spacing

words =user_string.split(" ")


# the number of times the word appears
count = 0

#store the words (keys) and their count (value)
words_dict = {}

# pick one word
for word in words:
    # check if word is repeated elsewhere in the sentence, if true add a value
    for y in words:
        if word == y:
            count += 1
            
    #reset count for the next word
    words_dict[word] = count
    count = 0


word_dict_sorted = {bundle[0]:bundle[1] for bundle in sorted(words_dict.items(),key= lambda v:v[1], reverse=True)}
#sort the dictionary by value

longest_word = next(iter(word_dict_sorted))

print(f"common word: {longest_word}")


        





