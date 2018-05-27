"""

Module 1 - Lab 2: Pseudocode, Printing and User Input

"""

# Our Goal
# We're going to create a script that is little more interactive than simply printing "Hello world!". 

# We're going to find out the user's name 
# We're going to find out the user's favorite color
# We're going to tell them our name
# We're going to tell them our favorite color. 
# Psuedocode
# We can use comments to create an outline for how we need to solve the problem. This method is called pseudocode, and it's how you should begin tackling every programming problem. 

# Let's look at the assignment again and break down what we need to do. 

# We're going to find out the user's name 
# We can break this down into pseudocode as: 

# # get the user to input their name
# # store that name as a variable
# User Input
# The input() method allows us to ask the user to enter information. From the console in PyCharm, type input() and see what happens. 

# input()
# Python pauses and waits for you (the user) to enter something. Type a word here, and notice that python returns it to you in quotes, showing you that it's taking whatever the user enters on the command line and converting it to a string (a data type used to store characters and letters). 

# Arguments
# You've now used two python functions; print and input. Functions are used to tell the computer to do something, such as "print this sentence". 

# However, functions alone don't do much. Type the following statement in your python console: 

# print()
# Exactly. 

# Functions tell python to do something, but in order to do something, we have to tell python what something we want them to operate on. We write that something, called an argument, inside the parenthesis: 

# print("This is my string")
# We can also do this:

something = "This is my string"

print(something)
# So we can now accomplish our pseudocode lines: 

# # store user name
user_name = input("Enter your name: ")  
# Printing
# We've already been working with the print statement, but there is so much more we can do with it. Try out the following code: 

veggie = "rutabaga"
cheese = "brie"
current_mood = "hungry"

print("Right now, I'm feeling pretty", current_mood)
print("My favorite veggie is {}".format(veggie))
print(cheese, "is my favorite!")
