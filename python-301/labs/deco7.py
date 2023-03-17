# create a decorator


import random
import time

def decorator_func(intial_func):
    def wrapper_func():
        choices = ["noisy", "untidy and arrogant", "sharp and deligent", "handsome and hardowrking"]
        chosen = random.choice(choices)
        print(chosen,end=" ")
        return intial_func()
    return wrapper_func


def time_it(initial_func):
    def wrapper_func(args):
        now = time.time()
        print(f"{now}:",end=" ")
        return initial_func(args)
    return wrapper_func



# define functions
@time_it
def student(name):
    print(f"student: {name}")


@decorator_func
def teacher():
    print("Musau Kimeu")

@decorator_func
def matatu_driver():
    print("jEFFERZON")

@decorator_func
def mjengo():
    print("Maasai")


student("kipchumba")
teacher()
matatu_driver()
mjengo()