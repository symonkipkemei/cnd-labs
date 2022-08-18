# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


user_string = input("Insert a string: ")

# split string  into words
user_words = user_string.split(" ")


#result_list
result_list = []
# tuple
user_alphabets = []
# split word into alphabets
for word in user_words:
    for alphabet in word:
        user_alphabets.append(alphabet)
    #after splitting word,convert to tuple and store in result list
    user_aplhabet_tuple = tuple(user_alphabets)
    result_list.append(user_aplhabet_tuple)
    #reset alphabet list for the next word
    user_alphabets = []


print(result_list)
        
        

