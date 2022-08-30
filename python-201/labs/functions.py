def greet(greeting: str, name: str) -> str:
    """Generates a greeting

    Args:
        greeting(str): The greeting to use, e.g. "hello"
        name(str): Name of the recipent you want to greet

    Return:
        A personalized greeting
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence


print(greet.__doc__)
message = greet("Hello","love")
print(message)
def love(*lovers):
    for hubby in lovers:
        print(hubby)


love("kip", "martha", "shamye", "rathio")

def penzi(**lombotove):
    print(lombotove)

penzi(love = "mapenzi", anger = "hasira", uvumulivu = "patience")


