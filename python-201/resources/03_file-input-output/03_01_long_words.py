# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

import csv
#open up the file
with open("resources/03_file-input-output/words.txt","r") as f:
    # write a reader object
    file_obj = csv.reader(f)
    list_obj = list(file_obj)
    for word_list in list_obj:
        word = word_list[0]
        if len(word) > 20:
            print(word)
