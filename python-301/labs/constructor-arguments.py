class Ingredients:
    "creating ingredients class"

    #the constructor method, gets implicitly called when you are instantiating an object
    def __init__(self ,name,amount,quantity_type):
        self.name = name
        self.amount = amount
        self.quantity_type = quantity_type

    def __str__(self) -> str:
        return f"There are {self.amount} {self.quantity_type} of {self.name}"

    def expire(self):
        self.name = "expired" + " " + self.name




a = Ingredients("carrots", 4, "piece")

b = Ingredients("sugar", 3, "table spoon")
c = Ingredients("water", 1, "litre")

a.expire()
print(a)
print(a, b, c)
print("mix")
print(f"{a.amount} {a.quantity_type} of {a.name}")
print("followed by ")
print(f" {b.amount} {b.quantity_type} of {b.name}")
print("followed by ")
print(f" {c.amount} {c.quantity_type} of {c.name}")





