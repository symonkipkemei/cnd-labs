def outer_func():
    msg= "Are we on the same page?"

    def inner_func():
        print(msg)

    return inner_func


outer_func()
outer_func()()

