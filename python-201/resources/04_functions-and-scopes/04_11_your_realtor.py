# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.


def real_adv(**kwargs:str)-> dict:
    """Real estate advertisments formated nicely

    Args:
        **kwargs (str): advertisments

    Returns:
        dict: a combination of different advertisments
    """
    combination = {}

    for key, values in kwargs.items():
        combination[key] = values
    
    return combination


adv = real_adv(maison = "Nyumba yako,nyumba yetu.",commercial="Make money, make more money",hospital="Nice hospital")

print("A real estate advertisment")
for key, value in adv.items():
    print(f"{key}:{value}")