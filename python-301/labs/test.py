

class AgeError(Exception):

    pass
    

age = int(input("Age: "))

if age < 0:
    raise AgeError(age)