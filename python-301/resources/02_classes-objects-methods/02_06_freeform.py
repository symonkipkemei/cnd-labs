# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


#animals
#we can model animals around classes based on where they live
#sea/lake/ocean
#land
#air


class WaterOrganisms:
    def __init__(self,name,type,habitat,reproduction,size,food) -> None:
        self.name = name
        self.type = type
        self.habitat = habitat
        self.reproduction = reproduction
        self.size = size
        self.food = food
    def __str__(self) -> str:
        """fish description"""
        return f"""
        {self.name} is a {self.type}. 
        It leaves in {self.habitat} habitat
        It reproduces by {self.reproduction}.
        It is avaragely {self.size} pounds.
        They feed on {self.food}.
        """

    def __add__(self,other):
        """aggregating the size

        Args:
            other (int): size

        Returns:
            str: total weight description
        """
        total_size = self.size + other.size
        return f"combined size : {total_size}"



tilapia = WaterOrganisms("Tilapia","fish","warm waters","spawning,laying of eggs",2,"algae,pellets")
dolphin = WaterOrganisms("Dolphin","mammal","open oceans,gulfs,inlet bays,coastal ocean","give birth",110,"fish,shrimps,jellyfish and octopuses")

print(tilapia)
print(dolphin)


class Person:
    def __init__(self,name,sex,country,eyes_color,age,size,what_keeps_exicted) -> None:
        self.name = name
        self.sex = sex
        self.country = country
        self.eyes_color = eyes_color
        self.age = age
        self.size = size
        self.exicted = what_keeps_exicted
    def __str__(self) -> str:
        return f"""
        My name is {self.name} . I am {self.sex} and {self.age} years old. 
        I come from {self.country}.
        My eye color is {self.eyes_color}.
        I am avaragely {self.size} pounds.
        What keeps me exicited is {self.exicted}.
        """
    
    def __add__(self,other):
        """aggregating the size

        Args:
            other (int): size

        Returns:
            str: total weight description
        """
        total_size = self.size + other.size
        return f"combined size : {total_size}"


symon = Person("Symon Kipkemei","male","kenya","black",25,74,"The ability to think and execute")
brian = Person("Brian Mubothi", "male","Uganda","black",26,54,"politics")
risper = Person("Risper Chepkorir","female","Tanzania","blue",22,45,"To love and to be loved back")

print(symon)
print(brian)
print(risper)

total = dolphin + symon
print(total)


class Trees:
    def __init__(self,name,height,diameter,leaf_type) -> None:
        self.name = name
        self.height = height
        self.diameter = diameter
        self.leaf_type = leaf_type
    
    def __str__(self) -> str:
        return f"""
        I am {self.name}.
        My height {self.height} meters and diameter {self.diameter} meters.
        My leaf type is {self.leaf_type}
        """
    

mapera = Trees("mapera",500, 25,"broad leaves")
print(mapera)