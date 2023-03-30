


def decorator_func(initial_func):
    def wrapper_func(name):
        print("the wrapper function has picked some ____________")
        return initial_func(name)
    
    return wrapper_func







@decorator_func
def prettify(name):
    return f"{name} flowers for you"


print(prettify("symooooon!"))