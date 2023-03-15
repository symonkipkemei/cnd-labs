


class Handshake():

    def __init__(self,name,country) -> None:
        self.name = name
        self.country = country

    def __call__(self):
        print(f"Hello {self.name}. Welcome to {self.country}")


greet = Handshake("SYMON","KENYA")


def say_hi():
    print("Hiii...")

    return "yes"

def say_moo():
    print("Moooooooooooo!!")

    return "yes"



#greetingsA = [say_hi(),say_moo()]

#greetingsB = [say_hi,say_moo]

greet()