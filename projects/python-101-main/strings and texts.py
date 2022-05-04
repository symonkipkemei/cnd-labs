# data type string
# enclosed by quotation marks
# do not mix them
# strings are not single pieces of information like a number,
# python thinks of a string as a sequence of characters.


# python should thefore know;


# how many characters are there
# how many are they


#ERROR MESSAGES
# read them from bottom up
3

#Thnings you can do withh strings
# 1. length/number of characters
# 2. concatenation ( plus operator on strings perform concatentation)
# 3. string indexing ( zero based numbering concept)
# 4. Positive/Negative indexing
# 5. slicing
# 6. string methods


name = "symon"
print(name[0])


def hohoho():
    
     """"
    Tasks
    Use the playground below to print a new string that impersonates the Santa Claus 
     impersonator from your local shopping mall by saying hohoho. 
    You can only use the provided string! Pick out the relevant characters and
     concatenate them in order to print out the new word."""

    #create "hohoho" from variable below
    santa = "hello"

    # pick right characters from string
    h = santa[0]

    len_santa = len(santa)
    o = santa[len_santa-1]

    print(h + o + h + o + h + o)

def picking_strings():
        """"
    Task
    Pick as many words as possible from the word below
    s = "plumage"
    """
    s = "plumage"

    print(s[::-1])

    print(s[0:4])
    print(s[-4:])



##STRING METHODS
# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

user_input = input("type something to win")
user_input = user_input.lower()

if user_input == "something":
    print("Congratulations, you won!")
else:
    print("you got it wrong")

t = "word"
print(t[-1])



