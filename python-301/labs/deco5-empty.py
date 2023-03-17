

def greetings():
    msg = "hello world!"
    print(msg)
    return msg


def prettify():
    print("flowers")

def decorator_func(initial_func):
    def wrapper_func():
        print("The wrapper function picked some juicy", end=" ")
        return  initial_func()
    return wrapper_func



@decorator_func
def prettify():
    print("flowers for you")



@decorator_func
def food():
    print("apples and potatoes")


prettify()

food()