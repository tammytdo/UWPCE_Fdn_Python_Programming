"""

Assignment 03 

Calculating the sum of odd integers

"""


# For this assignment:

# Ask the user to enter a starting and ending number
# The user must not enter a starting number less than 1
# while loop will keep asking until a start number greater than 0 is entered
start_num = int(input("Enter a starting number greater than 0: "))
while start_num < 1:
    # Create checks and error messages for the above
    print("Number must be greater than 0.")
    print()
    start_num = int(input("Enter a starting number: "))
    print()

# if this prints, the program is outside of the loop
print("Starting number is: ", start_num)

# The user must enter an ending number at least 5 times greater than the starting number

end_num = int(input("Enter an ending number that is 5x greater than the starting number: "))
while end_num < int(start_num * 5):
    # Create checks and error messages for the above
    print("Number must be 5x greater than the starting number.")
    print()
    end_num = int(input("Enter an ending number: "))
    print()
print("Ending number is: ", end_num)


# Create a list of integers in the range of the starting and ending numbers
integers = range(start_num, end_num)

# Print out the number and index of each item in the list that is even
for index, integer in enumerate(range(start_num, (end_num + 1))):
    print("The integer {} is at index {}".format(index, integer))


# Sum all the odd numbers in the list using a for loop
# ( hint: append odd numbers to a list and then sum() that list)

# store the even numbers
even_int = []
# store the odd numbers
odd_int = []

for integer in integers:
    if integer % 2 == 0:
        even_int.append(integer)
    else:
        odd_int.append(integer)

sum_odd_int = sum(odd_int)

# Print out the cumulative sum calculated above
print("The sum of the odd integers is:", sum_odd_int)
