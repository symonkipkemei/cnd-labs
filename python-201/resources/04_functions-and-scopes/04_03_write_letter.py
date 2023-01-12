# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.




def write_letter(name: str)-> str:
    """A love letter to my ex

    Args:
        name (str): The name of my ex

    Returns:
        str: A message to my ex
    """
    greeting =f"Hello beloved {name}\n\n"
    text = """It's been ages and centuries since I last saw you\nI miss you dearly.Had it not been for your lack of enthusiasim and vibes,\nwe would still be together.I moved on dear one.I am now in a love affair with python.\nI hope you doing well too!\n\n"""

    bye = f"Goodbye my lombotove {name}"

    letter = greeting + text + bye

    return letter


msg = write_letter("Architecture")
print(msg)

print(write_letter.__doc__)