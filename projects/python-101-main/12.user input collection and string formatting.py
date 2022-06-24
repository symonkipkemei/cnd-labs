
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


def command_line_game():
    player_name = input("What's your name ? : ")
    
    #welcome message
    print(f"Welcome {player_name} to the command line game.Have fun!")

    #door choices
    print("There are two doors\n(1). Left door\n(2). Right door")
    door_choice = int(input("Make your choice: "))

    if door_choice == 1:
        print("You've entered an empty room")
        print("Look around, there is a sword at the corner!")

        # sword options
        print("\n(1). Take sword\n(2). Leave the sword")


    elif door_choice == 2:
        print("Boom ! Am the dragon !! Fireeeeeeeee!!")
        print("\n(1). Take sword\n(2). Leave the sword")
    

    #options
    print("You have two options\n(1). Interact further\n(2). Run to the previous room")
    option_choice = int(input("Make your choice: "))

    
command_line_game()