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

print(greet("Hello", "Duncan"))
print(greet("hey", "Symon kipkemei"))
print(greet("35", "Sammy"))
print(greet("Hi", "Kipkemei"))
print(greet("True", "True"))

print(name)