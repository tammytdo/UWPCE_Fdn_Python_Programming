"""

Foundations of Python
UW Continuing Education
Modules 7-9

Study notes

"""
"""
from copy import deepcopy


# How to copy things (Object References)
# Looking at memory behind the scenes
x = 3
y = x
print(id(x), id(y))
#4297644480 4297644480

# Shallow Copy
colours1 = ["red", "blue"]
colours2 = colours1[:]

print(colours1)
# ['red', 'blue']
print(colours2)
# ['red', 'blue']
print(id(colours1), id(colours2))
# 4366795656 4368173448

colours2[1] = "green"

print(colours2)
# ['red', 'green']
print(colours1)
# ['red', 'blue']
print(id(colours1), id(colours2))

colours2 = colours1[:]
print(id(colours1))
# 4364525768
print(id(colours2))
# 4366798216

# Deep Copy
colours1 = ["red", "blue"]
colours2 = deepcopy(colours1)
print(colours1)
print(id(colours1))
print(colours2)
print(id(colours2))

# Installing Modules
# Importing Modules
# Importing functions from a Module
# Module Namespace
# dir() function
# help() function
# Executing Modules as Scripts (if name = main)
# Module Search Path

print()


# Module 8
# Basics of Object Oriented Programming
# Objects
# Classes
# Basic Syntax
# Instance Attributes


class Critter():

    # Creating a Constructor (Initialization Method)
    def __init__(self, name):
        # name is an attribute of the Critter class
        self.name = name
        print("A new critter named {} has been born!".format(self.name))

    # define a method, using the self parameter
    def talk(self):
        print("Hi, my name is {}. I'm an instance of the class Critter.".format(self.name))

    # using python's __str__ method
    # Creates a string that will be printed when someone prints the Class name
    def __str__(self):
        rep = "Critter object...\n"
        rep += "__str__ method: {}".format(self.name)
        return rep


print()

# Instantiating a class
# We've added an argument to init, so this must be passed when instantiating the class
print("BENJAMIN STUFF")
Benjamin = Critter(name= "Benjamin")
Benjamin.talk()
print("Printing just Benjamin:", Benjamin) # __str__ method
print("Printing Benjamin.name:", Benjamin.name)

print()

print("SCOOBY STUFF")
Scooby = Critter(name= "Scooby")
Scooby.talk()
print("Printing just Scooby:", Scooby)  # __str__ method
print("Printing Scooby.name:", Scooby.name)



# Python Special Built-In Functions
# __str__ method
    # Creates a string that will be printed when someone prints the Class name

# __repr__ method
    # Similar to the string method, but more for developers as it is often used for debugging

import datetime
now = datetime.datetime.now() 

print("Str:", str(now))
print("Repr:", repr(now))

#  __dict__ method
    # View all the attributes for a class

print(Scooby.__dict__)

# What other methods are available?
print(dir(Scooby))

"""

# OOP- Classes and Methods
# Class attributes
    # Attributes that belong to the class itself, and not an instance of the class
    # total = 0

# Static Methods
    # Similar to class attributes, these are functions that belong to the class, and not to any particular instance of the class

class Critter():
    
    total = 0
    
    def __init__(self, name):
       # name is an attribute of the Critter class
        self.name = name
        print("A new critter, {}, has been born!".format(self.name))
        Critter.total += 1
    
    # define a method, using the self parameter
    def talk(self):
        print("Hi. I'm {}".format(self.name))
    
    # using python's __str__ method
    def __str__(self):
        rep = "Critter object\n "
        rep += "name: {} \n".format(self.name)
        return rep

    @staticmethod
    def status():
        print("There are {} critters".format(Critter.total))



crit1 = Critter("Fred")
crit1.talk()
print("Fred")
print(crit1.total)

crit2 = Critter("Sally")
crit2.talk()
print("Sally")
print(crit2.total)

static_crit = Critter("Jimbo")
static_crit.talk()
print(static_crit)
Critter.status()

static_crit2 = Critter("Schubert")
static_crit2.talk()
print(static_crit2)
Critter.status()


# Exception Handling
# Try/Catch and Raising Exceptions¶
# try:
#     12/0
# except ZeroDivisionError:
#     print("I don't think so")
#     raise ZeroDivisionError


#Try/Catch with Multiple Exceptions¶
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!")
except IOError:
    print("Error: can't find file or read data.")
except SyntaxError:
    print("What are you even putting here?")
else:
    print("Written content in the file successfully.")


# Try/Catch with Functions¶
# def divide_things(num1, num2):
#     try: 
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("You totally can't divide by 0.")
#         raise ZeroDivisionError

# divide_things(6, 0)

# my_bf = "Alex"
# # Assert
# assert my_bf == "Ryan Gosling"


def kelvin_to_fahrenheit(temperature):
    assert (temperature >= 0), "Colder than absolute zero!"
    return ((temperature - 273) * 1.8) + 32

print(kelvin_to_fahrenheit(273))
print(int(kelvin_to_fahrenheit(505.78)))
# print(KelvinToFahrenheit(-5))




