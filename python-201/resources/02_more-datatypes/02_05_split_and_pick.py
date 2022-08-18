# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

#user word

user_string = input("Write a sentence of your choice: ")

#split sentence into words

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
            words_dict[word] = count
        #if not repeated , assign value of 0 
        else:
            count += 0
            words_dict[word] = count
    #reset count for the next word
    count = 0


#check which word has the highest value
value_list = []
for key, value in words_dict.items():
    value_list.append(value)


# sort list
value_list.sort(reverse=True)
print(value_list)
#highest value, first one in sorted list
highest_value = value_list[0]


# search word in dictionary based on value
for key, value in words_dict.items():
    if highest_value == value:
        print(f"The common word is {key}")
        break

        





