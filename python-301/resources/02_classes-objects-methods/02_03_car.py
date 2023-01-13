# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:

    def __init__(self,model:str,year:int,max_speed:int) -> None:
        self.model = model
        self.year = year
        self.max_speed = max_speed
    
    def increase_speed(self):
        multiplier = 5
        self.max_speed = self.max_speed * multiplier
    
    def __str__(self) -> str:
        return f"{self.model} was manufactured in the year {self.year}. It has a maximum speed of {self.max_speed} km/h"


vitz = Car("Toyota vitz", 2006, 180)
v8 = Car("Toyota landcruiser v8",2015,240)

print(v8)
print()
v8.increase_speed()
print(v8)