# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.






#greeting function
def greet(greeting: str, name: str)->str:
    """Generates a greeting

    Args:
        greeting(str): The greeting to use, e.g. "hello"
        name(str): Name of the recipent you want to greet

    Return:
        A personalized greeting
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence



#write letter
def write_letter(name: str)-> str:
    """A love letter to my ex

    Args:
        name (str): The name of my ex

    Returns:
        str: A message to my ex
    """


    greeting = greet("Hello beloved",name)
    text = """\nIt's been ages and centuries since I last saw you\nI miss you dearly.Had it not been for your lack of enthusiasim and vibes,\nwe would still be together.I moved on dear one.I am now in a love affair with python.\nI hope you doing well too!\n\n"""

    bye = f"Goodbye my lombotove {name}"

    letter = greeting + text + bye

    return letter


msg = write_letter("Architecture")
print(msg)