# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?



import pathlib

path = pathlib.Path("/home/fmd/pyfmd/cnd-labs/python-301/resources/05_exceptions/books")


try:
    # reading war and peace text 

    war_peace = ""
    with open("resources/05_exceptions/books/war_and_peace.txt","r") as f:
        lines = f.readlines()

    with open("resources/05_exceptions/books/crime_and_punishment.txt","w") as f1:
        f1.write(" ")


    for filepath in path.iterdir():
        with open(filepath,"r") as f2:
            line = f2.readline(1)
            print(line)
    

except FileNotFoundError:
    print('The path to the file is yet to be established....keep calm')

except IOError  as  e:
    print(f"The following error occured: {e} ; keep calm")

except Exception as ex:
    print(f"Untraced error : {ex} ; keep calm")

