


# there are several types of errors
# syntax errors caused by code problems
# exceptions which can be avoided ,caused by a problem that occurred during runtime


#anticpation of problems with raise
def class1():
 try:
     num = int(input("Enter a number: "))
    
 except:
     print("You didn't enter a number!")
     #catches all the errors because the error was not specified

 print("symon do not give up yet, do you remember quoting akina diana as variables")
   


def class2():
   # good practice to be specific as possible

   try:
       num = int(input("Enter a number: "))
    
   except ValueError:
       print("You didn't enter a number!")
       #catches all the errors because the error was not specified



def class3():
   try:
      
       dividend= int(input("Please insert a number to be divided:"))
       divider= int(input("Please enter a divider:"))

       result = dividend/divider

       print(f"The result of {dividend} divided by {divider} is {result}")
   except ValueError:
       print("you did not enter a number")

   except ZeroDivisionError:
      print("go back to primary school please")

   except Exception as e:
      #catch any exceptions that might occurr
      print(f"please remain calm, the following trouble ocuurred {e}")

   else:
      print("proud of you son, you are great")

   finally:
      print("great job")
      


def class4():
   #raising exceptions


   print("symon")

   raise ValueError

   #the rest of the code will nort execute when the value error is raised


   print("kipchumba")  



def class5():
    #raising exceptions

    age = int(input("age: "))

    if age < 0:
       raise ValueError('looks like you were not born yet')


def class6():
    #user input is converted into an integer even though it might be a negative number

    age = int(input("age: "))
    print(age)



class AgeError(Exception):
   def __init__(self,age) -> None:
      self.age = age

   def __str__(self) -> str:
       print(f"You cannot retrograde your age {self.age}")




class AgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"You'll be born in {abs(self.age)} years."

def class7():
   age = int(input("Age: "))


   if age < 0:
       raise AgeError(age)

   try:
       if age < 0:
           raise AgeError(age)
   except AgeError as ae:
       print(ae.message)




x = 10
y = 0

try:
    result = x / y
    print(result)
except Exception as e:
    print("An Exception was raised")
except ZeroDivisionError as zde:
    print("You cannot divide by zero")
finally:
    print("In finally block")