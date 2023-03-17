
from datetime import datetime



def log_it(func):
    def wrapper(*args, **kwargs):
        result= func(*args, **kwargs)

        with open("activity.log","a") as f:
            f.write(f"{func.__name__} was called at {datetime.now()}\n")
        return result
    return wrapper


@log_it
def send_email(to,subject,message):
    pass
    

@log_it
def greet():
    print("Hello negros")

send_email("user@example.com","hello","how are you")

greet()