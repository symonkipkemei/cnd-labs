def greet(greeting = "Hi", name = "user"):
    """Generates a greeting

    Args:
        greeting(str): The greeting to use, e.g. "hello"
        name(str): Name of the recipent you want to greet

    Return:
        A personalized greeting
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence


print(greet.__doc__)
message = greet("Hello","love")
print(message)
def love(*lovers):
    for hubby in lovers:
        print(hubby)


love("kip", "martha", "shamye", "rathio")

def penzi(**lombotove):
    print(lombotove)

penzi(love = "mapenzi", anger = "hasira", uvumulivu = "patience")


#we want to greet many users at once:
def greet_many(greeting,**args):
    greetings = ""
    for key,name in args.items():
        for x in name:
            sentence = f"{greeting},{x}! How are you!"
            greetings += sentence + "\n"
    return greetings

mesaage = greet_many(greeting = "hey dear", args=["kipchumba","lawi","rose","sammy"] ,)
print(mesaage)



def hehe(leo, kesho):
    """The code does the folloeing            

    Args:   
        leo(_type_): _description_
        kesho (_type_): _description_

    Returns:
        hello: None
    """
    return None
    
    
def herty():
    """The code does as follows

        
    """ 
