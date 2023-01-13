# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math
class Rectangle:
    def __init__(self,length, width) -> None:
        self.length = length
        self.width = width
        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)
    
    def __add__(self,other):
        combined_area = self.area + other.area
        return f"combined_area: {combined_area}"

    

class Circle:
    def __init__(self,radius) -> None:
        self.radius = radius
        self.perimeter = 2 * math.pi * self.radius
        self.area = math.pi * (self.radius * self.radius)


    def __add__(self,other):
        combined_area = self.area + other.area
        return f"combined_area: {combined_area}"

    

 #instantiate an object
rec = Rectangle(8,4)
circle = Circle(14)

print(circle.area)
print(circle.perimeter)

print(rec.perimeter)
print(rec.area)

ca = rec + circle
cb = circle + rec
print(ca)
print(cb)