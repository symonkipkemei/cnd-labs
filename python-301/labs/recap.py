#what is a class

# a class is a blueprint of an object

#how do we create classes

#how do we create methods and attributes

#how do we identify classes

#what are the characteristics of classes\

#how do we name a class

#the constructor method
#what is self

#what is an object 
#_____________________________________________________________________________
#we are going to create a car object


#HARD CODED CLASS
#_________________________________________________
class CarModel:
    #assigning values to self variables(attributes)
    def __init__(self):
        self.shape = "round"
        self.wheels = "four"
        self.color = "brown"
        self.engine = "2000cc"
        self.year = "2005"
    
   

#an insatnce of a class
vitz = CarModel()
print(vitz.color)
print(vitz.year)


#CLASS WITH ATTRIBUTES
#_________________________________________________

class CarModel():
    #attributes
    #assigning values(arguments) to self variables(attributes)

    def __init__(self,shape,wheels,color,engine,year):
        self.shape = shape
        self.wheels = wheels
        self.color = color
        self.engine = engine
        self.year = year
    
    def __repr__(self) -> str:
        return "This is still a car"

    def has_speed(self):
        if self.engine == "2000cc":
            return True
        else:
            return False



benz = CarModel("rectangle",6,"black","2000cc", 2019)
vitz = CarModel("box",4,"brown","1500cc",2030)
print(vitz)
print(benz.wheels)

print(vitz.has_speed())