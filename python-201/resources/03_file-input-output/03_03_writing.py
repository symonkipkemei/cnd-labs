# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
import csv

#create a list to store the inverted word
inverted_words = []
#read the words 
with open("/home/fmd/cnd-labs/python-201/resources/03_file-input-output/words.txt", "r") as w:
    reader_object = csv.reader(w)
    #convert the iterable to a 2d list
    word_2d_list = list(reader_object)

    #pick the words
    for word_1d_list in word_2d_list:
        #abstract word from the list
        word = word_1d_list[0]
        #invert the word
        word_inverted = word[::-1]
        inverted_words.append(word_inverted)

# store the word ina new list
with open("/home/fmd/cnd-labs/python-201/resources/03_file-input-output/words_reverse.txt", "w") as w:
    #convert the iterable to a 2d list
    for word in inverted_words:
        w.write(word + "\n")

    