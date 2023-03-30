def lowercase(func):
    "a decorator that avoids digital screaming"

    def wrapper(text):
        inital_result = func(text)
        new_result = inital_result.lower()

        return new_result
    return wrapper


@lowercase
def say_something(text):
    return text

@lowercase
def user_name(text):
    user = text + " " + "COMRADE"
    return user

print(say_something("HELLO ASSMIOOO"))


print(user_name("KIPKEMEI KIPLELGO SYMON"))



class Car():

    def __init__(self,name,color,engine) -> None:
        self.name = name
        self.color = color
        self.engine = engine

    def __call__(self):
        print(f"This car is a {self.color} {self.name} with engine power of {self.engine} cc")

    def __str__(self) -> str:
        print("This is a car")
        



MERCDES = Car("MERCIDEZ","BLACK","1600")

MERCDES()
