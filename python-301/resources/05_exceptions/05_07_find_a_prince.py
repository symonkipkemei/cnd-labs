# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


import pathlib

path = pathlib.Path("/home/fmd/pyfmd/cnd-labs/python-301/resources/05_exceptions/books")


class PrinceException(Exception):
    pass


try:
    for filepath in path.iterdir():
        with open(filepath,"r") as f2:
            line = f2.readlines(100)
            if "Prince" in line[0]:
                raise PrinceException

              
        
        

    
except PrinceException as p:
    print(f"Prince found in the first 100 Words")

except FileNotFoundError:
    print('The path to the file is yet to be established....keep calm')

except IOError  as  e:
    print(f"The following error occured: {e} ; keep calm")

except Exception as ex:
    print(f"Untraced error : {ex} ; keep calm")

