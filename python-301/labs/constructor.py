class Ingredients:
    "creating ingredients class"

    #the constructor method, gets implicitly called when you are instantiating an object
    def __init__(self):
        self.name = "carrots"
        self.amount = "orange"
        self.size = "big"

new = Ingredients()
print(new.name)


i = Ingredients()
print(i.name, i.amount, i.size)
