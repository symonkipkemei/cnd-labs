

def a():

    a =2

    b = 42
    a += b

    pass


def b():
    my_list = [1, 23, 3, 5 ,42]

    new_list = []

    for x in my_list:
        breakpoint()
        x + 1
        new_list.append(x)

    print(new_list)


print("welocme to symon's programme")

def do_fun_stuff():
    a = 20
    print("Hello, nice meeting you")
    print("Goodbye")

    b = 30

    return a

final_value = do_fun_stuff()
breakpoint()
print(final_value)