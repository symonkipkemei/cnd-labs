#G0 GETTER SUB PROGRAMS


#if the user happens to find the sword, assign variable to one
sword = 0
def player_name():
    """Collect user_name and welcome him/her to the game"""
    player_name = input("What's your name ? : ")

    print(f"Welcome {player_name} to the command line game.Have fun!")

    return player_name


def door_choices():
    print("There are two doors\n(1). Left door\n(2). Right door")
    door_choice = int(input("Make your choice: "))

    return door_choice

def left_door():
    print("Oops! You've entered an empty room")

def right_door():
    print("Booom !! I am the dragon, I am going to eat you !!")
    

def option():
    """You have an option of interacting further or return to previous room"""
    print("\nYou have two options\n(1). Interact further\n(2). Run to the previous room")
    user_option = int(input("Make your choice: "))

    return user_option

def option_further_right():
    print("\nYou have two options\n(1).fight\n(2).Run to the previous room")
    user_option = int(input("Make your choice: "))
    return user_option

def option_further_left():
    """Option further"""
    print("\nYou have two options\n(1).Look around\n(2). Run to the previous room")
    user_option = int(input("Make your choice: "))
    if user_option == 1:
        return user_option
    elif user_option == 2:
        return

def sword_found():
    """Sword found"""
    print("\nYou have found a sword!\n(1).Take it\n(2). Leave it")
    user_option = int(input("Make your choice: "))
    if user_option == 1:
        sword = 1
        return sword
    elif user_option == 2:
        sword = 0
        return sword

def main():
    sword = 0
    player_name()
    return_previous_room = True
    while return_previous_room:
        door_choice = door_choices()
        if door_choice == 1:
            left_door()
            user_option = option()
            if user_option == 1:
                further_option = option_further_left()
                if further_option == 1:
                    sword = sword_found()
                elif further_option == 2:
                    return_previous_room = True
                
        elif door_choice == 2:
            right_door()
            user_option = option()
            if user_option == 1:
                further_option = option_further_right()
                if further_option == 1:
                    if sword == 1:
                        print("You've won ! congratulations!")
                    
                    elif sword == 0:
                        print("you've lost")
                    return_previous_room = False

                elif further_option == 2:
                    return_previous_room = True
        else:
            print("Try again")

    

main()


        

        


        
        




    
    

    




        

