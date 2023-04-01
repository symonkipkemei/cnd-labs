# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.


import pathlib
path = pathlib.Path.cwd()

for filepath in path.iterdir():
    print(filepath.name)

    