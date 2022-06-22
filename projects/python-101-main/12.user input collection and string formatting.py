
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

break_keyword()