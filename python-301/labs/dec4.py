def weather(weather):
    return f"Today is {weather}"

def deorator_func(initial_func):
    def wrapper_func():
        print("The wrapper function picked some.....")
        return initial_func()
    return wrapper_func



def pretiffy():
    print("flowers")


decorated_prettify = deorator_func(pretiffy)
decorated_prettify()