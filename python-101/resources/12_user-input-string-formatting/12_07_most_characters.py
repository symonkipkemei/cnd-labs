# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


string = []
number_of_items = int(input("Insert Number of items: "))
for x in range(0,number_of_items):
    user_inpt = input("insert a string: ")
    string.append(user_inpt)
check = number_of_items -1
count = 0
for word in string:
    word_length = len(word)

    for variable in string:
        variable_length = len(variable)
        if word_length != variable_length:
            if word_length > variable_length:
                largest_length = word_length
                largest_word =word
                count += 1
                print( word, word_length,count)

    if count >= check:
        print(largest_length, largest_word)
        break

        

        



