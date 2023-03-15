def outer_func1():
    msg = "weekend"
    print(f"message {msg}")

    def inner_func():
        print(msg +"great")

    return inner_func




def outer_func(msg):
  
    def inner_func():
        print(msg +"great")

    return inner_func




inner = outer_func("BRYO the ")

inner()