# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def close_names(func):
    def wrapper(*args,**kwargs):
        ans = func(*args,**kwargs)
        return f'"{ans}"'
    return wrapper
    

@close_names
def message(name):
    return name

print(message("Love is a beautiful thing"))