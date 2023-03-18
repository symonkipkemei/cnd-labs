# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"



def files_test(file):
    x = file.endswith(".pdf")
    if x is True:
        print(f"{file} is pdf")
    else:
        print(f"{file} is not pdf")

def trial():
    txt = "Hello, welcome to my world."
    x = txt.endswith("my world.")
    print(x)



files_test(file_1)
files_test(file_2)
files_test(file_3)
files_test(file_4)



trial()