# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.


filename = "operators.pdf"


if ".pdf" in filename:
    print('the file is a pdf')



for x in filename:
    correct = True

    if x == ".":
        print(correct)
    elif x == "p":
        print(correct)
    elif x == "d":
        print(correct)
    elif x == "f":
        print(correct)
    else:
        print(not correct)


