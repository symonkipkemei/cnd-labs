# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.


class Door():
    def __init__(self,width,height,material) -> None:
        self.height = height
        self.width = width
        self.material = material


class FanlightDoor(Door):
    def __init__(self, width, height,material) -> None:
        super().__init__(width, height,material)
        self.fanlight = True
        self.fanlight_height = 300
        self.panelheight = self.height-300
        


door1 = Door(800,2100,"timber")
door2 = FanlightDoor(800,2100,"mahogany")

height = door2.panelheight
print(height)