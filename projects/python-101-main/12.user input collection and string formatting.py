
def user_input1():
    """Printing a blank user input"""
    user_input = input()
    word = ""
    for index,x in enumerate(user_input):
        print(index)
        if int(index)%2 != 0:
            x = str.upper(x)
        word += x
    print(word)



def user_input2():
    """user input taking on an argument"""

    user_input = input("insert a number: ")
    number = int(user_input) * 2
    print(number)



def while_loop():
    """It is important to declare the first varibale so that it compares its value with the variable on while loop"""
    name = None
    while name != "your name":
        name = input("Type your name: ")

    print("Finally!")





def break_keyword():

    while True:
        prompt = input("say something:")
        
        if prompt == "quit" or prompt == "exit":
            break
        else:
            print(prompt[::-1])
        
    print("nice one!")

def string_mini_language():
    '''Move string by certain position'''
    message = "you move me!"
    print(f"{message:>100}")

def string_concatenation():
    long_str = "check out this very long string that is full of wisdom \
    so you should definitely keep reading all the way to the end!"
    
    print(long_str)  # Prints in one line
    
    print(long_str)
    happy = "yes"
    
    love_message = ( f"you test so nice {happy} "
                "your hair is magestic but rough than wajackoyah's "
    f"you are so random {happy}"
    "you are so pretty than flowers"
    "the most exciting thing is we have the same energy levels to each another"
    "I hope this feeling grows and blossoms into sth beautiful")
    
    print(love_message)


def character_escaping():
    message = "cynthia is a beautiful girl, I like her a lot"
    print(message)
    
    message = "cynthia is a beautiful girl, I 'like' her a lot"
    print(message)
    
    message = "cynthia is a beautiful girl, I \"like\" her a lot"
    print(message)
    
    message = "cynthia is a beautiful girl, I \n\"like\" her a lot"
    print(message)


print(f"hello{'hello'}")
print(F"hello{'hello'}")
print("hello" + "hello")

print("hello{}".format(1 + 2))