# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


def make_sandwich(breadtype: str,*args: list) -> str:
    """A sandwich maker with different types of toppings

    Args:
        breadtype (str): Type of bread
        *args (list): toppings

    Returns:
        str: A sandwich
    """
    top_sandwich = breadtype
    bottom_sandwich = breadtype
    toppings = ""

    for topping in args:
        toppings += topping + ","

    sandwich = f"A top {top_sandwich},with: {toppings}and bottom {bottom_sandwich} sandwich"
    return sandwich


pina_sandwich = make_sandwich("festive bread", "pineapple", "mango","cider","corridanah","oninions")
print(pina_sandwich)