


#writing to a file
with open("file.txt", "a") as trial:
    trial.write("4 \n")

# reading a file
with open("file.txt", "r") as file:
    contents = file.read()
    print(type(contents))
