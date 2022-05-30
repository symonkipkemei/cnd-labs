
def conditionals_overview():
    # control flow
    # conditional statments
    # loops

    print("control flow")

def if_elif_else_statement():
    # code is executed from top to bottom in python
    # identation after control flow statement
    # elif and else depend on if to exist
    # if can exist on it's own

    # if one catches the rest are skipped

    import random

    jobs = ["architecture", "coding", "bim modelling"]
    input = random.choice(jobs)

    if input == "architecture":
        print("It must be nice to design buildings")

    elif  input == "coding":
        print("how does it feel to understand the language of a computer?")

    elif input == "bim modelling":
        print("is your career not boring? is it not repetitive?")

    else:
        print("print you have no career")


def flag():
    "using the state of a boolean value to decide what happens next in a conditional flow statment"

    correct = False

    if correct == True:
        print("congratulations")
    

def loop():
    "decipher a message sandwich btween numbers"

    secret = "2349H30023388281E3299371l1l3094842O0333322883"
    sol = ""

    # pick each character
    for char in secret:
        # determine if char is an alphabet
        if char.isalpha() is True:
            sol += char

    print(sol)


    """ create your name with alternating text sizes"""

    name = "symon kiplelgo"
    new_name = ""

    # remove spaces

    for index in range(len(name)):
        if name[index] != " ":
            new_name += name[index]

    print(f"The name without spacing is : {new_name}")

    twisted_name = ""
    # twisted alphabet
    for index in range(len(new_name)):
        if (index % 2) == 0:
            spec = new_name[index].upper()
            twisted_name += spec

        else:
            twisted_name += new_name[index]

    print(f"The twisted name is : {twisted_name}")


    
def range_function():

    # minus the character it stands for
    for x in range(5):
        if x % 2 != 0:
            print(x)


range_function()