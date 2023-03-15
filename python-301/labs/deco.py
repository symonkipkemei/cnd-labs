def lowecase(func):
    """A decorator that avoids digital screening

    """

    def wrapper(text):
        initial_result= func(text)
        new_result = initial_result.lower()
        return new_result
    return wrapper


@lowecase
def say_something(text):
    return text

print(say_something("HEY WHATSAPP?"))


@lowecase
def greetings(name):
    greetings = "Good morning ANGEL" + " " + name + ". You look GREAT!"
    return greetings


print(greetings("symon"))
