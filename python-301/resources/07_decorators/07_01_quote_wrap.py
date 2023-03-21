# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def decorate_text(text:str):
    def wrapper_func():
        new_text = f"'{text}' " + "-kipkemei, symon"

        print (new_text)

        return new_text
    return wrapper_func



decorated_text = decorate_text("love is a mind game of hopless hearts")

decorated_text()