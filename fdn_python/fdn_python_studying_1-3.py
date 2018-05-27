"""

Foundations of Python
UW Continuing Education
Modules 1-3

Study notes

"""


# split
jennys_number = "206-867-5309"
jennys_number.split("-")
print(jennys_number)
print(jennys_number.split("-"))

number_pieces = jennys_number.split("-")
print(number_pieces[0])
print(jennys_number.split("-", 1))
print(jennys_number.split("-", 1)[0])
print(jennys_number.split("-", 2)[:])

# replace
student = "tammi"
student = student.replace("i", "y")
print(student)

student = "tanny"
student = student.replace("anny", "elly")
print(student)

coffee = "covfefe"
coffee_happy = coffee.replace("vfef", "ffe")
print(coffee)
print(coffee_happy)

# concatenation
print("hello world")
a = "hello"
b = "world"
print(a + " " + b)

# creating a sequence of strings
print("cheese")
print("cheese, " * 5)

# fav_cheese = input("What is your favorite cheese?: \n")
# print(fav_cheese)

# string methods
print("hello world".upper())
print("hello world".lower())
print("hello world".swapcase())
print("hello world".capitalize())
print("hello world".title())
print("hello world".strip())
print("hello world".replace("l", "k", 2))
fav_cheese = "gouda"
new_cheese = fav_cheese.replace("goud", "Gorgonzola")
print(fav_cheese)
print(new_cheese)

first = "tammy"
mid = "t"
last = "do"

# Positional String Formatting
full_name = "{} {} {}".format(first, mid, last)
print(full_name.title())

# named formatting
full_name = "{first}{mid}{last}".format(first = first, mid = mid, last = last)
print(full_name.title())

# padding Strings
test_string = 10000000000
print("I have this much blah: {:,.2f}".format(test_string))
print("I have this much blah: {:,.3f}".format(test_string))

# Quotes Inside Strings
my_string = "this is my string!"
print(my_string)
my_kinda_string = "this is my 'string'"
print(my_kinda_string)
my_single_double_string = 'this is my "string"'
print(my_single_double_string)

# escape sequences
print("Escape \\ sequence")  # backslash
print("Escape \'sequence\'")  # single quote
print("Escape \"sequence\"")  # double quote
# print("Escape sequence \a")  #bell
print("Escape \n sequence")  # new line
print("Escape \t sequence")  # horizontal tab


print("appleappleappleappleappleapple\
appleappleappleappleappleapple")

# Math Operations
a = 10
b = 2
print("a =", a, ", b =", b)
print("add: ", a + b)
print("subtract: ", a - b)
print("multiply: ", a * b)
print("divide: ", b / a)
print("modulus: ", b % a)
print("exponent: ", a ** b)


running_total = 2 + 4 + 6
print(running_total)
running_total_doubled = running_total * 2
print(running_total_doubled)

# comparison operators
a = 10
b = 2
a == b
a != b
a > b
a < b
a >= b
a <= b

# assignment operators
x = 5
x += 2
print("x =", x)

x = 5
x -= 2
print("x =", x)

x = 5
x *= 2
print("x =", x)

x = 5
x /= 2
print("x =", x)

x = 5
x %= 2
print("x =", x)

x = 5
x //= 2
print("x =", x)

x = 5
x **= 2
print("x =", x)


# logic and truth
# booleans

# Truth Tables
x = 10 > 2
y = 15 != 5
# x and y == True

x = 10 < 2
y = 15 != 5
# x and y == False

x = 10 > 2
y = 15 == 5
# x and y == False

x = 10 < 2
y = 15 == 5
# x and y == False

# Flow Control

# If Statement
user_name = "Ada"
if user_name == "Ada":
    print("Hello Ada!")
if user_name == "Steven":
    print("Oh, it's Steven!")
# Else
else:
    print("Who the heck are you?!")

# elif

balance = 20
if balance < 0:
    print(" Balance is below 0, add funds now \
        or you will be charged a penalty.")
elif balance == 0:
    print("Balance is equal to 0, add funds soon.")
else:
    print("Balance is 0 or above.")

# Nested If Statements

balance = 0
below_zero_balance = 2 
if balance < 0:
    if below_zero_balance > 1: 
        fee = 25
    else:
        print("If your balance is below zero for more than 1 business day, you will be charged a $25 fee.")

elif balance == 0:
    print("Balance is equal to 0, add funds soon.")
else:
    print("Your balance is zero or above.")

# Compound Statements
user_color = "yellow"
user_age = 60
if user_color == "purple" and user_age > 90:
    print("Older people love purple!")
elif user_color == "green" and user_age > 90:
    print("You are a lizard king")
else:
    print("You are a mystery.")

# Lists
# Constructing a List
grocery_list = ["ice", "milk", "cheese"]
print(grocery_list)

# The Range Function
fav_numbers = list(range(0, 20, 2))
print(fav_numbers)

# Pulling items out of a list
print(grocery_list[0])
print(fav_numbers[5])
print(grocery_list[-1])

# Slicing a List
print(grocery_list[0:2])
print(fav_numbers[3:])
print(fav_numbers[-5:-1])

# List Membership and Length
print(grocery_list.count("butter"))
print(len(fav_numbers))

# Updating Lists
print(grocery_list)
grocery_list[0] = "cherries"
print(grocery_list[0])
print(grocery_list)
grocery_list[0:2] = "coffee", "curry"
print(grocery_list)
grocery_list.append("coffee")
print(grocery_list)
grocery_list2 = ["carrots", "broccoli", "yogurt"]
#grocery_list.append(grocery_list2)
#print(grocery_list)
grocery_list.extend(grocery_list2)
print(grocery_list)
grocery_list.remove("coffee")
print(grocery_list)
del grocery_list[1]
print(grocery_list)
del grocery_list[1:3]
print(grocery_list)
c = [4, 5, 6]
print(c)
c.pop(2)
print(c)

# List Methods
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)
#grocery_list.append(grocery_list2)
#print(grocery_list)
print(grocery_list + grocery_list2)
grocery_list = ",".join(grocery_list)
print(grocery_list)
print(dir(grocery_list))

# for loops
# The Range Function
for x in range(1, 20):
    print(x)

# step 5
for x in range(1, 20, 5):
    print(x)
else:
    print("The loop is over")


for letter in "tomatoes":
    print(letter)
for letter in "tomatoes":
    print("it's a fruit")

test_string = "testthisthing!"
for letter in test_string:
    print(letter)

for letter in test_string:
    print(letter + "no")

# Enumerating a list
fruit_list = ['apples', 'bananas', 'blueberries', 'oranges', 'mangos']
for index, fruit in enumerate(fruit_list):
    print(index, fruit)

fruits = ['apples', 'bananas', 'blueberries', 'oranges', 'mangos']

for index, fruit in enumerate(fruits):
    print("The fruit, {} is in position {}".format(fruit, str(index)))

# While Loops
response = ""

# while response != "Because!":
#     response = input("Why? ")
# print("Oh, ok then.")

#The Sentry Variable
counter = 0
while counter < 3:
    counter = counter + 1
    print("Nope: ", counter)
print("Yup")

# Break

count = 0
while True:
    count +=1
    if count > 10:
        break
    if count == 5:
        #skip 5
        continue
    print(count)

# List Comprehension
# String list comprehension
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
word_count = [len(w) for w in words]
print(word_count)

normalized_words_with_lengths = [[w.upper(), w.lower(), len(w)] for w in words]
print(normalized_words_with_lengths)

# Mathematical list comprehensions
s = [x**2 for x in range(10)]
print("s: ", s)
v= [2**i for i in range(10)]
print("v: ", v)
print(s,v)

# Filtering
m = [x for x in s if x%2 == 0]
print("m: ", m)
print(s, m)

n = [ x if x%2 ==0 else x/2 for x in s]
print("s: ", s)
print("n: ", n)

print(set("example"))