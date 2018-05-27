"""

Module 2 - Lab 2

Using boolean logic and if statements as flow control, write a program that: 

"""

import random


# Assign a random number between 50 and 100 to a variable called test_num
test_num = random.randint(50, 100)
print("Test number is:", test_num)

if test_num % 3 == 0 and test_num % 5 == 0:
    print("fizzbuzz")

# If test_num is divisible by three, print "fizz"
elif test_num % 3 == 0:
    print("fizz")

# If test_num is divisible by five, print "buzz"
elif test_num % 5 == 0:
    print("buzz")

# if test_num is divisible by both three and five, print "fizzbuzz!"
else:
    print("else")