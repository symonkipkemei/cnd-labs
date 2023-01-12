# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


import csv

#parameters are the words and their length

# create a dictionary to store the word and dict
store_dict = {}


# loop through the word list, assign items to the dict
with open("/home/fmd/cnd-labs/python-201/resources/03_file-input-output/words.txt", "r") as w:
    reader_object = csv.reader(w)
    #convert the iterable to a 2d list
    word_2d_list = list(reader_object)

    #pick the words
    for word_1d_list in word_2d_list:
        #abstract word from the list
        word = word_1d_list[0]
        len_word = len(word)

        # store word and length in dict
        store_dict[word] = len_word
#list to store the values
value_list = []

# total length of characters
total_char = 0
# sort the values in the txt, pick the most and the least
for value in store_dict.values():
    value_list.append(value)
    total_char += value

# sort the value list
value_list.sort()

#pick the longest/shortest word lenths

shortest_word_len = value_list[0]
longest_word_len = value_list[-1]

#pick the longest word(s), store in list
longest_words = [key for key, value in store_dict.items() if value == longest_word_len]

#pick the shortest word(s), store in list
shortest_words = [key for key, value in store_dict.items() if value == shortest_word_len]

print("\nThe shortest words are:")
for word in shortest_words:
    print(word,end=" ")

print("\n")

print("\nThe longest words are:")
for word in longest_words:
    print(word,end=" ")

print("\n")

print("\nThe total length of words is:")
print(total_char)