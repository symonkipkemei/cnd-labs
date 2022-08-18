# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

# pick a text from the use

user_text = input("Insert your text: ")
# create a dictionary

user_dict = {}

# create a count as value
count = 0
# pick letter from the text


for letter in user_text:
    # check if letter already in dict
    if letter in user_dict.keys():
        for key ,value in user_dict.items():
            # add a count of 1, to the already existing letter
            if key == letter:
                value += 1
                user_dict[key] = value
                break
               
    else:
        # add new letter to the dict
        count += 1
        user_dict[letter] = count

    #reset count to 0 for the next letter
    count = 0



    




print(user_dict)

