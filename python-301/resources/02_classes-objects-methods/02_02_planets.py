# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self,name:str,diameter:int,color:str,surface_temp:int,no_moons:int,rotation_days:int) -> None:
        self.name= name
        self.diameter = diameter
        self.color = color
        self.surface_temp = surface_temp
        self.no_moons = no_moons
        self.rotation_days = rotation_days
    def __str__(self) -> str:
        return f"""Planet {self.name} has a diameter of {self.diameter} kilometers .
The surface color is {self.color}.
{self.name} has {self.no_moons} moon(s) and it takes {self.rotation_days} days to revolve around the sun"""

    def has_life(self):
        if self.color == "blue":
            return True
        else:
            return False
    def bigger_than_earth(self):
        if int(self.diameter) > 12000:
            return f"{self.name} is bigger than Earth"
        else:
            return f"{self.name} is not bigger than Earth"
    



venus = Planet("venus",12500,"yellow",750,0,243)
mercury = Planet("mercury",4850,"orange",700,0,88)
earth = Planet("earth", 13000,"blue",300,1,365)
mars = Planet("mars",6790,"red",500,2,687)

print(mars)
print()
print(mars.bigger_than_earth())
print(earth)