# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


def decorator(func):
    def wrapper_func(args):
        output  = f"\n***************************** \n {args} \n*****************************"
        return output
        
    return wrapper_func



@decorator
def message_body(text):
    message = f"Welcome {text}"
    return message


print(message_body("Arch. Symon Kipkemei"))