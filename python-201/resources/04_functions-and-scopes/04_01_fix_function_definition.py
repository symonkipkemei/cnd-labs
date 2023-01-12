# The following function definition has a whole lot of bugs in it!
# Run the script and follow Python's error hints to fix them all.
# After your fixes, the function should allow you to take a name as an input
# and return a greeting message that you can save to a variable.

def say_hello(name:str) -> str:
        """ Say hello

        Args:
            name (str): Name of the recipient

        Returns:
            str: Greeting message
        """
        message = f"Hello {name}!"
        return message

greeting = say_hello("name")
print(greeting)
