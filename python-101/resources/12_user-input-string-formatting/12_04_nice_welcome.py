# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


user_name = input("Insert your name: ")


#version A
if " " in user_name:
    first_name = ""
    for letter in user_name:
        first_name += letter
        # space as full stop
        if letter == " ":
            break
    user_name = first_name

print(f"Hello {user_name}!, Welcome to my script")


#version B

split_name =user_name.split(sep=" ")
first_name = split_name[0]

print(f"Hello {first_name}!, Welcome to my script")