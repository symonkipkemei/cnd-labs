# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.




import csv


# list
words = []
#open up the file

#pick words in the txt and append into one dimensional list
with open("resources/03_file-input-output/words.txt","r") as f:
    # write a reader object
    file_obj = csv.reader(f)
    list_obj = list(file_obj)
    for word_list in list_obj:
        word = word_list[0]
        words.append(word)


total_count = (len(words) -1)
shortest_count = 0
longest_count = 0
no_characters =0
info_dict = {"Shortest_word": 0, "longest_word":0,"Total_length":0}

for word_check in words:
    for word_comparison in words:
        if word_check != word_comparison:
            #declare length of each
            word_check_len = len(word_check)
            word_comparison_len = len(word_comparison)
            # check if the word is the shortest/longest by comparing with the rest of the words
            if word_check_len < word_comparison_len:
                shortest_count += 1
            elif word_check_len > word_comparison_len:
                longest_count += 1


    # assign the length of the word to dictionary
    if total_count == shortest_count:
        info_dict["Shortest_word"] = word_check_len
    elif total_count == longest_count:
        info_dict["longest_word"] = word_check_len

    # assign no of characters
    no_characters += len(word_check)
    info_dict["Total_length"] = no_characters

    #reset count
    shortest_count = 0
    longest_count = 0


#abstracting shortest word

# dict items
length_shortest_word = info_dict["Shortest_word"]
length_longest_word = info_dict["longest_word"]
total_length = info_dict["Total_length"]

# look for word with that length in the list
for word in words:
    if len(word) == length_shortest_word:
        print(f"shortest word : {word}")
    if len(word) == length_longest_word:
        print(f"longest word : {word}")

#print total length
print(f"total length : {total_length}")